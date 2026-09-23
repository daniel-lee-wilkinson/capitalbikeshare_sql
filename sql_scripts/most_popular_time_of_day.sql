SELECT strftime('%H', started_at) AS hour, COUNT(*) AS trip_count
FROM trips
WHERE started_at IS NOT NULL
GROUP BY hour
ORDER BY hour;