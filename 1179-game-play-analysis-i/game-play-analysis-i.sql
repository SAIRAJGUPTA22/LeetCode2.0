-- Write your PostgreSQL query statement below
with cte_1 AS(
SELECT player_id,event_date, row_number()over(partition by player_id order by event_date)
as rnk
FROM Activity 
)
SELECT player_id, event_date as first_login FROM cte_1
WHERE rnk =1
