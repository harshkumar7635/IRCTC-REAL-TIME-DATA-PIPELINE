from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "central-rush-450208-g6"
DATASET_ID = "irctc_realtime"
TABLE_ID = "train_data"

CSV_FILE = "train_data.csv"

client = bigquery.Client(project=PROJECT_ID)

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

df = pd.read_csv(CSV_FILE)

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_APPEND"
)

job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=job_config
)

job.result()

print("✅ Train data successfully loaded into BigQuery!")
print(f"📊 Rows loaded: {len(df)}")