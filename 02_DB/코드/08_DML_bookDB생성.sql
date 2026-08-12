create database bookdb;

use bookdb;
create table publisher(
	pubNo varchar(10) primary key not null,
    pubName varchar(20)
);

insert into publisher (pubNo, pubName) values (1, '서울 출판사'),
												(2, '도서출판 강남'),
                                                (3, '정보출판사');

desc book;


alter table book modify bookNo varchar(10) primary key not null;
alter table book modify bookName varchar(20);
alter table book modify bookAuthor varchar(30);
alter table book modify bookprice int;
alter table book modify bookDate Date;
alter table book modify bookStock int;
alter table book modify pubNo varchar(10) not null;

alter table book add
	constraint FK_book_pubNo foreign key(pubNo) references publisher(pubNo);
    

desc bookClient;

alter table bookClient modify clientNo varchar(10) primary key not null;
alter table bookClient modify clientName varchar(30);
alter table bookClient modify clientPhone varchar(13);
alter table bookClient modify clientAddress varchar(50);
alter table bookClient modify clientBirth Date;
alter table bookClient modify clientHobby varchar(30);
alter table bookClient modify clientGender varchar(1);

desc bookSale;

alter table bookSale modify bsNo varchar(10) primary key not null;
alter table bookSale modify bsDate Date;
alter table bookSale modify bsQty int;
alter table bookSale modify clientNo varchar(10) not null;
alter table bookSale modify bookNo varchar(10) not null;

alter table bookSale add
	constraint FK_bookSale_clintNo foreign key(clientNo) references bookClient(clientNo);
alter table bookSale add
	constraint FK_bookSale_bookNo foreign key(bookNo) references book(bookNo);

/*
17:33:01	alter table book modify bookData Date
Error Code: 1054. Unknown column 'bookData' in 'book'	0.000 sec

17:34:05	alter table bookClient modify clientGener varchar(1)
Error Code: 1054. Unknown column 'clientGener' in 'bookclient'	0.000 sec

17:35:23	alter table bookClient modify clientGeder varchar(1)
Error Code: 1054. Unknown column 'clientGeder' in 'bookclient'	0.000 sec

17:36:41	alter table bookSale modify clintNo varchar(10) not null
Error Code: 1054. Unknown column 'clintNo' in 'booksale'	0.000 sec

17:37:20	alter table bookSale add  constraint FK_bookSale_clintNo foreign key(clintNo) references bookClient(clintNo)\
Error Code: 1072. Key column 'clintNo' doesn't exist in table	0.000 sec

*/
