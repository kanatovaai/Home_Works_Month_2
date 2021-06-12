create table products (
id integer, name text, price integer, amount integer, manufacture_date text
);

insert into products values (1, 'Bananas', 10, 6, '20.05.2021');
insert into products values (2, 'Apple', 70, 8, '19.05.2021');
insert into products values (3, 'Milk', 40, 1, '24.05.2021');

delete from products where id = 2;

update products set name = 'Soy milk' where id = 3;
update products set price = 100 where id = 1;

select * from products order by id;

select name, price, amount from products;
