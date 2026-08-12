/*
DML(4) : Select문
- 테이블 조회
	: 조건에 맞는 행에서 지정된 컬럼을 조회
		(그룹별 연산, 정렬)
        
- 형식
SELECT [ALL | DISTINCT] 열이름 리스트		=> 검색할 열 기술
	FROM 테이블명alter					=> 검색할 테이블명 기술
	[WHERE 검색조건(들)]				=> 질의 결과에 포함될 행이 만족해야할 조건'들'
	[GROUP BY 열이름]					=> 그룹질의
										특정 열로 그룹화한 후 각 그룹에 대해 한 행씩 질의 결과 생성
	[HAVING 검색조건(들)]				=> Group by 절에 의해 구성된 그룹들에 대해 적용할 조건
	[ORDER BY 열이름 [ASC┃DESC]			=> 특정 열의 값을 기준으로 질의 결과를 정렬
										ASC : 오름차순, DESC : 내림차순

SELECT	DISTINCT	FROM	WHERE	GROUP BY	HAVING	ORDER BY
   5	   6		  1		   2	   3		  4		   7
*/

# 예제 데이터베이스 bookdb 
# book, bookclient, booksale 테이블의 모든 행들을 제거 후 table import with wizard를 이용해 다시 데이터를 추가

use bookdb;
delete from booksale;
delete from bookclient;
delete from book;

# 데이터 임포트


select * from information_schema.table_constraints
	where constraint_schema='bookdb';
    
alter table bookdb.book drop constraint FK_book_pubNo;
alter table bookdb.booksale drop constraint FK_bookSale_bookNo;
alter table bookdb.booksale drop constraint FK_bookSale_clintNo;

alter table book add
	constraint FK_book_pubNo foreign key(pubNo) references publisher(pubNo);
alter table bookSale add
	constraint FK_bookSale_clintNo foreign key(clientNo) references bookClient(clientNo);
alter table bookSale add
	constraint FK_bookSale_bookNo foreign key(bookNo) references book(bookNo);
    

#데이터 임포트 후 조회로 확인
/*
	select [all|distinct] 컬럼명,컬럼명, ... from 테이블명 whrer 조건

*/

select * from bookdb.book;
select * from bookdb.booksale;
select * from bookdb.bookclient;

# select [ALL| DISTINCT] 문
#	: ALL -> 중복출력(모든 레코드 출력), (기본값)
#	: DISTINCT -> 중복된 레코드(행)을 한번만 출력
# 책 가격이 3만원 이상인 도서 조회
select * from bookdb.book where bookprice >= 30000;

# 책 가격이 3민원 이상인 도서의 도서명, 가격, 저자 조회
select bookname, bookprice, bookAuthor
	from bookdb.book
    where bookprice >= 30000;

# select DISTINCT문
# 책 가격이 3만원 이상인 도서의 가격 조회 => 중복데이터는 한 번만 출력
select distinct bookprice
	from bookdb.book
    where bookprice >= 30000;

# 도서의 저자들 조회
select bookAuthor
	from bookdb.book;
select distinct bookAuthor
	from bookdb.book;    
/*
# where절 : 조건에 따른 행 조회alter

where 조건식에 사용되는 연산자들
1) 비교 : >, <, >=, <=, =, !=
    price >= 10000
2) 논리 : and, or
    price >= 10000 and price <= 30000
3) 범위 : between 시작 and 끝
    price between 10000 and 30000
4) 리스트에 포함여부(멤버) : in, not in
    price in [10000, 20000, 30000]
    pubName in ['좋은출판사', '서울출판', '종로출판사']
5) NULL : is null, is not null
	clientHobby is null

6) 패턴매칭 : LIKE 문자열서식 (%, __)
	% : all
    _ : 단일문자(문자하나)
    bookName like '파이썬%'		=> '파이썬' 문자열로 시작하는 문자열
    bookName like '%파이썬'		=> '파이썬' 문자열로 끝나는 문자열
    bookName like '%파이썬%'	=> '파이썬' 문자열이 들어있는 문자열
    bookName like '%'			=> 0개 이상의 문자를 가진 문자열
    bookName like '_'		=> 1개의 문자로 구성된 문자열
    bookName like '____'	=> 4개의 문자로 구성된 문자열


*/








