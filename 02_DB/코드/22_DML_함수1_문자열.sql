# MySQL의 내장함수(built-in function)
/*
 - MySQL이 미리 만들어둔 함수
 - 문자열 함수 : 형변환, 부분문자열, 문자개수/바이트수, 비교, 치환, 결측치, ...
 - 날짜 함수 : 현재 날짜와 시간, 표준 날짜와 시간, 
	  			두 날짜의 길이(시간, 분,....), 연도,월,일,시,분,초 정보
 - 수학 함수 : 반올림, 올림, 내림, 절대값, 사인, 코사인, ....
 - 집계 함수 : 합계, 평균, 표준편차, 최대, 최소, ...
 - 분석 함수 : LAG, LEAD(앞뒤 데이터 조회), 누적분포, 상대순위 계산, 첫줄/마지막행
*/

# 문자열 함수

# 1. 문자열 연결 :
#  - 여러 문자열 하나로 결합
#  - CONCAT(문자열1, 문자열,...) : 문자열들을 하나로 결합
#  - CONCAT_WS(구분자, 문자열1, 문자열,...) : 구분자를 사이에 두고 결합

select concat('I', 'Love', 'MySQL') as col1,
	concat('I', ' Love', ' MySQL') as col2,
    concat_ws(' ', 'I', 'Love', 'MySQL') as col3,
    concat_ws(',', 'I', 'Love', 'MySQL') as col4;

use bookdb;

select concat(clientName, clientPhone) as '고객정보' from bookClient;
select concat_ws(': ', clientName, clientPhone) as '고객정보' from bookClient;

# 2. 형변환
# - 데이터 형식을 명시적으로 변환
# - CAST(컬럼 as 데이터유형) : 표준 SQL 방식의 형변환
# - CONVERT(컬럼, 데이터유형) : MySQL의 확장방식의 형변환 + 문자셋 변환

# - CAST/CONVERT에 사용가능한 데이터 유형 : 
#   BINARY, CHAR, DATE, DATETIME, TIME, DECIMAL, JSON, NCHAR, SIGNED, UNSIGNED

select 	4/2, 4/'2', 4/cast('2' as unsigned);
select 	4/3, 4/'3', 4/cast('3' as unsigned);
select cast('123' as signed) as col1,
	cast('3.14' as decimal(5,2)) as col2,
    cast(100 as char) as col3,
    cast('2025-02-04' as date) as col4,
    cast(3.99 as unsigned) as col5;

select 
	convert('123', signed) as col1,
    convert(100, char) as col2,
    convert('안녕하세요' using utf8mb4) as col3,
    convert('hello' using latin1) as col4,
    convert(now(), signed) as col5;

# 형변환 적용 사례
-- # 문자열데이터를 숫자 변환 후 집계 함수 적용
-- select sum(cast(price as decimal(10,2))) from order;

-- # 날짜문자열을 기준으로 정렬
-- select * from logs where cast(log_date as date) desc;

-- # 수치 연산 보장
select '5' / 2;
select 5 / 2;
select cast(5 as decimal) / 2;

-- # 문자 인코딩 대응
-- select convert(col_name using utf8mb4) from table_name;

use world;
show tables;
desc country;

select * from country limit 20;

select Name, SurfaceArea, cast(SurfaceArea as unsigned) as surface_int
	from country limit 10;
    

# 3. 결측치 처리
# NULL : 값이 존재하지 않음(unknown)

select 100 + null;
-- select avg(col);  null 자동 제외

# 결측치 처리 목적:
# - NULL을 다른 값으로 치환
# - 조건으로 NULL 판별
# - NULL로 인해 계산이 안되는 것 방지

# 3-1) 결측치 판단 : ISNULL
# ISNULL(컬럼)

# 샘플 DB생성
use exdb;
create table acorn_null(
	col1 int,
    col2 varchar(10),
    col3 varchar(10),
    col4 varchar(10),
    col5 varchar(10)
);

insert into acorn_null values 
	(1, null, 'col3','col4','col5'),
    (2, null, null, null,'col5'),
    (3, null, null, null, null);
    
select * from acorn_null;

-- 결측치 판단
select col1, isnull(col2), isnull(col3) from acorn_null;

# 3-2) 결측치 대체 : IFNULL, COALESCE
-- COALESCE(표현식1, 표현식2,....) :
--    왼쪽부터 검사해서 NULL이 아닌 첫번째 값 반환
--    인자 개수 제한 없음
--    표준 SQL 함수

-- IFNULL(표현식, 대체값) : 
--    NULL을 지정한 값으로 단순 대체
--    MySQL 전용 함수

-- select coalesce(phone, email, '연락처없음') as contact from customers;
-- -> phone, email 컬럼의 값을 차례로 조회하면서 
--     null이 아닌 값으로 첫번째 만나는 값을 반환,
--     모두 null이면 '연락처없음' 반환

select col1, coalesce(col2, col3, col4, col5, '없음')  from exdb.acorn_null;
select col1, ifnull(col2, '*')  from exdb.acorn_null;
select col1, ifnull(col2, '')  from exdb.acorn_null;
select col1, ifnull(col2, col5)  from exdb.acorn_null;

# 3-3) NULL로 변경 : NULLIF
-- NULLIF(표현식1, 표현식2) :
--   표현식1=표현식2 이면 NULL 반환
--    다르면 표현식1 그대로 반환
-- 결측을 의미하는 0, 빈문자열 '', 기본값 -1, 자리채움용 값 'N/A'
--  => null로 통일하기 위해서

create table acorn_null2(
	num1 int,
    num2 int
);

insert into acorn_null2 values (10, 3), (5, null), (3, 5);
insert into acorn_null2 values (10, 0);
select * from acorn_null2;

select num1 / num2 from acorn_null2;

select 100 / nullif(num2, 0) from acorn_null2;
select 100 / nullif(num1, 10) from acorn_null2;

select num2, if(num2 is null, 0, num2) as num2_ from acorn_null2;


# 4. 소문자, 대문자 변환 : LOWER, UPPER

select col1, col4, col5, upper(col5), lower(col4) from acorn_null;


# 5. 공백 제거 : TRIM, LTRIM, RTRIM

select '      acorn! MySQL    ' as col1, 
	trim('      acorn! MySQL    ') as col_trim,
	ltrim('      acorn! MySQL    ') as col_ltrim,
    rtrim('      acorn! MySQL    ') as col_rtrim;

select trim(both '#' from '# acorn! MySQL #') as col1,
	trim(leading '#' from '# acorn! MySQL #') as col2,
    trim(trailing '#' from '# acorn! MySQL #') as col3;
    

# 6. 문자열 크기/개수 : LENGTH, CHAR_LENGTH
# - LENGTH() : 문자열 바이트 수 반환
# - CHAR_LENGTH() : 문자열 개수 반환
# - 한글을 3바이트, 영문은 1바이트

select length(locName), char_length(locName) from exdb.location;
select length('acorn! MySQL'), length('에스큐엘 짱!'),
	char_length('acorn! MySQL'), char_length('에스큐엘 짱!');
    

# 7. 특정 문자까지의 길이 : POSITION
# - 지정한 특정 문자까지의 문자열 길이 반환
# - 특정문자가 없는 경우 0 반환
# - 문자열의 위치는 1부터 시작

select 'acorn! MySQL', position('!' in 'acorn! MySQL'),
	position('#' in 'acorn! MySQL'),
    position('my' in 'acorn! MySQL');
    

# 8. 지정한 길이의 문자열 반환 : REFT, RIGHT
# - REFT(문자열, 길이) : 문자열 왼쪽부터 지정한 길이 만큼의 문자열 반환
# - RIGHT(문자열, 길이) : 문자열 오른쪽부터 지정한 길이 만큼의 문자열 반환

select 'acorn! MySQL', 
	left('acorn! MySQL', 6),
    right('acorn! MySQL', 3);
    

# 9. 부분문자열 : SUBSTR, SUBSTRING
# - SUBSTR(문자열, 시작위치, 길이)
# - SUBSTRING(문자열, 시작위치, 길이)

select 'acorn! MySQL', 
	substr('acorn! MySQL', 6, 3),
    substring('acorn! MySQL', 3, 5);

select 'abc@email.com',
	position('@' in 'abc@email.com'),
	substr('abc@email.com', 1, position('@' in 'abc@email.com')-1);


-- 생년월일에서 연도분리
use bookdb;
select clientBirth, 
		substr(clientBirth, 1, position('-' in clientBirth)-1)
    from bookdb.bookClient;
select clientBirth, year(clientBirth)
		from bookdb.bookClient;

-- 고객성명을 성과 이름으로 분리
use marketdb;
select customer_name  as '성명', 
		substr(customer_name,1,1) as '성', 
        substr(customer_name,2,2) as '이름'
	from marketdb.customer;
    
-- '김'씨 성을 가진 고객이름 조회
select customer_name
	from marketdb.customer
	where substr(customer_name,1,1) = '김';
    

# 10. 문자열 치환 : REPLACE
# - REPLACE(문자열, 특정문자열, 대체문자열)

select customer_name, 
		replace(customer_name, '김', 'Kim')
	from marketdb.customer
	where customer_name like '김%';
    

# 11. 문자열 반복 : REPEAT
# - REPEAT(문자열, 반복수)

select 'Ha', repeat('Ha', 10);


# 12. 공백문자생성 : SPACE

select customer_name, 
		concat(substr(customer_name,1,1), 
				space(5),
                substr(customer_name,2,2))
	from marketdb.customer;


# 13. 문자열 역순으로 출력 : REVERSE
# - REVERSE

select 'acorn! MySQL', reverse('acorn! MySQL');

with ip_list(ip)
as (
	select '192.168.0.1'
	union all
	select '10.6.100.99'
	union all
	select '8.8.8.8'
	union all
	select '192.200.211.111'
)
select ip, 
	reverse(ip),
	substr(ip, 1, char_length(ip) - position('.' in reverse(ip)))
 from ip_list;
 

# 14. 문자열 비교 : STRCOMP
# - 두 문자열이 동일하면 0 반환, 다르면 -1 반환

select strcmp('acorn! MySQL', 'acorn! MySQL'),
	strcmp('acorn! MySQL', 'acorn# MySQL');