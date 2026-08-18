# 크로스(cross) 조인과 셀프(self) 조인
/*
1. 크로스 조인(cross join)
 - 두 테이블의 모든 경우의 수를 조합한 데이터가 필요할 때
 - 형식: 
	select 컬럼명
		from 테이블1
        cross join 테이블2
        where 검색조건;
*/

# 스키마와 테이블 생성
create schema exdb;
use exdb;

create table department(
	dptNo varchar(5),
    dptName varchar(10)
);

create table location(
	locNo varchar(5),
    locName varchar(10)
);


# 데이터 삽입
insert into department (dptNo, dptName)
    values ('1','영업'),('2','마케팅'),('3','인사');

insert into location (locNo, locName)
	values ('01', '서울'), ('02','부산'), ('03', '인천'), ('04','대전');

select *
	from location
    cross join department
    order by locNo, dptNo;

/*
2. 셀프조인
	- 자신과의 내부 조인
    - 동일한 테이블 사용
    - 반드시 별칭을 사용해야 함
    - 형식 :
		select ...
			from 테이블 A(별칭)
            [inner] join 테이블 B(별칭)
            on A.칼럼 = B.칼럼
               
    
    
    
    - 사용 목적 :
		1) 계층구조(트리구조) 표현
			- 조직도(상사-부하관계)
            - 카테고리(대분류-중분류-소분류)
            - 부품구조
		2) 같은 테이블내의 데이터 비교
			- 같은 부서 내 다른 직원 정보 비교
            - 같은 제품군에서 가격 비교
*/

select A.dptName, B.dptName
	from exdb.department as A
    inner join exdb.department as B
    on A.dptNo = B.dptNo;


use exdb;
-- 예제 데이터
create table employee(
	empNo int primary key,
    empName varchar(20) not null,
    job varchar(30),
    managerNo int,
    salary int
);

insert into employee values
	(1001, '김대표', '대표이사', null, 10000000),
    (1002, '이부장', '개발부장', 1001, 7000000),
    (1003, '박부장', '영업부장', 1001, 6800000),
    (1004, '최과장', '개발과장', 1002, 5000000),
    (1005, '정대리', '개발대리', 1004, 4000000),
    (1006, '강사원', '개발사원', 1004, 3200000),
    (1007, '윤과장', '영업과장', 1003, 4800000),
    (1008, '한사원', '영업사원', 1007, 3000000);

/* 관계도

김대표(1001)
   │
   ├─────────────────┐
   ↓                 ↓
이부장(1002)       박부장(1003)
   │                 │
   ↓                 ↓
최과장(1004)       윤과장(1007)
   │                 │
 ┌─┴──────┐          ↓
 ↓        ↓      한사원(1008)
정대리  강사원
(1005)  (1006)

*/
-- 직원 이름과 관리자 이름 조회하기
-- employee 테이블에는 관리자 이름이 저장되어 있지 않음
-- => 자기 자신과의 조인 필요
select *
	from employee E
    inner join employee M
    on E.managerNo = M.empNo;

select E.empName as 직원, M.empName as 관리자
	from employee E
    inner join employee M
    on E.managerNo = M.empNo;
    
select E.empName as 직원, M.empName as 관리자
	from employee E
    left join employee M
    on E.managerNo = M.empNo;

select E.empName as 직원,
	ifnull(M.empName, '관리자 없음') as 관리자
	from employee E
    left join employee M
    on E.managerNo = M.empNo;

select E.empName as 직원,
	ifnull(M.empName, '관리자 없음') as 관리자
	from employee E, employee M
    where E.managerNo = M.empNo;

select E.empName as 직원,
	ifnull(M.empName, '관리자 없음') as 관리자
	from employee E, employee M
    where E.managerNo = M.empNo or isnull(E.managerNo);




# 공통테이블 표현식(Common Table Expression:CTE)
-- MySQL 8.0 이후 제공
/*
    실제 데이터베이스에 생성되는 테이블은 아니지만
    쿼리 실행 결과를 테이블 처럼 활용하기 위한 논리적 테이블을 만들 때 사용

    [형식]
    with [테이블명] (열이름1, 열이름2, ...)
		AS
		(
			<select문>
		)

	select [열이름] from [테이블명]
    
[목적]
1. 복잡한 SQL 단순화 : 긴 SQL을 여러 단계로 분리
2. 가독성 향상 : 중첩된 서브쿼리를 이해하기 쉽게 표현
3. 결과 재사용 : 하나의 SQL에서 CTE 결과를 여러 번 참조
4. 단계적 데이터 처리 : 조회 -> 집계 -> 필터링 등을 단계별 처리
5. 재귀 처리 : 조직도, 카테고리, 계층 구조 처리
6. 유지보수 향상 : SQL의 각 처리 단계가 명확해짐
*/
with loc_dpt (locNo, locName, dptNo, dptName)
as
(
    select locNo, locName, dptNo, dptName
    from location
    cross join department
)
select * from loc_dpt;

-- 출판사별 평균 도서가격이 20000원 이상인 출판사 조회
with avg_pub (pub, avgPrice)
as
(
select pub, avgPrice
from book

)

use bookdb;

select B.pubNo, P.pubname, avg(B.bookprice)
	from bookdb.book B
    join bookdb.publisher P
    on B.pubNo = P.pubNo
    group by B.pubNo;

select P.pubNo, P.pubName, avg(bookprice) as avgPrice
	from bookdb.book B
    join bookdb.publisher P
    on B.pubNo = P.pubNo
    group by P.pubNo
    having avgPrice >= 25000;

with pubAvg as (
select P.pubNo, P.pubName, avg(bookprice) as avgPrice
	from bookdb.book B
    join bookdb.publisher P
    on B.pubNo = P.pubNo
    group by P.pubNo
)
select * from pubAvg
	where avgPrice >= 25000;

-- CTE 처리 흐름 단계
/*
    1단계. book 테이블과 publisher 테이블을 조인
    2단계. 출판사번호별로 group by
    3단계. 평균가격 계산
    4단계. pubAVg 공통테이블 표현
    5단계. pubAVg 공통테이블에서 평균가격 >= 25000
    6단계. 최종 결과
=> 서브쿼리나 복잡한 질의문에 대하여 CTE로 표현할 경우 단순화, 가독성 향상

-- 고객의 구매금액이 10만원 이상인 고객 추출
*/

select BC.clientName, sum(BS.bsQty*B.bookprice) as sumprice
	from bookdb.bookclient BC
    join bookdb.booksale BS
		on BC.clientNo = BS.clientNo
    join bookdb.book B
		on BS.bookNo = B.bookNo
    group by BC.clientNo
    having sumprice >= 100000;

with clientTotal as(
select BC.clientName, sum(BS.bsQty*B.bookprice) as sumprice
	from bookdb.bookclient BC
    join bookdb.booksale BS
		on BC.clientNo = BS.clientNo
    join bookdb.book B
		on BS.bookNo = B.bookNo
    group by BC.clientNo
),
highClient as (
	select * from clientTotal
	where sumprice >= 100000
)
select * from highClient
	order by sumprice desc
    limit 1;

-- 재귀 CTE
/*
[형식]
with recursive CTE이름 as (
	-- Anchor query
	select ...

    union all
	
    -- Recursive query
    select ...
    from 테이블
    join CTE이름
    on ...
)
select 컬럼 from CTE이름

-- 재귀CTE에는 Anchor Query와 Recursive Query 두 부분이 있음
첫번째 Anchor Query : 재귀 탐색을 시작할 데이터
두번째 Recursive Query : 이전 결과로 이용해 다음 데이터를 계속 탐색
더 이상 데이터가 없으면 종료

*/

# employee 테이블을 사용한 재귀 CTE예
-- 대표부터 모든 하위 직원 조회하기
with recursive empTree as (
	-- 시작점 : 최상위 직원
    select empNo, empName, job, managerNo, 1 as level
		from employee
        where managerNo is null
       
	union all
	-- 하위 직원 반복 검색
    select E.empNo, E.empName, E.job, E.managerNo, T.level + 1
		from employee E
		inner join empTree T
		on E.managerNo = T.empNo
)

select * from empTree;

/* 재귀가 수행되는 과정
1단계: Anchor Query -> 김대표 level=1
2단계: 김대표의 사원번호 1001을 managerNo로 가지고 있는 직원 탐색 ->
        이부장 : level=2, 박부장 : level=2
3단계: 이부장, 박부장의 부하직원 탐색
        이부장 -> 최과장 level=3
        박부장 -> 윤과장 level=3
4단계 : 최과장, 윤과장의 부하직원 탐색
		 최과장 -> 정대리, 강사원 level = 4
         윤과장 -> 한사원 level = 4
5단계 : 더 이상 하위 직원이 없으므로 재귀가 종료


*/
with recursive empTree as (
	-- 시작점 : 최상위 직원
    select empNo, empName, job, managerNo, 1 as level, cast(empName as char(200)) as path
		from employee
		where managerNo is null
       
	union all
	-- 하위 직원 반복 검색
    select E.empNo, E.empName, E.job, E.managerNo, T.level + 1, concat(T.path, '>', E.empName) as path
		from employee E
		inner join empTree T
		on E.managerNo = T.empNo
)

select * from empTree;

-- 특정 관리자의 모든부하직원 조회하기

with recursive subEmpTree as (
	-- 시작점 : 최상위 직원
    select empNo, empName, job, managerNo, 0 as level
		from employee
		where empName = '이부장'
       
	union all
	-- 하위 직원 반복 검색
    select E.empNo, E.empName, E.job, E.managerNo, S.level + 1
		from employee E
		inner join subEmpTree S
		on E.managerNo = S.empNo
)
select * from subEmpTree;


/*
12:17:43	select book.publisher, avg(bookprice)  from bookdb.book B   
  group by B.pubNo LIMIT 0, 5000	
  Error Code: 1054. Unknown column 'book.publisher' in 'field list'	0.000 sec

12:19:23	select book.pubNo, avg(book.bookprice)  from bookdb.book B    
 group by book.pubNo LIMIT 0, 5000	
 Error Code: 1054. Unknown column 'book.pubNo' in 'field list'	0.000 sec
*/


/*
11:49:42	with loc_dpt (locNo, locName, dptNo, dptName) as (  select locNo, locName, dptNo, dptName 
 from location         cross join department )	
 Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds 
 to your MySQL server version for the right syntax to use near '' at line 7	0.000 sec


14:37:26	select empNo, empName, job, managerNo, T.level + 1   from employee E   
      inner join empTree T         
      on E.managerNo = T.empNo ) select * from emp Tree	
      Error Code: 1064. You have an error in your SQL syntax; 
      check the manual that corresponds to your MySQL server version for the right syntax
      to use near ') select * from emp Tree' at line 5	0.000 sec

14:54:37	with recursive subEmpTree as (  -- 시작점 : 최상위 직원  
   select empNo, empName, job, managerNo, 0 as level   from employee   where empName = '이부장'      
   union all  -- 하위 직원 반복 검색     select E.empNo, E.empName, E.job, E.managerNo, S.level + 1  
   from employee E   inner join subEmployee S   on E.managerNo = S.empNo ) select * from subEmpTree	
   Error Code: 1146. Table 'exdb.subemployee' doesn't exist	0.000 sec

*/







































