# Write your MySQL query statement below
SELECT distinct 
    i1.num as ConsecutiveNums 
FROM 
    logs i1  join 
    logs i2 ON  
    i1.id=i2.id+1   join 
    logs i3 ON i2.id=i3.id+1 

WHERE   i1.num=i2.num AND 
    i2.num=i3.num