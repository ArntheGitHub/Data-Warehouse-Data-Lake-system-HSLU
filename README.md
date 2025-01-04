# **Data Warehouse & Data Lake System - HSLU**  
## **Weather Impact on Public Transport and Shared Mobility in Switzerland**  

### **Overview**  
This repository contains the code, pipelines, and resources developed for the **"Data Warehouse & Data Lake System"** project at Lucerne University of Applied Sciences and Arts (HSLU).   
The project investigates how weather conditions influence public transport and shared mobility services across Switzerland, offering insights into sustainable urban mobility strategies. By integrating real-time data from multiple sources, this project aims to support data-driven decision-making for urban planners and transport authorities.  

---

## **Repository Structure**  

### **1. Lambda Functions**  
#### **Data Lake (ETL Pipelines):**  
Serverless AWS Lambda functions are used to automate data ingestion, processing, and storage in the data lake. These pipelines ensure continuous, real-time data collection from external APIs.  

- **`lambda_free_float_location.py`** – Ingests hourly data on free-floating vehicles (e.g., bikes, scooters) and updates the data lake.  
- **`lambda_station_status.py`** – Retrieves station-based vehicle data, applies filters, and stores the results in the data lake.  
- **`lambda_weather.py`** – Collects hourly weather data from OpenWeatherMap and uploads it to the data lake.  
- **`lambda_station_loc.py`** – Gathers station location data and maps it to Zurich neighborhoods. This function runs as a one-time job.  
- **`lambda_provider.py`** – Imports provider information for shared mobility services and stores it in the data lake.  

#### **Data Warehouse (ELT Pipelines):**  
Lambda functions transfer processed data from the data lake to the data warehouse for structured storage and analysis.  

- **`lambda_data_warehouse.py`** – Transfers daily weather and mobility data from the data lake to the data warehouse.  
- **`lambda_static_location_warehouse.py`** – Loads static location data, such as neighborhood boundaries, into the data warehouse.  
- **`lambda_static_provider_warehouse.py`** – Migrates provider data from the data lake to the warehouse for further processing.  

---

### **2. Data Exploration**  
- **`Explore_Data.ipynb`** – Jupyter Notebook for initial data exploration, visualization, and preliminary analysis of the ingested datasets.  

---

### **3. Test Project**  
- **`test_project/`** – Proof-of-concept code that validates the feasibility and performance of core project components, such as data ingestion and ETL pipelines.  

---

## **Data Sources**  

### **1. OpenWeatherMap API**  
- Provides real-time and historical weather data across six major Swiss cities.   
- **Key Variables**: Temperature, humidity, wind speed, and weather conditions.   
- This data is used to evaluate the influence of weather on public transport reliability and shared mobility usage patterns.  

### **2. Swiss Shared Mobility API**  
- Supplies real-time data on shared mobility services (e.g., bikes and e-scooters), covering availability, reservations, and vehicle status.   
- **Key Variables**: Geolocation, provider details, reservation status, and operational state.  

### **3. Swiss Federal Railways (SBB) API**  
- Offers insights into public transport networks, including hourly station usage trends and route coverage. This data aids in analyzing passenger flow and potential disruptions.  

---

## **Project Goals**  
The primary objective of this project is to create an end-to-end data pipeline that supports the analysis of weather's impact on public transport and shared mobility, ultimately contributing to sustainable urban transport systems.  

### **1. Data Lake Implementation:**  
- Design and implement a data lake to store and manage raw data from external APIs.  
- Utilize AWS S3 for scalable and cost-effective storage of heterogeneous datasets.  

### **2. Data Warehouse Design:**  
- Develop a structured data warehouse using PostgreSQL to facilitate efficient querying, reporting, and visualization.  
- Implement ETL processes that transform and load data from the data lake into the warehouse, ensuring data integrity and accuracy.  

### **3. Key Research Questions:**  
- **How do weather conditions affect public transport reliability and shared mobility usage?**   
- **What is the impact of extreme weather events on shared mobility demand and fleet distribution?**   
- **How can shared mobility services reduce carbon emissions during weather-induced disruptions in public transport?**   
- **What long-term environmental benefits can be achieved by integrating shared mobility and public transport systems during adverse weather conditions?**  

---

## **Future Enhancements**  
- **Enhanced Geospatial Analysis** – Integrate neighborhood-level data to enable more granular, localized insights.  
- **Predictive Modeling** – Implement machine learning models to forecast public transport disruptions and recommend shared mobility interventions.  
- **Additional Data Sources** – Expand to include traffic, socioeconomic, and demographic data for a more comprehensive analysis of urban mobility patterns.  
- **User Behavior Insights** – Incorporate survey data and mobility app usage to analyze the behavioral factors influencing shared mobility adoption.  

---

This project serves as a scalable foundation for future studies and real-world applications in sustainable urban mobility and environmental planning.
