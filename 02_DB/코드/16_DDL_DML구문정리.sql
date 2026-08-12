/*
1. DDL(Data Definition Language)

: CREATE, ALTER, DROP
	- 데이터베이스(스키마), 테이블, 뷰, 인덱스, 사용자, ... 등
       DB개체를 생성/수정/삭제
	- 직접 데이터베이스 테이블에 영향이 미치므로 
      DDL 명령어를 실행하는 순간 처리 작업이 즉시 완료 (auto commit)
	- 작업 취소(rollback)나 완료(commit)을 시킬 수 없음

#1. create문
 : 데이터베이스(스키마), 테이블, 뷰, 인덱스, 사용자계정 등 생성(정의)
	create schema  
    create database
    create table
    create view
    create index
    create user
    
 1) 데이터베이스(스키마) 생성
	create schema 데이터베이스명 [default charater set utf8mb4];
    create database 데이터베이스명 [default charater set utf8mb4];

 2) 테이블 생성
	- 속성(필드, 컬럼)에 대한 이름과 데이터유형, 제약조건등을 정의
    - 형식
    create table 테이블명 (
		열이름 데이터타입 [제약조건],
        열이름 데이터타입 [제약조건],
        열이름 데이터타입 [제약조건],
		contraint 제약조건명 primary key (컬럼이름, ),
        contraint 제약조건명 foreign key 컬럼이름 references 테이블명(컬럼이름),
    );    
    [제약조건] : 
		not null		: 빈값 허용하지 않음
        unique			: 중복값 허용하지 않음
        default 기본값	: 기본값 설정
        primary key		: 기본키 설정
		foreign key 컬럼이름 references 테이블명(컬럼이름) : 외래키 설정
        check 체크조건	: 특정 내용의 제약조건 (값 범위 등)
        on delete 또는 on update :참조되는 테이블의 행 삭제/갱신 시 옵션

 ** 기본키를 복합키를 사용할 경우 반드시  constraint 문에서 정의할 것

#2. alter문

- 테이블 수정
- 테이블에 대한 정의 변경
- 새로운 컬럼 추가, 특정 컬럼의 기본값 변경, 특정 컬럼 삭제 등
- 형식
alter table 테이블명 
	add				: 컬럼 추가
	rename cloumn	: 컬럼 이름 변경
    modify			: 컬럼 데이터형식 변경
    change			: 컬럼이름과 데이터형식 함께 변경
    drop column		: 컬럼 삭제
    drop			: 여러 개 컬럼 삭제
    drop primary key: 기본키 삭제
    drop constraint	: 제약조건 삭제
    
alter table old테이블명 rename new테이블명;
rename table old테이블명 to new테이블명;
rename table old테이블명1 to new테이블명1,
			 old테이블명2 to new테이블명2,
             ... ;	

#3. drop문 :
 -- 데이터베이스의 각종 객체들(DB, table, view,...) 자체를 삭제
	: 구조와 내용(data) 모두 제거
	drop database 데이터베이스명;
    drop schema 데이터베이스명;
    drop table [데이터베이스명.]테이블명;
    drop view 뷰이름;
	drop user 사용자계정정보;

---------------------------------

2. DML : CRUD
	C : INSERT INTO (컬럼명리스트) VALUES (값리스트);
    R : SELECT [all | distinct] 컬럼들 
			FROM 테이블명
            WHERE 조건절 
			GROUP BY 그룹화할컬럼들
            HAVING 그룹화결과필터링조건
			ORDER BY 정렬기준컬럼들
            limit
            with rollup

	U : UPDATE 테이블 SET 컬럼명=변경값 WHERE 조건
    D : DELETE FROM 테이블 WHRER 조건
	- 데이터를 삽입/조회/수정/삭제를 위한 조작어
    - 테이블의 행을 대상으로
    - 조작 작업이 메모리 버퍼에서 수행되어 
       실시간으로 테이블에 영향을 미치지 않음
	- 실수가 있는 경우 작업 취소 가능 -> ROLLBACK : 트랜잭션
	- DML 명령어가 실제 테이블에 반영되기 위해서는 COMMIT 명령어 수행해야 함

#1. 데이터 삽입(insert)
	insert into 테이블명 (컬럼명1, 컬럼명2,...) values (값1, 값2, ...);
	insert into 테이블명 values (값1, 값2, ...);
		--> 테이블의 모든 컬럼에 대한 값을 지정하여 삽입
	insert into 테이블명 (컬럼명1, 컬럼명2,...)
			values (값1, 값2, ...),
					(값1, 값2, ...),
                    ...,
                    (값1, 값2, ...);

#2. 데이터 갱신(update)
  - 특정 컬럼(열)의 값을 수정하는 명령어
  - 조건에 맞는 행을 찾아서 열의 값 수정
  - 형식 : update 테이블명 set 컬럼명=변경값 where 조건;
    
#3. 데이터 삭제(delete)
  - 테이블에 있는 기존 행(레코드)을 삭제하는 명령어
  - 형식 : delete from 테이블명 where 조건;

#4. 데이터 조회(select)
  - 테이블의 데이터를 조회하는 명령어
  - 형식 : 
  select [all|distinct] 컬럼(열)리스트 (*)
    from 테이블명
    [where 검색조건(들)]
    [group by 열이름]
    [having 검색조건(들)]
    [order by 열이름 [asc|desc]]
  
  select [all|distinct] 컬럼(열)리스트 (*) : 검색할 열리스트 지정
  where 검색조건(들) : 질의 결과에 포함될 행들이 만족할 조건 기술
  group by 열이름 : 그룹 질의 ->특정 컬럼으로 그룹화한 수 각 그룹에 대해
					한 행씩 질의 결과 생성
  having 검색조건(들) : group by 절에 의해 구성된 그룹들에 대해 적용할 조건
  order by 열이름 [asc|desc] : 열이름의 값을 기준으로 결과를 정렬
				asc : 오름차순,  desc : 내림차순
                
# select문 실행순서
select  distinct  from   where  group by  having  order by
  (5) 		(6)    (1)    (2)       (3)     (4)      (7)

# 예. 
	select * from book;
	select bookName, bookPrice from book;
	select bookName, bookPrice from book where bookPrice>=30000;
	select distinct bookName, bookPrice from book where bookPrice>=30000;
  

# where 조건식에 사용되는 연산자들

1) 비교 : >, <, >=, <=, ==, !=
	price >= 10000
    
2) 논리 : and, or
	price >= 10000 and price <=20000
    
3) 범위 : between 시작 and 끝
	price between 10000 and 20000
    
4) 리스트에 포함여부(멤버) : in, not in
	price in (10000, 20000, 30000)
    pubName in ('삼성출판사', '금성출판사', '화성출판사')
    fruits not in ('사과','배','수박')
    
5) NULL : is null, is not null
	price is null
    
6) 패턴매칭 : like 문자열서식 (%, _)
	(문자열의 일부가 위치하는 데이터 검색)
    % : all
    _ : 단일문자(문자하나)
    ___ : 3개 문자로 구성된 문자열
    
    bookName like '%파이썬%'  => '파이썬' 문자열이 들어가있는 모든 문자열
    bookName like '파이썬%' => '파이썬' 문자열로 시작하는 문자열
    bookName like '%파이썬' => '파이썬' 문자열로 끝나는 문자열
    bookName like '%' => 0개 이상의 문자를 가진 문자열
    bookName like '_' => 단일문자
    bookName like '____' => 4개의 문자로 구성된 문자열
  
  
# 집계함수
1) count() : 조건에 맞는 행(row)의 개수 계산

   count(*) -> NULL 포함한 전체 행
   count(컬럼) -> NULL 제외한 행수
   count(distinct 컬럼) -> 중복 제거 후 개수
   
   count() as 별칭

2) sum() : 특정 숫자 컬럼의 총합 계산
   sum(숫자컬럼)
   sum(distinct 숫자컬럼)
   group by와 함께 사용하면 그룹별 합계 계산
	예. select customerNo, sum(order) as total_order
			from bookSale	
			group by customerNo;

3) avg() : NULL 값 제외한 평균값 계산
   avg(숫자컬럼)
   avg(distinct 숫자컬럼)
	group by와 함께 사용하여 그룹별 평균
    
4) min(), max() : 최소, 최대값
	group by와 함께 사용
    
5) group_concat() : 여러 행의 문자열 하나의 문자열로 결합
	group_concat(컬럼명)
	select
		customerNo,
        group_concat(bookNo) as product_order
	from bookSale
    group by customerNo;
    
    결과]
    customerNo	 product_order
    ---------------------------
    1            1001, 1010
    3 			 1, 1002, 3
    
6) variance() / var_pop() / var_samp() : 분산

7) stddev() / stddev_pop() / stddev_samp() : 표준편차


# 그룹별 집계 : select ~ from ~ group by ~ having ~

- 그룹별 질의에 대한 결과 생성
- 형식 :
	select 집약키컬럼, 집계함수(컬럼),...
		from 테이블명
        group by 집약키컬럼
        [having 검색(필터링)조건]
- 집약키 : group by에서 사용하는 컬럼
			집약키는 여러개 지정 가능
- 집약키에 따라 그룹화한 후 그룹별로 집계함수나 조건에 따른 질의결과 생성
- 주의: select 구에는 1개의 값을 반환하는 상수, 
		group by에서 사용한 집약키 컬럼, 집계함수만 나올 수 있음
- having 검색(필터링)조건은 반드시 group by 뒤에 와야 함, order by 뒤에 오면 안됨
        
- 그룹별 연산 단계 :
	그룹별 데이터 분리(split)
    -> 집계함수나 그룹별 연산을 적용(apply)
    -> 그룹별 연산 결과를 통합 (merge)
   
   
   
3.트랜잭션(transaction)
    - DBMS에서 데이터를 다루는 논리적인 작업 단위
    - 회복 및 병행 수행 시 처리되는 작업의 논리적 단위 사용
    - 하나의 트랜잭션은 정상적으로 종료될 경우 COMMIT 연산이 수행되고,
      비정상적으로 종료될 경우 ROLLBACK 연산 수행하여 작업 취소

*/


