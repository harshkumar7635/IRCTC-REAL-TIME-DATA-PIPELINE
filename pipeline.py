from google.cloud import bigquery

PROJECT_ID = "central-rush-450208-g6"
DATASET_ID = "irctc_realtime"
VIEW_ID = "train_dashboard"

client = bigquery.Client(project=PROJECT_ID)

query = f"""
SELECT *
FROM `{PROJECT_ID}.{DATASET_ID}.{VIEW_ID}`
ORDER BY last_updated DESC
"""

query_job = client.query(query)

print("\n🚆 IRCTC TRAIN DASHBOARD DATA\n")

for row in query_job.result():
    print(dict(row))
