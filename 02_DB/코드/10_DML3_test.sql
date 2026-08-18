use bookdb;

create table bookdb.customer(
	customer_HP varchar(20) not null
    

);

alter table bookdb.customer add (
	sex varchar(2),
    age int
);

