WITH actual_trips AS
(
SELECT * FROM Trips
WHERE client_id in (SELECT users_id FROM Users WHERE banned ='No')
AND driver_id in (SELECT users_id FROM Users WHERE banned ='No')
and request_at between '2013-10-01' and '2013-10-03'
),
fulfilled_trips AS
(
SELECT request_at, coalesce(COUNT(*),0) as fulfilled
FROM actual_trips
WHERE status !='completed'
GROUP BY request_at
),
total_trips AS
(
SELECT request_at, coalesce(COUNT(*),0) as total
FROM actual_trips
GROUP BY request_at
)
SELECT a.request_at as day , round(coalesce(fulfilled::numeric/total,0),2) as "Cancellation Rate"
FROM total_trips a LEFT JOIN fulfilled_trips f
on a.request_at = f.request_at
order by a.request_at