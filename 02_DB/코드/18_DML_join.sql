/*
조인(join)
- 두 테이블에 대한 공통키(컬럼)를 기준으로 하나의 행(튜플)으로 합침
- 조인 종류
	- 내부조인(inner join)
    - 외부조인(outer join)
*/
use bookdb;

# 내부조인(inner join)
/*
- 공통 컬럼(기본키=외래키)의 값이 동일한 튜플(레코드)만 반환
[형식]
select 열리스트
    from 테이블1, 테이블2
    where 테이블1.키 = 테이블2.키;
    
# 조인문 표기방식(2): join ~ on 을 사용
select 열리스트
    from 테이블1 (inner) join 테이블2
    on 조인조건(기본케=외래키);
*/

# 조인문 표현방식(1) : where 조건을 사용 
-- 도서주문한 고객 이름과 주문량 출력

select * from booksale;

# booksale 테이블에는 고객이름이 없으므로 고객정보를 갖고 있는 bookclient 테이블과의 조인이 필요

select booksale.clientNo, clientName, bsQty
    from booksale, bookclient
    where booksale.clientNo= bookclient.clientNo;


# select문에서 사용하는 컬럼명 앞에 해당하는 테이블명을 명시적으로 지정함으로써
# 서버에 정확한 위치를 알려주어 성능 향상
select booksale.clientNo, bookclient.clientName, booksale.bsQty
    from booksale, bookclient
    where booksale.clientNo= bookclient.clientNo;

/*
- 스키마명.테이블명.컬럼명 => 너무길다
- from 문에서 스키마명.테이블명을  지정하여 사용
- 별칭을 select와 where절에서 사용함
*/

select bookdb.booksale.clientNo, bookdb.bookclient.clientName, bookdb.booksale.bsQty
    from bookdb.booksale, bookdb.bookclient
    where bookdb.booksale.clientNo= bookdb.bookclient.clientNo;
#-> 너무 길다.... from 문 부터 코드가 실행된다는것 기억하기

select BS.clientNo, BC.clientName, BS.bsQty
        from bookdb.booksale BS, bookdb.bookclient BC
		where BS.clientNo= BC.clientNo;

# 조인문 표기방식(2): join ~ on 을 사용 (명시적)

/*
    from 테이블A
    join 테이블B
    on 테이블A.컬럼c = 테이블B.컬럼c
*/
select BC.clientNo, BC.clientName, BS.bsQty
    from bookdb.bookclient BC
    join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

select *
    from bookdb.bookclient BC
    join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

# 조인문 표기방식(3): inner join ~ on 을 사용 (명시적)
/*
    from 테이블A
    inner join 테이블B
    on 테이블A.컬럼c = 테이블B.컬럼c
*/
select BC.clientNo, BC.clientName, BS.bsQty
    from bookdb.bookclient BC
    inner join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

select *
    from bookdb.bookclient BC
    inner join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;
-- -> 공통 컬럼이 두 번 출력됨. 필요한 컬럼만 지정하여 출력할 것


-- 도서 주문한 고객번호와 고객이름 조회
select BC.clientNo, BC.clientName
    from bookdb.bookclient BC
    inner join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;
-- -> 고객번호와 이름이 중복되어 출력

# 내부조인 결과 정렬
-- 이름순으로 정렬
select distinct BC.clientNo, BC.clientName
    from bookshopdb.bookclient BC
    inner join bookshopdb.booksale BS
    on BC.clientNo = BS.clientNo
    order by BC.clientName;


# 주문한 도서의 고객명과 도서명 출력
-- -> 테이블 3개 필요
select BC.clientName, BO.bookName
    from bookdb.bookclient BC, bookdb.booksale BS, bookdb.book BO
    where BC.clientNo = BS.clientNo and BO.bookNo = BS.bookNo;

# join 으로 표현
select BC.clientName, BO.bookName
    from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo;

-- 주문한 고객번호와 고객이름, 도서명과 도서 가격 조회
select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo;

-- 주문한 고객정보(번호와 이름), 도서정보(도서명, 가격), 주문정보(주문번호, 주문일자, 주문량) 조회
select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice, BS.bsNo, BS.bsDate, BS.bsQty
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo;

-- 주문한 고객정보(번호와 이름), 도서정보(도서명, 가격), 주문정보(주문번호, 주문일자, 주문량, 주문금액) 조회
select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice, BS.bsNo, BS.bsDate, BS.bsQty, BO.bookprice
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo;
        
select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice, BS.bsNo, BS.bsDate, BS.bsQty, BS.bsQty*BO.bookprice as 'totalprice'
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo;
        
-- 주문한 고객정보(번호와 이름), 도서정보(도서명, 가격), 주문정보(주문번호, 주문일자, 주문량, 주문금액)를 최근주문일수 기준으로 조회
select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice, BS.bsNo, BS.bsDate, BS.bsQty, BO.bookprice
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo
        order by BS.bsDate desc;

select BC.clientNo, BC.clientName, BO.bookName, BO.bookPrice, BS.bsNo, BS.bsDate, BS.bsQty, BS.bsQty*BO.bookprice as 'totalprice'
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo
        order by BS.bsDate desc;

-- 2019년 이후 주문한 도서에 대한 주문일자, 고객명, 도서명, 도서가격, 주문수량, 주문금액 조회
select BS.bsDate, BC.clientName, BO.bookName, BO.bookprice, BS.bsQty, BO.bookprice
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo
        where BS.bsdate > '2019-01-01';

select BS.bsDate, BC.clientName, BO.bookName, BO.bookprice, BS.bsQty, BS.bsQty*BO.bookprice as 'totalprice'
	from bookdb.booksale BS
		inner join bookdb.bookclient BC on BC.clientNo = BS.clientNo
        inner join bookdb.book BO on BO.bookNo = BS.bookNo
        where BS.bsdate > '2019-01-01';

/*
10:03:46	select clientNo, clientName, bsQty  
   from booksale, bookclient   
   where booksale.clientNo= bookclient.clientNo LIMIT 0, 5000
   Error Code: 1052. Column 'clientNo' in field list is ambiguous	0.000 sec
*/

# 2. 외부조인(outer join)
/*
두 테이블의 공통컬럼으로 결합하되, 공통컬럼의 값이 없는 튜플도 반환
- 좌측 외부조인(left outer join) : 왼쪽 테이블의 모든 정보 유지
	select 열리스트
		from 테이블1
        left [outer] join 테이블2
        on 조인조건(보통 기본키=외래키)

- 우측 외부조인(right outer join) : 오른쪽 테이블의 모든 정보 유지
	select 열리스트
		from 테이블1
        right [outer] join 테이블2
        on 조인조건(보통 기본키=외래키)

- 완전 외부조인(left outer join) : 양쪽 테이블의 모든 정보 유지
	좌측외부조인과 우측외부조인 결과 결합(union)하여 구현

*/

# 좌측외부조인
select *
	from bookdb.bookclient BC
    left outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

-- 고객 중 한번도 구매한 적이 없는 고객(고객번호, 이름) 조회
select BC.clientNo, BC.clientName
	from bookdb.bookclient BC
    left outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
    where BS.clientNo is null
    order by BS.clientNo;
    
-- 한번도 판매된적 없는 도서 정보 조회
select BO.bookNo, BO.bookName
	from bookdb.book BO
    left outer join bookdb.booksale BS
    on BS.bookNo = BO.bookNo
    where BS.bookNo is null
    order by BS.bookNo;



# 우측외부조인

select *
	from bookdb.bookclient BC
    right outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo;

-- 한번이라도 주문한 적 있는 고객의 번호와 이름 조회, 중복된 경우 한번만 출력
# BS에 있으면 일단 주문은 한 친구 라는 논리
select distinct BC.clientNo, BC.clientName
	from bookdb.bookclient BC
    right outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
    order by BC.clientNo;
    
#완전외부조인( full outer join)
-- MySQL에서는 완전 외부조인에 대한 명령어가 따로 없고, 좌측 외부조인과 우측외부조인결과 union

select *
	from bookdb.bookclient BC
    left outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
union
select *
	from bookdb.bookclient BC
    right outer join bookdb.booksale BS
    on BC.clientNo = BS.clientNo







/*
11:27:17	select distinct BC.clientNo, BC.clientName  from bookdb.bookclient BC  
   right outer join bookdb.booksale BS     on BC.clientNo = BS.clientNo  
   order by BS.clientNo LIMIT 0, 5000	
   Error Code: 3065. Expression #1 of ORDER BY clause is not in SELECT list, references column 'bookdb.BS.clientNo' which is not in SELECT list; this is incompatible with DISTINCT	0.000 sec


*/










