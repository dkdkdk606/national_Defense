/*
유니온(UNION)
- 여러 테이블을 위/아래로 합치기
- 합치는 테이블들의 칼럼이 모두 동일해야 함
*/

create schema uniondb;
use uniondb;
# 임포트 위자드로 테이블 생성
CREATE table inquiry_2018(
	id int
);

LOAD DATA INFILE 'C:/Workspaces/02_DB/코드/data/inquiry_2018.csv'
INTO TABLE inquiry_2018
CHARACTER SET utf8mb4
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from uniondb.inquiry2018;
desc uniondb.inquiry2018;
 
-- 2018과 2019를 union
select * from uniondb.inquiry2018
union
select * from uniondb.inquiry2019;
 
-- 2018과 2020를 union
select * from uniondb.inquiry2018
union
select * from uniondb.inquiry2020;
 
-- 2019과 2020를 union
select * from uniondb.inquiry2019
union
select * from uniondb.inquiry2020;
 
 
select * from uniondb.inquiry2018
union
(select * from uniondb.inquiry2019 
 limit 1);
 
select * from uniondb.inquiry2018
union
select * from uniondb.inquiry2019 
limit 1;
 
(select * from uniondb.inquiry2018
limit 2)
union
(select * from uniondb.inquiry2019 
limit 1);
 
(select * from uniondb.inquiry2018
limit 3)
union
(select * from uniondb.inquiry2020 
limit 2)
order by star desc;