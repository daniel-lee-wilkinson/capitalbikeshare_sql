SELECT
  member_casual,
  COUNT(*) AS trip_count,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM trips), 1) AS percent_of_total
FROM trips
GROUP BY member_casual;