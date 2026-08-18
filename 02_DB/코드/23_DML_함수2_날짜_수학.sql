# 날짜/시간 관련 함수들
-- 날짜나 시간데이터를 활용하기 위해서
-- 일정 기간의 데이터를 검색하기 위해서

# 1. DBMS서버의 현재 날짜나 시간
# - CURRENT_DATE : 서버의 현재 날짜(연-월-일)
# - CURRENT_TIME : 서버의 현재 시간(시:분:초)
# - CURRENT_TIMESTAMP : 서버의 현재 날짜와 시간
# - NOW : 서버의 현재 날짜와 시간
# - 시간관련 함수의 경우 인수로 3과 같이 정수를 주면 밀리초 단위까지 확인

select current_date(), current_time(), current_timestamp(), now();
select current_date(), current_time(3), current_timestamp(3), now(3);
select current_date(), current_time(2), current_timestamp(2), now(4);

# 2. 국제표준(UTC) 날짜나 시간
# - UTC_DATE : 세계표준 날짜(연-월-일)
# - UTC_TIME : 세계표준 시간(시:분:초)
# - UTC_TIMESTAMP : 세계표준 날짜와 시간

select utc_date(), utc_time(), utc_timestamp();
select utc_date(), utc_time(4), utc_timestamp(2);

# 3. 날짜 더하기, 빼기 : DATE_ADD, DATE_SUB

-- 현재 날짜의 연도에 1년 증가한 날짜
select now(), date_add(now(), interval 1 year);

-- 현재 날짜의 연도에 1년 감소한 날짜
select now(), 
	date_add(now(), interval -1 year),
	date_sub(now(), interval 1 year);
    
# 4. 날짜 간 차이 구하기 : DATEDIFF, TIMESTAMPDIFF
# - DATEDIFF() : 날짜간 일수 차이 반환
# - TIMESTAMPDIFF() : 연, 월, 일, 시간 등의 기준에 따라 두 날짜의 차이를 반환
#       기준 : year, month, day, quarter, hour, minute, second

-- 일수 차이
select datediff('2023-12-31 23:59:59.999999', '2023-01-01 00:00:00.000000');

select timestampdiff(year, '2023-12-31 23:59:59.999999',
 '2023-01-01 00:00:00.000000');

select timestampdiff(month, '2023-12-31 23:59:59.999999',
 '2023-01-01 00:00:00.000000');

select timestampdiff(day, '2023-12-31 23:59:59.999999',
 '2023-01-01 00:00:00.000000');

select timestampdiff(minute,  '2023-01-01 00:00:00.000000', 
'2023-12-31 23:59:59.999999');


# 5. 지정한 날짜의 요일 반환 : DAYNAME

select dayname('2025-12-30');


# 6. 날짜의 연, 월, 일, 주 등을 반환 
# - YEAR()
# - MONTH()
# - WEEK()
# - DAY()

select year('2025-12-30'), month('2025-12-30'), 
	day('2025-12-30'), week('2025-12-30');
    
# 7. 시간이 시, 분, 초 반환
# - HOUR()
# - MINUTE()
# - SECOND()

select now(), hour(now()), minute(now()), second(now());

# 8. 날짜 형식 변환 : DATE_FORMAT, GET_FORMAT
# - DATE_FORMAT(날짜, 국가나지역)
# - GET_FORMAT(날짜, 국가나지역)

select
	get_format(date, 'USA') as USA,
	get_format(date, 'EUR') as EUR,
    get_format(date, 'ISO') as ISO,
    get_format(date, 'INTERNAL') as INTERNAL;
    
select
	date_format(now(), get_format(date, 'USA')) as USA,
	date_format(now(), get_format(date, 'EUR')) as EUR,
    date_format(now(), get_format(date, 'ISO')) as ISO,
    date_format(now(), get_format(date, 'INTERNAL')) as INTERNAL;
    
# 수학관련 함수
# - round(), floor(), ceil() : 반올림, 올림, 내림
# - rank(), dense_rank(), row_number() : 
# 	순위 출력(동일순위 개수만큼 증가), 동일순위 상관없이 1 증가, 행 순위
# - 삼각함수, 절대값 등
