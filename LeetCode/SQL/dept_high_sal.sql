# Write your MySQL query statement below
#select d.Name as Department, e.Name as Employee, Max(Salary) as Salary
#from Employee as e join Department as d on e.DepartmentId = d.Id
#group by d.Name
#having e.Name = (select Name from Employee as x 
#                 where salary = Salary and e.DepartmentID = x.DepartmentID );

select d.Name as Department, e.Name as Employee, e.Salary as Salary
from Employee as e join Department as d on e.DepartmentId = d.Id
where (e.DepartmentID, Salary) in (select DepartmentID, max(Salary) 
                                from Employee
                                group by DepartmentID);