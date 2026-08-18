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
	studNo char(10) not null,
    studName varchar(20) not null,
    studYear int default 4 Check(studYear>=1 and studYear<=4),
	studAdress varchar(40),
    studBirthDay date,
    dptNO int,
    constraint Fk_student_department foreign key(dptNo) references department(dptNo)
);

INSERT INTO `testdb2`.`student` (`studNo`, `studName`, `studYear`, `studAdress`, `studBirthDay`, `DptNo`) VALUES ('2018', '홍길동', '4', '서울시 종로구', '1998-01-01', '1');
INSERT INTO `testdb2`.`student` (`studNo`, `studName`, `studYear`, `studAdress`, `studBirthDay`, `DptNo`) VALUES ('2021', '이몽룡', '1', '경기 안양', '2001-12-12', '2');
INSERT INTO `testdb2`.`student` (`studNo`, `studName`, `studYear`, `studAdress`, `studBirthDay`, `DptNo`) VALUES ('2020', '성춘향', '2', '전북 남원', '2001-10-10', '3');


create table professor(
	profNo int primary key not null,
    profName varchar(20) not null,
    profRank varchar(40),
    profPhone varchar(40),
    dptNo int,
    constraint Fk_professor_department foreign key(dptNo) references department(dptNo)
);

create table course(
	courNo varchar(10) primary Key not null,
    courName varchar(40) not null,
    courScore float,
    profNo int,
	constraint Fk_course_professor foreign key(profNo) references professor(profNo)
);


create table scores(
	# 참고 : 복합키로 주키 설정 시
	#	필드명 뒤에 primary key를 각각 사용할 경우 오류 발생
	# studNo char(10) not null primary key,
    # courNo varchar(10) not null primary key,
    # Error Code: 1068. Multiple primary key defined	0.000 sec

	score int,
    grade char(4),
    constraint Fk_result_student foreign key(studNo) references student(studNo),
    constraint Fk_result_course foreign key(courNo) references course(courNo)
);


