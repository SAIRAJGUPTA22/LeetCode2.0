-- Write your PostgreSQL query statement below
with salaries AS 
(
SELECT E.id,E.name as Employee, salary,departmentid, d.name as Department,
dense_rank()OVER(PARTITION BY departmentid ORDER BY salary desc) as rnk
FROM Employee  E join DEPARTMENT D ON D.id = E.departmentid
)
SELECT Department,Employee,Salary FROM salaries WHERE rnk <4