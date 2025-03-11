-- Write your PostgreSQL query statement below
SELECT E1.name as Employee FROM 
Employee E1 Join Employee E2 ON E1.managerId = E2.id
WHERE E1.Salary > E2.Salary