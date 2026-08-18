# where 조건문 비교

# 저자가 '홍길동' 인 도서의 도서명, 저자 조회
select bookName, bookAuthor from bookdb.book where bookAuthor = '홍길동';

select * from book;
# 가격이 30000 이상인 도서의 도서명, 가격, 재고 조회
select bookName, bookPrice, bookStock from bookdb.book where bookPrice >= 30000;



# 재고량이 3~5인 도서 조회
select * from bookdb.book
	where bookStock between 3 and 5;

# 저자가 홍길동 이면서 재고가 3권 이상인 도서 조회
select * from bookdb.book where bookStock >= 3 and bookAuthor = '홍길동';
# 저자가 '홍길동' 또는 '성춘향' 인 도서 조회
select * from bookdb.book where bookAuthor = '홍길동' or bookAuthor = '성춘향';

# where 조건문 3) 범위 between and
# 도서가격이 25000 ~ 35000 인 도서명, 도서가격 조회
select bookName, bookPrice from bookdb.book where bookPrice between 25000 and 35000;
# # where 조건문 4) 리스트에 포함 in, not in
# 출판사가 '좋은출판사' 와 '강남출판사'인 도서의 도서이름, 저자 조회
select bookName, bookAuthor from bookdb.book where pubNo in (1, 2);

select * from publisher;

# 좋은출판사가 아닌 출판사에서 출간한 도서의 도서명, 출판사번호 조회
select bookName, pubNo from bookdb.book where pubNo not in (1);
# 저자가 홍길동 또는 '성춘향 인 도서 조회
select * from bookdb.book where bookAuthor in ('홍길동', '성춘향');

# where 조건문 5) NULL : is null, is not null
-- 고객의 취미가 빈문자열인 데이터 조회
select * from bookdb.bookClient where clientHobby = '';
-- 고객의 취미가 빈문자열인 경우 취미의 값을 null로 변경
update bookdb.bookClient set clientHobby = Null where clientHobby = '';

-- 고객의 취미가 null인 데이터 조회
select * from bookdb.bookClient where clientHobby is Null;

# where 조건문 6) 패턴매칭 Like (%, _)
-- 1990년대 출생한 고객의 이름과 생일 조회
select clientName, clientBirth from bookdb.bookclient where clientBirth like '199%';
-- 이름이 네 글자인 고객 정보 조회
select * from bookdb.bookClient where clientName like '____';
-- 고객이름에 '베'가 들어가는 고객의 정보 조회
select * from bookdb.bookclient where clientName like '%배%';