# Write your MySQL query statement below

select s1.Score as Score, count(s2.Score) as Rank from Scores as s1 left join (select distinct Score from Scores) as s2 on s1.Score <= s2.Score group by s1.id order by s1.Score desc

