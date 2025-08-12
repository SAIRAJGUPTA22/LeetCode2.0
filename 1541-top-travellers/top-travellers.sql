# Write your MySQL query statement below
select name,coalesce(total_distance,0) as travelled_distance
from users u left join (select user_id,sum(distance) as total_distance
from Rides
group by user_id) R ON u.id = R.user_id 
order by total_distance desc,name asc