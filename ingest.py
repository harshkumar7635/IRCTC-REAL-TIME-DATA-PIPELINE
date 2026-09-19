from google.cloud import bigquery
import pandas as pd
import logging

PROJECT_ID = "central-rush-450208-g6"
DATASET_ID = "irctc_realtime"
TABLE_ID = "train_data"

CSV_FILE = "train_data.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = bigquery.Client(project=PROJECT_ID)

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

try:
    logging.info("Reading train data from CSV...")
    df = pd.read_csv(CSV_FILE)

    logging.info(f"Rows found: {len(df)}")

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )

    logging.info("Loading data into BigQuery...")

    job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    job.result()

    logging.info("Train data successfully loaded into BigQuery!")
    logging.info(f"Rows loaded: {len(df)}")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")