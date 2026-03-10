import os

from google.cloud import bigquery
from google.oauth2 import service_account


def _get_env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None or value.strip() == "":
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def create_client(project_id: str) -> bigquery.Client:
    # If GOOGLE_APPLICATION_CREDENTIALS is set, use it explicitly.
    # Otherwise, fall back to Application Default Credentials.
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if credentials_path:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path
        )
        return bigquery.Client(project=project_id, credentials=credentials)
    return bigquery.Client(project=project_id)


def build_query(table_id: str) -> str:
    return f"""
SELECT
  FORMAT_DATE('%A', DATE(started_at)) AS weekday,
  EXTRACT(DAYOFWEEK FROM started_at) AS weekday_order,
  member_casual,
  start_lat,
  start_lng,
  COUNT(*) AS trip_count
FROM `{table_id}`
WHERE
  started_at IS NOT NULL
  AND start_lat IS NOT NULL
  AND start_lng IS NOT NULL
GROUP BY weekday, weekday_order, member_casual, start_lat, start_lng
ORDER BY weekday_order, trip_count DESC
"""


def main():
    project_id = _get_env("BQ_PROJECT_ID", os.getenv("GOOGLE_CLOUD_PROJECT"))
    table_id = _get_env("BQ_TABLE_ID")
    output_csv = os.getenv("BQ_OUTPUT_CSV", "tripdata.csv")

    client = create_client(project_id)
    query = build_query(table_id)

    df = client.query(query).to_dataframe()
    df.to_csv(output_csv, index=False)
    print(f"Saved {len(df)} rows to {output_csv}")


if __name__ == "__main__":
    main()
