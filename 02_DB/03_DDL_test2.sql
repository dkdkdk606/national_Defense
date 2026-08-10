use testdb2;

create table professor(
	proNo int primary key,
    proName varchar(20),
    proRank varchar(40),
    proPhone varchar(40),
    dptNo int,
    constraint Fk_professor_department foreign key(dptNo) references department(dptNo)
);

create table course(
	couNo int primary Key,
    couName varchar(40),
    couScore float,
    proNo int

);

