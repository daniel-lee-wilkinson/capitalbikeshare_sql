SELECT
  CASE
    WHEN duration_min <= 5 THEN '0–5 min'
    WHEN duration_min <= 15 THEN '5–15 min'
    WHEN duration_min <= 30 THEN '15–30 min'
    ELSE '30+ min'
  END AS duration_category,
  COUNT(*) AS trip_count
FROM (
  SELECT
    (julianday(ended_at) - julianday(started_at)) * 1440 AS duration_min
  FROM trips
  WHERE started_at IS NOT NULL AND ended_at IS NOT NULL
) AS sub
GROUP BY duration_category
ORDER BY trip_count DESC;