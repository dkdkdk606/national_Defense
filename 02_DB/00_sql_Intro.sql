# 데이터베이스 선택
-- use world;

# 테이블 조회
-- select * from country;
select * from world.country;

# 데이터베이스 목록 조회
show databases;

# SQL(Structured Query Language
# 데이터 정의어(Data Definition Language:DDL)
#    : 스키마(데이터베이스), 테이블 정의 및 면경(alter)

# 데이터 조작어(Data Multipulation Language:DML)
#	: 데이터 조회, 수정, 추가, 삭제


# 데이터 제어어(Data Control Language:DCL)

create schema shopdb;
use shopdb;

 

CREATE TABLE `shopdb`.`member` (
  `memberID` CHAR(8) NOT NULL,
  `memberName` VARCHAR(10) NOT NULL,
  `memberAddress` VARCHAR(50) NULL,
  PRIMARY KEY (`memberID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin; 

INSERT INTO `shopdb`.`member` (`memberID`, `memberName`, `memberAddress`) VALUES ('id01', '홍길동', '서울시 마포구');
INSERT INTO `shopdb`.`member` (`memberID`, `memberName`, `memberAddress`) VALUES ('id02', '이몽룡', '경기도 안양시');
INSERT INTO `shopdb`.`member` (`memberID`, `memberName`, `memberAddress`) VALUES ('id03', '성춘향', '전라북도 남원시');

 select testdb from member;
 
 
 CREATE SCHEMA `testdb` DEFAULT CHARACTER SET utf8 ;
CREATE TABLE `testdb`.`product` (
  `productNo` VARCHAR(10) NOT NULL,
  `productName` VARCHAR(30) NULL,
  `productPrice` INT NULL,
  `productMaker` VARCHAR(30) NULL,
  `productDate` DATE NULL,
  PRIMARY KEY (`productNo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `testdb`.`product` (`productNo`, `productName`, `productPrice`, `productMaker`, `productDate`) VALUES ('1001', '노트북', '1000000', '삼성', '20211110');
INSERT INTO `testdb`.`product` (`productNo`, `productName`, `productPrice`, `productMaker`, `productDate`) VALUES ('1002', 'TV', '1200000', 'LG', '2021-10-10');
INSERT INTO `testdb`.`product` (`productNo`, `productName`, `productPrice`, `productMaker`, `productDate`) VALUES ('1003', '마우스', '30000', '로지텍', '2020/11/01');

select * from testdb.product;