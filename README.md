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




