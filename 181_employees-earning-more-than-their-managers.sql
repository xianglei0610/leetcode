# Write your MySQL query statement below

select e1.Name as Employee  from Employee e1 left join Employee e2 on  e2.Id=e1.ManagerId where e1.Salary > e2.Salary;