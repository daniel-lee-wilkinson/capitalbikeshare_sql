SELECT
  ROUND(AVG((julianday(ended_at) - julianday(started_at)) * 1440), 1) AS avg_trip_minutes
FROM trips
WHERE started_at IS NOT NULL
  AND ended_at IS NOT NULL
  AND julianday(ended_at) > julianday(started_at);