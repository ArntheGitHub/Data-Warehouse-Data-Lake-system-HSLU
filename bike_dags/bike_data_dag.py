import requests
import psycopg2
import uuid
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from psycopg2.extras import execute_values

DB_CONFIG = {
    'dbname': 'bikes',
    'user': 'postgres',
    'password': '',
    'host': 'localhost',
    'port': '5432'
}

API_URL = "https://gbfs.prod.sharedmobility.ch/free_bike_status.json"

def generate_run_id():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    unique_id = str(uuid.uuid4())[:8]
    return f"BIKE_{timestamp}_{unique_id}"

def store_bike_data():
    run_id = generate_run_id()
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        bikes = response.json()['data']['bikes']
        
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS bike_status (
                run_id VARCHAR(30),
                bike_id VARCHAR(100),
                provider_id VARCHAR(100),
                lat FLOAT,
                lon FLOAT,
                is_reserved BOOLEAN,
                is_disabled BOOLEAN,
                timestamp TIMESTAMP,
                PRIMARY KEY (run_id, bike_id)
            );
            
            CREATE TABLE IF NOT EXISTS run_summary (
                run_id VARCHAR(30) PRIMARY KEY,
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                total_bikes INTEGER,
                status VARCHAR(20)
            );
        """)

        current_time = datetime.now()
        cur.execute(
            "INSERT INTO run_summary (run_id, start_time, total_bikes, status) VALUES (%s, %s, %s, %s)",
            (run_id, current_time, len(bikes), 'IN_PROGRESS')
        )

        bike_data = [(
            run_id,
            bike['bike_id'],
            bike['provider_id'],
            bike['lat'],
            bike['lon'],
            bike['is_reserved'],
            bike['is_disabled'],
            current_time
        ) for bike in bikes]

        execute_values(cur, """
            INSERT INTO bike_status (
                run_id, bike_id, provider_id, lat, lon, 
                is_reserved, is_disabled, timestamp
            ) VALUES %s
        """, bike_data)

        cur.execute(
            "UPDATE run_summary SET status = 'COMPLETED', end_time = %s WHERE run_id = %s",
            (datetime.now(), run_id)
        )

        conn.commit()

    except Exception as e:
        if 'conn' in locals() and 'cur' in locals():
            cur.execute(
                "UPDATE run_summary SET status = 'FAILED', end_time = %s WHERE run_id = %s",
                (datetime.now(), run_id)
            )
            conn.commit()
        raise
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

dag = DAG(
    'bike_data_collection',
    default_args={
        'owner': 'airflow',
        'retries': 3,
        'retry_delay': timedelta(minutes=2),
        'execution_timeout': timedelta(minutes=5),
    },
    schedule_interval=timedelta(minutes=10),
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

PythonOperator(
    task_id='fetch_bike_data',
    python_callable=store_bike_data,
    dag=dag,
)