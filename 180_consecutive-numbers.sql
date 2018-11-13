# Write your MySQL query statement below


select distinct(L1.Num) as ConsecutiveNums  from Logs L1
left join Logs L2 on L1.Id =L2.id-1
left join Logs L3 on L2.Id =L3.id-1
where L1.Num =L2.Num and L1.Num = L3.Num;