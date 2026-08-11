/*
DDL(DataDefinition Language) 데이터 정의어

1. Create : 데이터베이스(=스키마), 테이블, 뷰, 인덱스 등의 생성
1) 데이터베이스(=스키마) 생성
create schema 데이터베이스명 [default character set uef8mb4];
=create database 데이터베이스명 [default character set uef8mb4];

2) 테이블 생성
create tabel 테이블명 (
	열이름1 데이터타입 [제약조건(PK, NN, FZ 등)],
    열이름2 데이터타입 [제약조건(PK, NN, FZ 등)],
    열이름3 데이터타입 [제약조건(PK, NN, FZ 등)],
    열이름4 데이터타입 [제약조건(PK, NN, FZ 등)],
    ...,
    열이름n 데이터타입 [제약조건(PK, NN, FZ 등)],
    constraint 제약조건명 primary key (칼럼이름),
    constraint 제약조건명 foreign key 컬럼 이름 reference 테이블명(칼럼이름),
    
);
*기본키를 복합키로 사용할 경우 반드시 constraint 문에서 정의할 것

[제약조건 종류]
not null	: 빈값 허용하지 않음	
primary key	: 기본키로 설정
foreign key 칼럼이름 references 테이블명(칼럼이름)	: 외래키 설정	
unique		: 중복값 허용하지 않음
default 기본값	: 기본값 설정
check 체크조건	: 특정 내용이 제약조건(값, 범위 등) 
on delete 또는 on update : 참조되는 테이블의 행 삭제/갱신 시

*/
/*
단축키
ctrl + Enter 현재 선택한 줄만 실행
ctrl + Shift + Enter : 선택한 여러 줄 실행
ctrl + / : 주석 결정/해지  (커서를 문장의 젓먼째 컬럼에 두어야 함)

*/
-- create schema testdb default Character set utf8mb4;
-- drop database testdb;

# shopdb 생성 -> 상품테이블 생성
create database shopdb default character set utf8mb4;
use shopdb;




# 기본키 설정(제약조건)
#	기본키 컬럼은 중복불가, 변경불가
create table product(
	prdNo varchar(10) not null primary key,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30)
);

create table product2(
	prdNo varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
	primary key(prdNo)
);

create table product3(
	prdNo varchar(10) not null,
    prdName varchar(30) not null,
    prdPrice int,
    prdCompany varchar(30),
	constraint PK_product_prdNo primary key(prdNo)
);

create table publisher(
	pubNo varchar(10) not null primary key,
    pubName varchar(30) not null
);
# 왜래키 : 다른 테이블의 기본키를 갖는 컬럼, 두 테이블 연결
# 	기본 설정은 Restrict 로 설정되어 레코드 변경이나 삭제 불가
create table book (
	bookNo varchar(10) not null primary key,
    bookName varchar(30) not null,
    bookPrice int default 10000 check(bookprice>1000),
    bookDate date,
    pubNo varchar(10) not null,
    constraint FK_book_publisher foreign key(pubNo) references publisher(pubNo)
);

