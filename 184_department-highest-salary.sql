# Write your MySQL query statement below

select d.Name as Department   ,e.name as Employee  ,e.Salary  from Employee as e,

(select max(Salary ) as Salary, DepartmentId from Employee  group by DepartmentId) t1,
Department  as d
where e.DepartmentId =t1.DepartmentId and e.Salary =t1.Salary and e.DepartmentId =d.id
;