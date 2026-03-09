from google.cloud import bigquery
from google.oauth2 import service_account

# important: Ensure that the service account key file is securely stored and not
# exposed in version control or public repositories.

# query BigQuery using the service account credentials

credentials = service_account.Credentials.from_service_account_file("/tmp/gcp_key.json")

client = bigquery.Client(project="capitalbikeshare-489408", credentials=credentials)

query = """
SELECT
  FORMAT_DATE('%A', DATE(started_at)) AS weekday,
  EXTRACT(DAYOFWEEK FROM started_at) AS weekday_order,
  member_casual,
  start_lat,
  start_lng,
  COUNT(*) AS trip_count
FROM `capitalbikeshare-489408.02_2026.tripdata`
WHERE
  started_at IS NOT NULL
  AND start_lat IS NOT NULL
  AND start_lng IS NOT NULL
GROUP BY weekday, weekday_order, member_casual, start_lat, start_lng
ORDER BY weekday_order, trip_count DESC
"""

df = client.query(query).to_dataframe()
# Save once
df.to_csv("tripdata.csv", index=False)
