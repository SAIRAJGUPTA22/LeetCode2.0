WITH actual_trips AS (
    SELECT t.*
    FROM Trips t
    JOIN Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
    JOIN Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
),
trip_stats AS (
    SELECT 
        request_at,
        COUNT(*) AS total_trips,
        SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) AS cancelled_trips
    FROM actual_trips
    GROUP BY request_at
)
SELECT 
    request_at AS "Day",
    ROUND(COALESCE(cancelled_trips::numeric / total_trips, 0), 2) AS "Cancellation Rate"
FROM trip_stats
ORDER BY request_at;
