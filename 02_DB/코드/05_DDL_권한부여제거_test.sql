use testdb2;

create table testdb2.test(
	id int not null primary key,
    content varchar(100)
);

select * from testdb2.test;