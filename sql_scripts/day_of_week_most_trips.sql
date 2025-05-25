SELECT
  strftime('%w', started_at) AS weekday,
  COUNT(*) AS trip_count
FROM trips
WHERE started_at IS NOT NULL
GROUP BY weekday
ORDER BY trip_count DESC;


----
SELECT
  strftime('%w', started_at) AS weekday,
  COUNT(*) AS trip_count
FROM trips
WHERE started_at IS NOT NULL
GROUP BY weekday
ORDER BY
  CASE strftime('%w', started_at)
    WHEN '1' THEN 1  -- Monday
    WHEN '2' THEN 2
    WHEN '3' THEN 3
    WHEN '4' THEN 4
    WHEN '5' THEN 5
    WHEN '6' THEN 6
    WHEN '0' THEN 7  -- Sunday last
  END;