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





