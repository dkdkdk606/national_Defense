/*
ALTER 문
: 테이블을 수정
 - 테이블에 대한 정의 변경
 - 새로운 열(컬럼/필드)을 추가
 - 특정 열의 기본값 변경
 - 특정 열 삭제 등

2. ALTER 문 형식
ALTER Table
	ADD :열 추가
    RENAME COLUMN : 열 이름 변경
    MODIFY : 열의 데이터 형식 변경
    CHANGE : 열 이름과 데이터 형식 변경
    DROP COLUMN : 열 삭제
    DROP : 여러 개 열 삭제
    DROP PRIMARY KEY : 기본 키 삭제
    DROP CONSTRAINT : 제약조건 삭제


alter문 1.열(컬럼) 추가
alter table 테이블명 add 컬럼이름 자료형;
alter table 테이블명 add (컬럼이름1 자료형1,
						컬럼이름2 자료형2,
                        컬럼이름3 자료형3,
                        ...,
                        컬럼이름n 자료형n);
);
*/

# 테이블 구조 확인 :
# 테이블 구조 확인 :
-- desc 테이블명;
-- describe 테이블명;
desc student;
describe course;


use testdb2;
alter table student add studAge varchar(2);
alter table student add (
	studTel varchar(15),
    studPostCode varchar(6)
);
alter table student add  studAddress2 varchar(20) null;

/*
alter문 2. 열속성 변경 Modify
alter table 테이블명 modify 칼럼이름 변경할데이터형식;
*/

alter table student modify studName varchar(20) null;

# alter 문 3. 열이름 변경 Rename column
-- alter table 테이블명 rename column 변경전이름 to 변경후이름
alter table student rename column studTel to studHP;

# alter문 4. 컬럼 이름과 데이터 유형을 함께 변경 Change
-- alter table 테이블명 change 컬럼변경점이름 변경후이름 변경할데이터형식;

alter table student change studAddress  studAddress1 varchar(30);

# alter문 5. 컬럼 삭제 Drop
-- alter table 테이블명 drop column 컬럼명; # 한 컬럼만 삭제
/* alter table 테이블명 drop 컬럼명1, # 여러 컬럼 삭제
					  drop 컬럼명2,
                      drop 컬럼명3, 
*/
alter table student drop column studHP;
alter table student drop studAge,
					drop studAdress,
                    drop studPostCode;
                    
# alter문 6. 제약조건 변경 Drop constraint
/*
- 기본키 삭제:a
	alter table 테이블명 drop primary key;
    
* A테이블의 기본키를 외래키로 참조하고 있는 테이블B가 있다면
  먼저 A의 기본키를 참조하여 외래키로 사용하고 있는 테이블 B에서 외래키를 삭제한 후
  A테이블의 기본키 삭제 가능
*/

# 외래 키 제약조건 삭제
alter table student drop constraint FK_student_department;
alter table professor drop constraint Fk_professor_department;

# 외래 키 삭제
alter table department drop primary key;
# 원인: department 테이블의 기본키 컬럼을 참조하는 테이블이 존재하기 때문에
-- Error Code: 1553. Cannot drop index 'PRIMARY': needed in a foreign key constraint
# 해결방법 : 기본키를 외래키로 갖는 

# alter 문 6. 제약조건 변경(2) 기본키/외래키 제약조건 추가
# 기본키 추가
-- alter table 테이블명 add primary key (컬럼명);
-- alter table 테이블명 add constraint 제약조건이름 primary key (컬럼명);

# 외래키 제약조건 추가
-- alter table 테이블명 add constraint 제약조건이름 foreign key(컬럼명);
-- 	  					  references 참조테이블명(컬럼명);
# 외래키를 설정하려면 먼저 기본키를 갖는 테이블에서 기본키를 설정해야 함
alter table department add constraint PK_department_dptNo
	primary key(dptNo);

alter table professor add constraint FK_professor_dptNo
	foreign key professor(dptNo) references department(dptNo);

alter table student add constraint FK_student_dptNo
    foreign key(dptNo) references department(dptNo);

desc professor;
desc student;

# 제약조건 목록 보기
show databases;
select * from information_schema.table_constraints
	where constraint_schema='testdb2';

# alter문 6. 제약조건 변경(3) : 외래키 제약조건 설정값 변경
/*
외래키 제약조건 시 on Update RESTRICT / on Delete RESTRICT로 설정된 경우:
	외래키로 참조되고 있는 기본키를 갖는 테이즐에서 행을 삭제하거나 변경할 때 오류 발생
예1. department 테이블의 한 레코드의 학과코드를 3에서 10으로 변경 시 오류 발생
UPDATE `testdb2`.`department` SET `dptNo` = '10' WHERE (`dptNo` = '3');
ERROR 1451: 1451: Cannot delete or update a parent row:
    a foreign key constraint fails (`testdb2`.`student`,
    CONSTRAINT `FK_student_dptNo` FOREIGN KEY (`dptNo`)
    REFERENCES `department` (`dptNo`))
    
예2. dapartment의 3열 삭제할 때 오류 발생
DELETE FROM `testdb2`.`department` WHERE (`dptNo` = '3');

ERROR 1451: 1451: Cannot delete or update a parent row:
    a foreign key constraint fails (`testdb2`.`student`,
    CONSTRAINT `FK_student_dptNo` FOREIGN KEY (`dptNo`)
    REFERENCES `department` (`dptNo`))
*/

## 외래 키 제약조건 설정값 변경 방법 ;
# 1단계: 외래키 기존제약 조건 삭제
# 2단계: 외래키 제약조건 다시 설정 =>
# 	on Update CASCADE/ on Delete CASCADE 로 설정 cascade로 바꾸면 한쪽에서 바뀌면 다른쪽도 바로 바뀜
use testdb2;
# 1단계: 외래키 기존제약 조건 삭제 
alter table professor drop constraint FK_professor_dptNo;
alter table student drop constraint FK_student_dptNo;
# 2단계: 외래키 제약조건 다시 설정

alter table professor add constraint FK_professor_dptNo
	foreign key professor(dptNo) references department(dptNo)
	on delete restrict on update cascade;
alter table student add constraint FK_student_dptNo
    foreign key(dptNo) references department(dptNo)
    on delete restrict on update cascade;
    
#alter문 6. 제약조건 추가/삭제
/*
 * 제약조건 삭제나 변경 전 확인
	select * from information_schema.table_constraints
		where constraint_schema='testdb2';
	select * from information_schema.table_constraints
		where constraint_schema='testdb2' and table_name='student';
*/

	select * from information_schema.table_constraints
		where constraint_schema='testdb2' and table_name='student';

/* student 테이블에 학생 정보를 추가할 때 학년을 5로 주면 오류 -> check 제약조건 때문에
UPDATE `testdb2`.`student` SET `studYear` = '5' WHERE (`studNo` = '2018');
ERROR 3819: 3819: Check constraint 'student_chk_1' is violated.
*/

# Check 제약조건 삭제 
alter table student drop constraint student_chk_1;

# check 제약조건 변경 : 1<= studYear <= 5
alter table student add check(studYear >= 1 and studYear <= 5);

#alter문 8. 테이블 이름 변경 rename
/*
한 개 테이블명 변경
-- alter table old테이블명 rename new테이블명;
여러 테이블 이름 한번에 변경
-- rename table old테이블명1 to new테이블명1,
				old테이블명2 to new테이블명2,
                old테이블명3 to new테이블명3,
                ...;
*/              

alter table board2 rename boardTable;
