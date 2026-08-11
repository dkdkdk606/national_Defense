/*
DML : insert 문
- 테이블에 레코드 삽입(추가)

형식
	insert into 테이블명 (컬럼명1, 컬럼명2, ...) values (값1, 값2, ...);
 => 컬럼 순서와 개수가 일치해야 함
*/

use marketdb;

insert into membertype (membertype_id, membertype) values (1, '보통 회원');
insert into membertype (membertype_id, membertype) values (2, '할인 회원');
select * from membertype;

# customer 테이블 삽입
insert into customer (customer_id, customer_name, birthday, membertype_id)
	values (1, '김바람', '1984-06-24', 2);
insert into customer (customer_id, customer_name, birthday, membertype_id)
	values (2, '이구름', '1990-07-16', 1);
insert into customer (customer_id, customer_name, birthday, membertype_id)
	values (3, '박하늘', '1976-03-09', 2);
insert into customer (customer_id, customer_name, birthday, membertype_id)
	values (4, '강산', '1991-05-04', 1);
insert into customer (customer_id, customer_name, birthday, membertype_id)
	values (5, '유바다', '1993-04-21', 2);

insert into product (product_id, product_name, stock, price)
	values (1, '약용 입욕제', 100, 70);
insert into product (product_id, product_name, stock, price)
	values (2, '약용 핸드솝', 23, 700),
			(3, '천연 아로마 입욕제', 4, 120);

# 모든 필드 채운다면 열 이름 생략 가능
insert into product
	values	(4, '거품목욕제', 23, 120);

# 기본값이 없는 필드들 채우지 않으면 기본값으로 알아서 넣어줌
insert into product (product_id, product_name, stock)
	values (5, '거품', 23);

/* 그렇다고 파이썬처럼 매개변수를 비우면 오류;;
insert into product (product_id, product_name, stock, price)
	values (5, '거품', 23);
*/

DELETE FROM `marketdb`.`product` WHERE (`product_id` = '5');

select * from information_schema.table_constraints
	where constraint_schema = 'marketdb';

select * from product;

#데이터 임포트를 이용한 테이블 생성/데이터 입력

/*
1단계: 스키마 탭에서 데이터베이스이름 선택 후 마우스 우클릭 - [Table Data Import Wizard] 클릭
2단계: 임포트할 데이터파일(csv)을 지정 - [Next]
3단계: 기존의 테이블에 데이터 임포트할지 새로운 테이블을 만들지 선택
    - 기존의 테이블에 데이터 임포트인 경우 : 테이블 지정 -> [Next]
    - 새로운 테이블에 데이터 임포트인 경우 : 테이블명 지정-> [Next]
4단계: 임포트할 데이터와 테이블의 컬럼이 일치하는지 확인 -> [Next]
    - 컬럼별 데이터 형식 지정
5단계: Repair Import / Import data file [Next]클릭하여 수행
6단계: 데이터 생성 메시지 출력

*/


desc prodoctorder;

/*
문제 product.csv 파일을 임포트하여 새로운 product2 테이블생성하고,
	product 테이블과 같은 형식에 대이터로 변경
*/

desc product;
desc product2;

alter table product2 rename column prdNo to product_id;
alter table product2 modify product_id int not null primary key;

alter table product2 rename column prdName to product_name;
alter table product2 modify column product_name varchar(20) not null;

alter table product2 rename column prdPrice to price;
alter table product2 modify price int not null default 0;

alter table product2 drop column prdMaker;
alter table product2 drop column prdColor;
alter table product2 drop column ctgNo;

alter table product2 add stock int not null default 0 ;


# drop table product2;















