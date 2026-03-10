-- Ordered by trip volume (descending)
WITH weekday_trips AS (
  SELECT
    strftime('%w', started_at) AS weekday_num,
    COUNT(*) AS trip_count
  FROM trips
  WHERE started_at IS NOT NULL
  GROUP BY weekday_num
)
SELECT
  CASE weekday_num
    WHEN '0' THEN 'Sunday'
    WHEN '1' THEN 'Monday'
    WHEN '2' THEN 'Tuesday'
    WHEN '3' THEN 'Wednesday'
    WHEN '4' THEN 'Thursday'
    WHEN '5' THEN 'Friday'
    WHEN '6' THEN 'Saturday'
    ELSE 'Unknown'
  END AS weekday_name,
  trip_count
FROM weekday_trips
ORDER BY trip_count DESC;


----

-- Ordered Monday → Sunday
WITH weekday_trips AS (
  SELECT
    strftime('%w', started_at) AS weekday_num,
    COUNT(*) AS trip_count
  FROM trips
  WHERE started_at IS NOT NULL
  GROUP BY weekday_num
)
SELECT
  CASE weekday_num
    WHEN '0' THEN 'Sunday'
    WHEN '1' THEN 'Monday'
    WHEN '2' THEN 'Tuesday'
    WHEN '3' THEN 'Wednesday'
    WHEN '4' THEN 'Thursday'
    WHEN '5' THEN 'Friday'
    WHEN '6' THEN 'Saturday'
    ELSE 'Unknown'
  END AS weekday_name,
  trip_count
FROM weekday_trips
ORDER BY
  CASE weekday_num
    WHEN '1' THEN 1  -- Monday
    WHEN '2' THEN 2
    WHEN '3' THEN 3
    WHEN '4' THEN 4
    WHEN '5' THEN 5
    WHEN '6' THEN 6
    WHEN '0' THEN 7  -- Sunday last
  END;