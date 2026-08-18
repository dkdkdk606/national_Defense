## 서브쿼리(SubQuery)
/*
- 하위질의(부속질의)
- 하나의 SQL문 안에 포함된 또 다른 select문
  : 하나의 SQL문 안에 SQL 문이 중첩(nested)되어 있는 구조
- 어떤 SQL의 실행결과를 다른 SQL에서 다시 사용하는 방법
  : 질의를 1차 수행한 다음 반환 결과를 기초로 다음 질의를 수행
- 다른 테이블에서 가져온 데이터로 현재 테이블에 있는 정보를 찾거나 가공할 때

- [기본형식]
    select 컬럼
        from 테이블
        where 컬럼연산자 (
            select 컬럼 from 테이블);

1) 단일 행 서브쿼리
- 서브쿼리의 결과 값이 단일 행(튜플)인 경우
- '='연산자 사용
    main query
        where 조건절 = (sub query)
        
2) 다중 행 서브쿼리
- 서브쿼리의 결과 같이 여러 행인 경우
- 'in', 'any', 'all', 'exists' 연산자 사용

# 서브쿼리 연산자
- where 절에서 사용
- 데이터를 선택하는 조건이나 술어 같이 사용
- 연산자 종류 :
    비교 : =, !=, >, >=, <, <=        		=> 단일행으로 반환
    집합 : in, not in               		=> 다중행으로 반환
    한정 : all(모두), any(최소한하나라도)   => 다중행으로 반환
    존재 : exists, not exists				=> 다중행으로 반환
*/

# 1. 단일행 서브쿼리 : 비교(=, !=, >, >=, <, <= )
-- bookdb에서 고객 호날두의 주문일자와 주문량 조회

select BC.clientName, BS.bsDate, bsQty
	from bookdb.booksale BS
    join bookdb.bookClient BC
    on BC.clientNo = BS.clientNo
    where BC.clientName = '호날두';

select BS.bsDate, BS.bsQty
	from bookdb.booksale BS, bookdb.bookclient BC
    where BS.clientNo = BC.clientNo and BC.clientName = '호날두';

-- 서브쿼리로
select BS.bsDate, BS.bsQty
    from bookshopdb.booksale BS
    where BS.clientNo = (select BC.clientNo
                            from bookshopdb.bookclient BC
                            where BC.clientName = '호날두');

-- 고객 호날두의 총 주문량 조회
select sum(BS.bsQty) as '총주문량'
	from bookdb.booksale BS
    where BS.clientNo = (select BC.clientNo
							from bookdb.bookclient BC
							where BC.clientName ='호날두');




-- 가장 비싼 도서의 가격과 도서명 조회
select B.bookprice, B.bookName
	from bookdb.book B
    where bookprice = ( select max(B.bookprice) from bookdb.book B);

select B.bookprice as '도서가격',
		GROUP_CONCAT(B.bookName) as '도서목록'
	from bookdb.book B
    group by B.bookprice
    order by B.bookprice desc
    limit 1;


/*
select B.bookprice, B.bookName
	from bookdb.book B
    order by bookprice desc
    limit 1;
*/


-- 평균도서가격 이상인 도서들의 도서명과 가격 조회
select B.bookprice, B.bookName
	from bookdb.book B
    where B.bookprice >= (select avg(B.bookprice)
							from bookdb.book B );
#2. 다중행 서브쿼리
-- 도서를 구매한 적 있는 고객명 조회
select clientNo, clientName
	from bookdb.bookclient BC
    where BC.clientNo in (select distinct clientNo from bookdb.booksale);

select distinct BC.clientName
	from bookdb.bookclient BC
    right join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

-- 도서를 구매한적 없는 고객명 조회
select clientNo, clientName
	from bookdb.bookclient BC
    where BC.clientNo not in (select distinct clientNo from bookdb.booksale);

select distinct BC.clientName
	from bookdb.bookclient BC
    left join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
    where BS.bsNo is null;
    

# 2. 다중행 서브쿼리(2) : 한정(any, all)
-- 한정은 관계연산자 뒤에 위치
-- any : 검색조건이 서브쿼리의 결과 중 하나 이상 만족하면 참
-- all : 검색조건이 서브쿼리의 결과 모든 값에 만족하면 참

-- 고객번호가 2인 고객이 주문한 도서의 최고 주문수량보다
-- 더 많은 도서를 구입한 고객의 고객번호, 주문번호, 주문수량 조회

select BS.clientNo, bs.bsNo, bs.bsqty
	from bookdb.booksale BS
    where BS.bsQty > all(select BS.bsQty
							from bookdb.booksale BS
							where BS.clientNo = '2' );

select BS.clientNo, bs.bsNo, bs.bsqty
	from bookdb.booksale BS
    where BS.bsQty > any(select BS.bsQty
							from bookdb.booksale BS
							where BS.clientNo = '2' );

-- 고객번호 2보다 더 많이 주문한 고객 정보 조회
select BS.clientNo, bs.bsNo, bs.bsqty
	from bookdb.booksale BS
    where BS.bsQty > any(select BS.bsQty
							from bookdb.booksale BS
							where BS.clientNo = '2' )
		and BS.clientNo !='2';

# [서브쿼리 유형]
/*
1. 스칼라(scalar)서브 쿼리
 - select 절에 서브쿼리 사용'
 - 결과값을 단일 컬럼의 스칼라 값으로 전환
 - 스칼라 값이 들어갈 수 있는 모든 곳에 사용 가능


2. 인라인(inline) 뷰
- from 절에서 사용
- 테이블 명 대신 인라인 뷰 부속질의를 사용(가상테이블)
- 서브쿼리 결과 반환되는 데이터는 다중 행, 다중 열이라도 상관 없음 
- 가상 뷰 형태로 제공 
- 개발 중에 뷰가 필요한 모든 경우 뷰를 생성하면 관리할 양이 너무 많아
		트랜잭션 관리나 성능상 문제 발생 가능성이 매우 높은 경우 사용


3. 중첩(nested) 서브쿼리
- where 절에 서브쿼리를 사용 : 결과를 한정하기 위해 사용
- 부속질의 또는 하위질의라고 부름
- 한 질의문 안에 다른 질의문이 중첩(nested)
- 다른 테이블에서 가져온 데이터로 현재 테이블에 있는 정보를 찾거나 가공하기 위해 사용

*/

-- 스칼라 서브쿼리 예 
select BS.clientNo as '고객번호',
    (select clientName from bookdb.bookclient BC
        where BC.clientNo = BS.clientNo) as '고객명',
    sum(bsQty) as '총주문수량'
from bookdb.booksale BS
group by BS.clientNo;

-- 인라인 뷰 서브쿼리 예.
-- 도서가격이 25000원 이상인 도서에 대해 도서별로 도서명, 가격, 총판매수량, 총판매액을 조회하되 총판매액 내림차순으로 출력

select bookName, bookPrice, sum(bsQty) as '총판매수량', sum(bookPrice * bsQty) as '총판매액'
    from (select bookNo, bookName, bookPrice
        from bookdb.book
        where bookPrice >= 25000) B,
        bookdb.booksale BS
	where B.bookNo = BS.bookNo
    group by B.bookNo;

-- 중첩 서브쿼리 예
select sum(BS.bsQty)
	from bookdb.booksale BS
    where BS.clientNo = (select clientNo from bookdb.bookclient BC
								where BC.clientName = '호동생');












/*
15:25:20	select BS.bsDate, BS.bsQty  from bookdb.booksale BS, bookdb.bookclient BC  
   where BS.clientNo = BC.clientNo and BC.clientName = '호날두;	
   Error Code: 1064. You have an error in your SQL syntax; 
   check the manual that corresponds to your MySQL server version for the right syntax to use near
   ''호날두' at line 3	0.000 sec
15:30:13	select sum(BS.bsQty) as '총주문량'  from bookdb.booksale BS   
  where BS.clientNo = (select        from bookdb.bookclient BC      
  where BC.clientName ='호날두' )	
  Error Code: 1064. You have an error in your SQL syntax; 
  check the manual that corresponds to your MySQL server version for the right syntax to use 
  near 'from bookdb.bookclient BC        where BC.clientName ='호날두' )' at line 4	0.000 sec
15:37:36	select B.bookprice, B.bookName  from bookdb.book B   
  where B.bookprise >= (select avg(B.bookprice)        
  from bookdb.book B ) LIMIT 0, 5000	
  Error Code: 1054. Unknown column 'B.bookprise' in 'where clause'	0.000 sec

15:41:56	select B.bookName  from bookdb.book B     group by B.bookprice LIMIT 0, 5000	
Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY clause and
 contains nonaggregated column 'bookdb.B.bookName' which is
 not functionally dependent on columns in GROUP BY clause;
 this is incompatible with sql_mode=only_full_group_by	0.000 sec



*/


































