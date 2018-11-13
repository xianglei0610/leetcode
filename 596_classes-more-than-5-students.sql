# Write your MySQL query statement below

select A.class from  (select  distinct student,class  from courses ) as A group by A.class having   count(A.student)>=5;