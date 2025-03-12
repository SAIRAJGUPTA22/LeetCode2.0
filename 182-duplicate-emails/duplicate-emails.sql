-- Write your PostgreSQL query statement below
SELECT email as Email FROM Person 
group by email 
having count(id)>=2