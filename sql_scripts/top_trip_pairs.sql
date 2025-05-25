SELECT
  start_station_name,
  end_station_name,
  COUNT(*) AS trip_count
FROM trips
WHERE start_station_name IS NOT NULL
  AND end_station_name IS NOT NULL
GROUP BY start_station_name, end_station_name
ORDER BY trip_count DESC
LIMIT 10;