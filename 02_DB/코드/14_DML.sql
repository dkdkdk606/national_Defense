/*
데이터 집계 :
- 최대, 최소, 합계, 평균, ...

집계함수 :
- SUM() : 합계
- AVG() : 평균
- COUNT() : 선택된 열의 행 수(null 값은 제외)
- COUNT(*) : 전체 행의 수
- MAX() : 최대값
- MIN() : 최소값

집계함수를 적는 곳은 정해져 있음
-> SELECT 구
-> HAVING 구
-> ORDER BY 구

집계함수는 1개의 값을 반환하는 것만 함께 적을 수 있다
- 상수, 집계함수, DISTINCT, 연산자 등
*/

# SUM() : 합계
-- 도서 테이블에서 총 재고 수량 계산해서 출력
-- 열이름 없이(수식이 열 이름이 됨) 총합만 출력
select sum(bookStock) from bookdb.book;
#	-> 집계 결과 테이블의 컬럼명은 sum(컬럼명)으로 저장

# 집계 결과 컬럼명 지정 -> 한글도 가능
select sum(bookStock) as 'sum of bookStock'
	from bookdb.book;

select sum(bookStock) as '총 재고량';

# 고객번호가 2인 고객이 주문한 도서의 총 주문수량 조회
select sum(bsQty) as '2번 고객 총 주문량' from booksale where clientNo=2 ;

select * from booksale;
# 최소 주문수량 조회
select min(bsQty) as '최소 주문량' from booksale;
select * from bookdb.booksale
	where bsQty = 9; 


# 최대 주문수량 조회
select max(bsQty) from booksale;
select * from bookdb.booksale
	where bsQty = 1; 

# 실험
-- select * from bookdb.booksale
-- 	where bsQty = (select min(bsQty) from bookdb.booksale); 
-- select * from booksale
-- 	where bsQty = (select max(bsQty) from booksale);

-- 평균 AVG()
# 평균주문량
select avg(bsqty) as '평균주문량'
	from bookdb.booksale;

-- 최소, 최대, 평균을 함께 출력
select min(bsQty), max(bsQty), avg(bsQTY)
    from bookdb.bookSale;

select min(bsQty) as '최저주문량',
		max(bsQty) as '최대주문량',
		avg(bsQTY) as '평균주문량'
    from bookdb.bookSale;

-- round() 함수 : 수치값 반올림
select min(bsQty) as '최저주문량',
    max(bsQty) as '최대주문량',
    round(avg(bsQTY)) as '평균주문량'
from bookshopdb.bookSale;

-- 총수 : COUNT()
select count(*) from bookdb.bookSale;
select count(*) from bookdb.bookClient;
select count(clientHobby) from bookdb.bookClient;
select count(bookNo) from bookdb.bookSale;
select count(distinct bookNo) from bookdb.bookSale;

# 문제
/*
-- 1. 고객 테이블에서 취미에 공백이 들어 있는 행의 총수 출력
select count(*) from bookdb.bookclient where clientHobby = '';
*/

select * from bookdb.bookclient ;

-- 1. 남성 고객의 총 수 출력
select count(*) as '남성 고객의 총 수' from bookdb.bookclient where clientGender = '남';

-- 2. 고객 테이블에서 취미에 null 들어 있는 행의 총수 출력
select count(*) as '취미에 null' from bookdb.bookclient where clientHobby is null;
    
select * from bookdb.book ;
-- 3. 도서 테이블에서 총도서 수 출력 
select sum(bookStock) as '총도서 수' from bookdb.book;

-- 4. 도서 테이블에서 가장 싼 도서가격, 가장비싼 도서가격, 평균가격 출력
select min(bookprice) as '싼 도서가격',
		max(bookprice) as '가장비싼 도서가격',
        round(avg(bookprice)) as '평균가격'
			from bookdb.book;



