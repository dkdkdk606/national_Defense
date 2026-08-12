/*
DML(2) : Update
- 특정한 컬럼(열/필드/속성)의 값을 수정 -> 데이터 수정
- 조건에 맞는 행을 찾아서 열의 값을 수정

- 형식
	Update	테이블명	SET		컬럼=값				where	조건;
- ex
	update	procuct		set		prdName='UHD TV'	where	prdNo='5';
*/
use marketdb;
update product set price=130 where product_id='3';

# 문제 bookdb 에서 도서번호가 1001 인 도서가격을 25000으로 수정alter
update bookdb.book set bookprice = 25000 where bookNo = '1001';
# 출판사 번호가 '1'인 출판사의 이름을 '좋은출판사'로 변경
update bookdb.publisher set pubName = '좋은출판사' where pubNo = '1';

select * from bookdb.book;
select * from bookdb.publisher;


















