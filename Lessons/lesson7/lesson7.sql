create table students3 (
id integer PRIMARY KEY unique  , name text , surname text, age integer, level integer, course_id integer , foreign key (course_id) references course(id));

create table course (
id integer primary key unique, name text , direction text
);

insert into course values (1, 'GeekTech', 'Python');
insert into course values (2, 'GeekTech', 'frontEnd');

мinsert into students3 values (1, 'kadyr', 'Umarov', 24, 2, 1);
insert into students3 values (2, 'Sher', 'K', 27,  2, 2);
insert into students3 values (3, 'Vladimir', 'Putin', 60,  3 ,1);
insert into students3 values (4, 'Adelya', 'Kojomurayova', 18, 3 , 2);
insert into students3 values (5, 'daniiar', 'm', 21 , 2, 1);

select * from students3 where course_id = 2;

