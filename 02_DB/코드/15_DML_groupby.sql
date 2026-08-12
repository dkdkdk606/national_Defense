/*
그룹별 집계 : GROUP BY

- 특정할 열(컬럼)을 기준으로 그룹화한 후 각 그룹에 대한 질의 결과를 한 행씩 생성
- 형식 :
	select 집약키컬럼, 집계함수(컬럼), ...
		from 테이블명
		GROUP BY 열이름
        Having 검색(필터링)조건
    집약키 : GROUP BY에서 지정된 열 이름 
			집약키는 여러 개 지정 가능
	집약키에 따라 그룹화 한 후 그룹별로 집계함수 조건에 따른 질의 결과 생성
    HAVING 검색(필터링)조건은 반드시 group by 뒤에 와야 함. order by뒤에 오면 오류
- 주의사항:
    select구에서 1개의 값을 반환하는 상수, GROUP BY에서 사용한 열,
    집계함수만 나올 수 있음

- 그룹별 연산 단계:
    1단계(SPLIT): 그룹별 데이터 분리
    2단계(APPLY) : 집계함수나 그룹별 연산을 적용
    3단계(MERGE) : 그룹별 연산 결과 통합
*/

# 도서별 주문량 합계 출력
select bookNo, sum(bsQty) as '주문량 합계'
	from bookdb.booksale
	group by bookNo;


select * from bookdb.booksale;
#도서별 주문량 합계를 2번째 열 기준으로 정렬하여 출력
select bookNo, sum(bsQty) as '주문량 합계'
	from bookdb.booksale
	group by bookNo
    order by 2;
    
#도서별 주문량 합계를 2번째 열 기준으로 정렬하여 출력
select bookNo, sum(bsQty) as '주문량 합계'
	from bookdb.booksale
	group by bookNo
    order by 2;
    
select bookNo, sum(bsQty) as '주문량 합계'
	from bookdb.booksale
	group by bookNo
    order by sum(bsQty);
    
select bookNo, sum(bsQty) as '주문량합계'
	from bookdb.booksale
	group by bookNo
    order by 주문량합계;	# 별칭 이름으로도 정렬 가능
							# 별칭 이름이 공백이 들어가면 여러 구문으로 해석되어 실행되지 않음
                            # 별칭이름은 공백없이 작성
    
select * from bookdb.booksale order by 1 desc;

select bookNo, sum(bsQty) as '주문량합계'
	from bookdb.booksale
	group by bookNo
    with rollup;

select bookNo, sum(bsQty) as '주문량합계'
	from bookdb.booksale
	group by bookNo
    with rollup
    order by 2 desc;

# group by + having절
-- having 검색조건(필터링)
-- group by에 의해 구성된 그룹들에 대해 적용할 조건 기술
-- 검색조건(필터링) : 집계함수, 비교연산을 주로 사용
-- group by 없이 단독으로 사용 불가
-- where절 뒤에 위치
-- where절: 개별 행 필터링 / having절 : 그룹별 필터링

-- 출판사별 도서 총 수 출력
select pubNo, count(*) as '도서총수'
	from bookdb.book
    group by pubNo
    with rollup
    order by 2 desc;

select * from book;

# 가격이 25000원 이상인 도서 5개 이상인 출판사
select pubNo, count(*) as '25000_이상_도서총수'
	from bookdb.book
    where bookprice >= 25000
    group by pubNo
    having 25000_이상_도서총수 >=5;


select pubNo, count(*), avg(bookprice)
	from bookdb.book
    group by pubNo;


select pubNo, count(*), avg(bookprice)
	from bookdb.book
    group by pubNo
    having avg(bookprice) >= 25000;

## group by 한 결과들 리스트로 concat

select count(*)
    from bookdb.book
    where bookPrice>=25000 and pubNo='2';

select count(*)
    from bookdb.book
    where bookPrice>=25000 and pubNo='3';

select count(*)
    from bookdb.book
    where bookPrice>=25000 and pubNo='1';

-- 고객별 구매한 책번호 조회
select bookNo
	from bookdb.booksale
    where clientNo=2;
# 그룹바이 집계 결과를 병합하기 어려움 <- 그룹별 결과가 서로 다른 길이를 가짐
/*select bookNo
	from bookdb.booksale
    group by clientNo;
16:23:46	select bookNo  from bookdb.booksale     group by clientNo LIMIT 0
5000	Error Code: 1055. Expression #1
of SELECT list is not in GROUP BY clause and contains nonaggregated
column 'bookdb.booksale.bookNo' which is not functionally dependent on columns in
GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.000 sec
*/
select *
	from bookdb.booksale;


select clientNo, group_concat(bookNo separator ',') as 'bookID'
	from bookdb.booksale
    group by clientNo;

#1. 도서 테이블에서 가격 순으로 내림차순 정렬하여, 도서명, 저자, 가격 출력 (가격이 같으면 저자 순으로 오름차순 정렬)
select * from book;
select bookName, bookAuthor, bookPrice
	from bookdb.book
    order by bookprice desc, bookAuthor asc;
#2. 도서 테이블에서 저자에 '길동'이 들어가는 도서의 총 재고 수량 계산하여 출력
select sum(bookStock) from bookdb.book
	where bookAuthor like '%길동%';

#3. 도서 테이블에서 ‘좋은출판사' 도서 중 최고가와 최저가 출력 publisher
select max(bookprice), min(bookprice) from bookdb.book
	where pubNo = 1;
    
select max(bookprice), min(bookprice) from bookdb.book
	where pubNo = (select pubNo 
					from bookdb.publisher 
					where pubName = '좋은출판사');
    
#4. 도서 테이블에서 출판사별로 총 재고수량과 평균 재고 수량 계산하여 출력
select pubNo, sum(bookStock) as '총재고수량',
				avg(bookstock) as '평균재고수량'
                from bookdb.book
				group by pubNo;

#5. 도서판매 테이블에서 고객별로 ‘총주문수량’과 ‘총주문건수’ 출력.
select * from bookdb.bookSale;
select clientNo,
		sum(bsqty) as '총주문수량',
		count(*) as '총주문건수'
        from bookdb.bookSale
	group by clientNo;
#6. 도서판매 테이블에서 고객별로 ‘총주문수량’과 ‘총주문건수’ 출력, 단 주문 건수가 2이상인 고객만 해당
select clientNo,						#4
		sum(bsqty) as '총주문수량',		#4
		count(*) as '총주문건수'		#4
			from bookdb.booksale		# 1 
			group by clientNo			# 2 (where 생략)
            having count(*) >= 2;		# 3
            









