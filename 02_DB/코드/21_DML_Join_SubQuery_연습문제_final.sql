use bookshopdb;

/* 조인 연습문제 */
use bookdb;

#1. 모든 도서에 대하여 도서의 도서번호, 도서명, 출판사명 출력
select bookNo, bookName, pubName
	from bookdb.book B
    join bookdb.publisher P
    on B.pubNo = P.pubNo;

#2. '서울 출판사'에서 출간한 도서의 도서명, 저자명, 출판사명 출력(조건에 출판사명 사용)
  select B.bookName, B.bookAuthor, P.pubName
	from bookdb.book B
    join bookdb.publisher P
		on B.pubNo = P.pubNo
	where P.pubName = '정보출판사';

#3. '정보출판사'에서 출간한 도서 중 판매된 도서의 도서명 출력
#   (중복된 경우 한 번만 출력) (조건에 출판사명 사용)
select distinct B.bookName
	from bookdb.book B
    right join bookdb.booksale BS
    on B.bookNo = BS.bookNo;
    
#4. 도서가격이 30,000원 이상인 도서를 주문한 고객의 
#   고객명, 도서명, 도서가격, 주문수량 출력
select BC.clientName, B.bookName, B.bookPrice, BS.bsQty
	from bookdb.bookclient BC
    join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
    join bookdb.book B
    on BS.bookNo = B.bookNo
    where B.bookprice >= 30000;
    
#5. '안드로이드 프로그래밍' 도서를 구매한 고객에 대하여
#   도서명, 고객명, 성별, 주소 출력 (고객명으로 오름차순 정렬)
select bookName, clientName, clientGender, ClientAddress
	from bookdb.bookclient BC
    right join bookdb.booksale BS
    on BC.clientNo = BS.clientNo
    join bookdb.book B
    on BS.bookNo = B.bookNo
    where B.bookname = '안드로이드 프로그래밍'
    order by BC.clientName;

#6. '도서출판 강남'에서 출간된 도서 중 판매된 도서에 대하여 '총 매출액' 출력
select sum(BS.bsQty * B.bookprice) as '총 매출액'
  from bookdb.booksale BS
  join bookdb.book B
    on BS.bookNo = B.bookNo
  join bookdb.publisher P
    on B.pubNo = P.pubNo
  where P.pubName = '도서출판 강남';
/*
ERROR 1054 (42S22): Unknown column 'BS.bookprise' in 'field list'
ERROR 1054 (42S22): Unknown column 'B.bookprise' in 'field list'
*/
#7. '서울 출판사'에서 출간된 도서에 대하여 
#   판매일, 출판사명, 도서명, 도서가격, 주문수량, 주문액 출력
select BS.bsDate, P.pubName, B.bookName, B.bookPrice, BS.bsQty, (BS.bsQty * B.bookPrice) as '주문액'
  from bookdb.booksale BS
    join bookdb.book B
      on BS.bookNo = B.bookNo
    join bookdb.publisher P
      on B.pubNo = P.pubNo
    where pubName = '서울 출판사';

#8. 판매된 도서에 대하여 도서별로 도서명, 총 주문 수량 출력
select B.bookName, sum(BS.bsqty) as '총 주문 수량'
  from bookdb.booksale BS
  join bookdb.book B
   on BS.bookNo = B.bookNo
  group by B.bookName;

#9. 판매된 도서에 대하여 고객별로 고객명, 총구매액 출력
#   (총구매액이 100,000원 이상인 경우만 해당)
select BC.clientName, sum(BS.bsQty * B.bookprice) as '총구매액'
  from bookdb.booksale BS
  join bookdb.bookclient BC
    on BS.clientId = BC.clientId
  join bookdb.book B
    on BS.bookNo = B.bookNo
  group by BC.clientId, BC.clientName;

/*
ERROR 1054 (42S22): Unknown column 'BS.clientNo' in 'on clause'

*/

#10. 판매된 도서 중 '도서출판 강남'에서 출간한 도서에 대하여 
#    고객명, 주문일, 도서명, 주문수량, 출판사명 출력
select P.pubName, BS.bsDate, B.bookName, BS.bsQty, P.pubName
  from bookdb.booksale BS
    join bookdb.book B
      on BS.bookNo = B.bookNo
    join bookdb.publisher P
      on B.pubNo = P.pubNo
    where pubName = '도서출판 강남';
-- -------------------------------

/* 서브쿼리 연습문제 */

#1. 호날두(고객명)가 주문한 도서의 총구매량 출력
select sum(bsqty) as '총 구매량'
  from Bookdb.booksale BS
  where BS.clientId = (select BC.clientId
                        from bookdb.bookclient BC
                        where BC.clientName = '호날두');

#2. '종로출판사'에서 출간한 도서를 구매한 적이 있는 고객명 출력

select distinct BC.clientName
  from bookdb.bookclient BC
  where BC.clientID = any(select BS.clientID
                      from bookdb.booksale BS
                      where BS.bookNo = any(select B.bookNo
                                        from bookdb.book B
                                        where B.pubNo = (select P.pubNo
                                                        from bookdb.publisher P
                                                        where P.pubName = '종로출판사')));
/*
ERROR 1054 (42S22): Unknown column 'BS.pubNo' in 'where clause'
ERROR 1242 (21000): Subquery returns more than 1 row
*/                                      
#3. 베컴이 주문한 최고 주문수량 보다 더 많은 도서를 구매한 고객명 출력
select BC.clientName
  from bookdb.bookclient BC
  where BC.clientId = any(select BS.clientId
                        from bookdb.booksale BS
                        where BS.bsqty > (select BS.bsqty
                                            from bookdb.booksale BS
                                            where BS.clientID = (select BC.clientID
                                                                  from bookdb.bookclient BC
                                                                  where BC.clientName = '베컴')
                                            order by BS.bsqty desc
                                            limit 1));

/*
ERROR 1064 (42000): You have an error 
in your SQL syntax; check the manual that corresponds to your MySQL server version 
for the right syntax to use near 'in(select BS.clientId' at line 3

ERROR 1064 (42000): You have an error in your SQL syntax; 
check the manual that corresponds to your MySQL server version for 
the right syntax to use near 'decs' at line 10


*/

#4. 서울에 거주하는 고객에게 판매한 도서의 총 판매량 출력
select sum(BS.bsqty) as '총 판매량'
  from bookdb.booksale BS
  where clientID = any(select BC.clientID
                        from bookdb.bookclient BC
                        where BC.ClientAddress = '서울');
#5. '정보출판사'에서 출간한 도서를 구매한 적이 있는 고객명 출력
select distinct BC.clientName
  from bookdb.bookclient BC
  where BC.clientID = any(select BS.ClientID
                          from bookdb.booksale BS
                          where BS.bookNo = any(select B.bookNo
                                                from bookdb.book B
                                                where B.pubNo = (select P.pubNo
                                                                  from bookdb.publisher P
                                                                  where P.pubName = '정보출판사')));
