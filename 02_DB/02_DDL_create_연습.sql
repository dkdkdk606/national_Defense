Create schema Testdb2 default character set utf8mb4;
use Testdb2;

Create Table department(
	dptNo int primary key,
    dptName varchar(20) not null,
    dptTel varchar(20)
);

INSERT INTO `testdb2`.`department` (`dptNo`, `dptName`, `dptTel`) VALUES ('1', '컴퓨터학과', '02-1111-1111');
INSERT INTO `testdb2`.`department` (`dptNo`, `dptName`, `dptTel`) VALUES ('2', '정보통신학과', '031-2222-2222');
INSERT INTO `testdb2`.`department` (`dptNo`, `dptName`, `dptTel`) VALUES ('3', '경영학과', '032-3333-3333');

use Testdb2;
Create Table student(
	stdNo int primary key,
    stdName varchar(20) not null,
    stdYear int default 4 Constraint check_class Check(stdYear>=1 and stdYear<=4),
	stdAdress varchar(40),
    stdBirthDay date,
    dptNO int,
    constraint Fk_student_department foreign key(dptNo) references department(dptNo)
);

INSERT INTO `testdb2`.`student` (`stdNo`, `stdName`, `stdYear`, `stdAdress`, `stdBirthDay`, `DptNo`) VALUES ('2018', '홍길동', '4', '서울시 종로구', '1998-01-01', '1');
INSERT INTO `testdb2`.`student` (`stdNo`, `stdName`, `stdYear`, `stdAdress`, `stdBirthDay`, `DptNo`) VALUES ('2021', '이몽룡', '1', '경기 안양', '2001-12-12', '2');
INSERT INTO `testdb2`.`student` (`stdNo`, `stdName`, `stdYear`, `stdAdress`, `stdBirthDay`, `DptNo`) VALUES ('2020', '성춘향', '2', '전북 남원', '2001-10-10', '3');

