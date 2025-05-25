SELECT strftime('%H', started_at) AS hour, COUNT(*) AS trip_count
FROM trips
GROUP BY hour
ORDER BY hour;