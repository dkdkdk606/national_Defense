/*
Drop문
- 데이터베이스, 테이블, 뷰, 인덱스, ... 삭제
- 테이블의 구조와 데이터 모두 삭제 

# 데이터베이스 삭제
drop schema 데이터베이스(스키마) 이름;
drop database 데이터베이스(스키마) 이름;

# 테이블 삭제
drop table 테이블명;
drop table 테이블명1, 테이블명2, ...;

*/


drop schema testdb3;

create schema testdb3;
use testdb3;
create table testdb3.board(
	boardId int auto_increment not null primary key,
    boardTitle varchar(30) not null,
    boardAuthor varchar(30),
    boardCountent varchar(200) null
);

create table testdb3.board2(
	boardId int auto_increment not null primary key,
    boardTitle varchar(30) not null,
    boardAuthor varchar(30),
    boardCountent varchar(200) null
);

create table testdb3.board3(
	boardId int auto_increment not null primary key,
    boardTitle varchar(30) not null,
    boardAuthor varchar(30),
    boardCountent varchar(200) null
);
#use testdb3;
drop table if exists testdb3.board;

drop table testdb3.board2, testdb3.board3;

drop database if exists testdb3;


