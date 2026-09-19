# 🚆 IRCTC Real-Time Data Pipeline

A Python-based railway data pipeline that processes train information and stores it in Google BigQuery for analysis and monitoring.

## 📌 Project Overview

This project demonstrates a cloud-based data pipeline for railway/train data using Python and Google Cloud BigQuery.

The pipeline retrieves train data from BigQuery and displays the latest railway information, including train status, delays, stations, platforms, and update timestamps.

## 🛠️ Tech Stack

- Python
- Google Cloud BigQuery
- Google Cloud Python Client Library
- Pandas
- SQL
- Git & GitHub

## 📊 Data Fields

The train dataset contains:

- Train Number
- Train Name
- Source Station
- Destination Station
- Departure Time
- Arrival Time
- Status
- Delay (Minutes)
- Platform Number
- Last Updated

## ⚙️ Project Structure

```text
IRCTC-REAL-TIME-DATA-PIPELINE/
│
├── pipeline.py
├── train_data.csv
├── requirements.txt
├── .gitignore
└── README.md

## 🏗️ Project Architecture

```text
train_data.csv
      ↓
Python Ingestion (ingest.py)
      ↓
Data Validation & Logging
      ↓
Google BigQuery
      ↓
SQL Analysis
      ↓
Dashboard / Analytics

## 🚀 How to Run

### 1. Activate Virtual Environment

```bash
venv\Scripts\activate

### 2. Install Dependencies

```bash
pip install -r requirements.txt

### 3. Run the Data Ingestion Pipeline

```bash
python ingest.py

### 4. Run the Dashboard Query

```bash
python pipeline.py

## 📌 Project Highlights

- Built a Python-based batch data ingestion pipeline for railway train data.
- Implemented data validation and logging using Pandas and Python.
- Stored and analyzed train data using Google BigQuery Sandbox.
- Created SQL views for train status, delays, route analysis and station performance.
- Developed a Python dashboard query to retrieve the latest train analytics.
- Used Git and GitHub for version control and project management.

> Note: Due to BigQuery Sandbox limitations, the pipeline uses batch/micro-batch ingestion instead of true real-time streaming.

## 📂 Project Structure

```text
IRCTC-REAL-TIME-DATA-PIPELINE/
│
├── ingest.py              # CSV → BigQuery data ingestion
├── pipeline.py            # BigQuery dashboard query
├── train_data.csv         # Sample railway train data
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore             # Ignored files and folders
└── README.md              # Project documentation

## ☁️ Google Cloud & BigQuery

- **Cloud Platform:** Google Cloud Platform (GCP)
- **Data Warehouse:** Google BigQuery
- **Dataset:** `irctc_realtime`
- **Table:** `train_data`
- **Processing:** SQL-based analytics and BigQuery views
- **Ingestion:** Python + Pandas batch/micro-batch pipeline

> The project uses BigQuery Sandbox to maintain a no-billing development setup. Therefore, the pipeline uses batch/micro-batch ingestion rather than true streaming.

## 🔐 Security

- Sensitive configuration is stored in `.env`.
- `.env` is excluded from Git using `.gitignore`.
- `.env.example` is provided as a safe configuration template.
- No credentials or private keys are stored in the repository.

## 👨‍💻 Author

**Harsh Kumar**  
B.Tech — Metallurgical and Materials Engineering  
NIT Tiruchirappalli

GitHub: `https://github.com/harshkumar7635`

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Cloud Platform:** Google Cloud Platform (GCP)
- **Data Warehouse:** Google BigQuery
- **Query Language:** SQL
- **Authentication:** Google Cloud Application Default Credentials
- **Version Control:** Git & GitHub
- **Development Environment:** VS Code

## 📊 Data Fields

The train dataset contains the following fields:

| Field | Description |
|---|---|
| `train_number` | Unique train number |
| `train_name` | Name of the train |
| `source_station` | Starting station |
| `destination_station` | Destination station |
| `departure_time` | Scheduled departure time |
| `arrival_time` | Scheduled arrival time |
| `status` | Current train status |
| `delay_minutes` | Delay duration in minutes |
| `platform_number` | Assigned platform number |
| `last_updated` | Timestamp of the latest ingestion |






