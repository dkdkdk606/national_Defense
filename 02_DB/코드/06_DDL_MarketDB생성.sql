create schema marketdb;

use marketdb;


create table membertype(
	membertype_id int primary key not null,
    membertype varchar(5) not null
--     constraint PK_membertype_membertype_id
-- 		primary key membertype(membertype_id)
);

create table customer(
	customer_id int primary key not null,
    customer_name varchar(45),
    birthday	date,
    membertype_id int not null,
    constraint FK_customer_membertype_id
		foreign key(membertype_id)
        references membertype (membertype_id)
);

create table product(
	product_id	int primary key not null,
    product_name varchar(20) not null,
    stock	int default 0 not null,
    price	int default 0 not null

);

create table prodoctorder(
	order_id int primary key not null,
    customer_id int not null,
    product_id int not null,
    quantity int,
    price int,
    order_time datetime,
    constraint FK_prodoctorder_customer_id foreign key(customer_id) references customer(customer_id),
    constraint FK_prodoctorder_product_id foreign key(product_id) references product(product_id)
);






/*
15:14:41	
create table product(  product_id int,     product_name varchar(20),     
stock int,     price decimal(100)  )	
Error Code: 1426. Too-big precision 100 specified for 'price'. Maximum is 65.	0.000 sec

15:25:54	create table customer(  customer_id int primary key not null,     customer_name varchar(45), 
    birthday date,     membertype_id int not null,    
    constraint FK_customer_membertype_id foreign key(membertype_id) references membertype(membertype_id) )	
    Error Code: 1824. Failed to open the referenced table 'membertype'	0.000 sec


*/









