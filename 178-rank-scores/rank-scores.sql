# Write your MySQL query statement below
SELECT score, dense_rank()Over(order by score desc) as 'rank'
from scores