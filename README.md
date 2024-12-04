# Data Warehouse & Data Lake System - HSLU

## Weather Impact on Public Transport and Shared Mobility in Switzerland

### **Overview**
This repository contains the code and resources developed for the **"Data Warehouse & Data Lake System"** project at Lucerne University of Applied Sciences and Arts (HSLU).  
The project explores the influence of weather conditions on public transport and shared mobility services in Switzerland, aiming to provide insights for sustainable urban mobility strategies.

---

## **Repository Structure**

### **1. Lambda Functions**
#### **Data Lake (ETL Pipelines):**
- **`lambda_free_float_location.py`**: Processes hourly data on free-floating vehicles (e.g., scooters) and uploads to the data lake.
- **`lambda_station_status.py`**: Fetches station-based vehicle data, applies filtering, and stores it in the data lake.
- **`lambda_weather.py`**: Collects hourly weather data and uploads it to the data lake.
- **`lambda_station_loc.py`**: Fetches station locations and links them to Zurich neighborhoods. Runs only once.
- **`lambda_provider.py`**: Loads provider data for shared mobility services into the data lake.

#### **Data Warehouse (ELT Pipelines):**
- **`lambda_data_warehouse.py`**: Populates the data warehouse from the data lake with daily weather and mobility data.
- **`lambda_static_location_warehouse.py`**: Uploads static neighborhood data directly to the data warehouse.
- **`lambda_static_provider_warehouse.py`**: Transfers provider data from the data lake to the warehouse.

### **2. Data Exploration**
- **`Explore_Data.ipynb`**: Initial exploration and visualization of data sources.

### **3. Test Project**
- **`test_project/`**: Proof-of-concept code to validate project feasibility.

---

## **Data Sources**

### **1. OpenWeatherMap API**
- Provides real-time and historical weather data for six major Swiss cities.
- **Key Variables**: Temperature, humidity, wind speed, and weather conditions.

### **2. Swiss Shared Mobility API**
- Offers real-time data on shared mobility services (e.g., scooters, bikes).
- **Key Variables**: Vehicle status, geolocation, and reservation details.

### **3. Swiss Federal Railways (SBB)**
- Includes hourly and annual station user trends and route network details.

---

## **Project Goals**
1. **Data Lake Implementation**:
   - Ingest, transform, and store raw data from APIs into an S3 bucket.
2. **Data Warehouse Design**:
   - Integrate structured data for in-depth analysis and visualization.
3. **Key Research Questions**:
   - Impact of weather conditions on public transport reliability and shared mobility usage.
   - Carbon emission analysis of weather-induced changes in transport patterns.
   - Long-term environmental benefits of integrating mobility systems during extreme weather.

---
