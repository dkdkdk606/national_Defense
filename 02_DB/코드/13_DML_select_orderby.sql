/*
정렬 ORDER BY [ASC|DESC]

- 특정한 열의 값을 기준으로 질의 결과 정렬
- 가장 마지막에 수행
- 형식
	SELECT FROM WHERE GROUP BY HAVING ORDER BY

	ORDER BY 컬럼이름 [ASC|DESC]
    ASC : 오름차순, 기본값으로 생략 가능
    DESC : 내림차순
*/

# 도서이름 순으로 도서 조회(도서이름 오름차순)

select * from bookdb.book order by bookName;
# 정렬기준 : 숫자(0->9) -> 알파벳(a->z) -> 한글(ㄱ->ㅎ)
select * from bookdb.book order by bookName DESC ;


insert into boodb.book values ('1016', 'k소문자실험', '1', '1000', '2021-12-12', '3', '1');

# 출력 개수 제한 : limite
#	limit : 출력 레코드 수 지정
select * from bookdb.book order by bookDate desc limit 5;

#	limit offset '시작위치' : 시작 위치 '시작위치'+1 번째 부터로 변경
select * from bookdb.book order by bookDate desc limit 5 offset 3;

#	limit 시작, 개수
select * from bookdb.book order by bookDate desc limit 5 , 3;
# 기준 없이도 가능
select * from bookdb.book limit 5 offset 3;

#정렬의 조건을 두개 이상 지정
#	재고수량을 기준으로 내림차순 정렬, 재고수량이 동일한 경우 최근발행일 순으로 지정
select * from bookdb.book
	order by bookStock DESC, bookDate DESC;













































