/*
DML(3) : Delete
- 테이블에 있는 기존 행을 삭제
- 형식
	delete	from	테이블명	where	조건;
- ex
	delete	from	product		where	prdNAME='그늘막텐트';
	delete from product;  -> 모든 행 삭제
*/

select * from marketdb.product;

delete from marketdb.product where product_name = '거품목욕제';
#아래 둘 다 안됨 정확해야함
delete from marketdb.product where product_name = '거품목욕';
delete from marketdb.product where product_name = '거품 목욕제';

use bookdb;

select * from bookdb.book;
#문제. bookdb 에서 도서명이 '자료구조'인 행을 삭제
delete from bookdb.book where bookName = '자료구조';
#도서 발행일이 2019년도인 행을 삭제
delete from bookdb.book where bookdate >= '2019-01-01' and bookdate <= '2019-12-31';
delete from bookdb.book where bookdate = '2019';
delete from bookdb.book where bookdate between '2019-01-01' and '2019-12-31';


#취미가 빈문자열인 행 삭제
select * from bookdb.bookclient;
delete from bookdb.bookclient where clientHobby = '';

select * from information_schema.table_constraints
	where constraint_schema='bookdb';


/*
10:24:55	delete from bookdb.book where bookdate >= '2019-01-01' and bookdate <= '2019-12-31'
Error Code: 1451. Cannot delete or update a parent row:
a foreign key constraint fails (`bookdb`.`booksale`, CONSTRAINT `FK_bookSale_bookNo` FOREIGN KEY (`bookNo`) REFERENCES `book` (`bookNo`))	0.000 sec

10:29:12	delete from bookdb.book where bookdate = '2019'
Error Code: 1292. Incorrect date value: '2019' for column 'bookdate' at row 1	0.000 sec

10:30:37	delete from bookdb.bookclient where clientHobby = ''	
Error Code: 1451. Cannot delete or update a parent row:
a foreign key constraint fails (`bookdb`.`booksale`, CONSTRAINT `FK_bookSale_clintNo` FOREIGN KEY (`clientNo`) REFERENCES `bookclient` (`clientNo`))	0.000 sec

*/

