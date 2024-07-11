# Write your MySQL query statement below
SELECT name, bonus
FROM Employee E
LEFT JOIN Bonus B ON E.empId = B.empId
WHERE bonus < 1000 
   OR NOT EXISTS (SELECT *
                  FROM Bonus B2 
                  WHERE B2.empId = E.empId);
