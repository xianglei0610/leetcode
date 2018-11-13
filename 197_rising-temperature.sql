# Write your MySQL query statement below

select w1.Id as Id  from  Weather w1 ,Weather w2 where w1.Temperature>w2.Temperature and subdate(w1.RecordDate,1) = w2.RecordDate;