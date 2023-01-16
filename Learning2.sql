-- create table student(roll_no int primary key, sname varchar(10), address varchar(30),contact_no bigint,age int);
-- select * from student;
/* insert into student values 
(100,'jks','ggn',9599584756,21),
(101,'pks','ggn',9799586796,14),
(102,'ab','kkr',9599434756,21),
(103,'sa','up',7599534756,21),
(104,'pky','up',6500584756,21),
(105,'ps','up',7043584756,21),
(106,'sr','lky',9599586403,20),
(107,'ab','krl',7431084756,20),
(108,'as','kkr',9569584707,21),
(109,'gvda','blr',7400583756,22),
(110,'bgt','bhp',8733410483,22);*/

-- select sname,address from student order by roll_no;
-- select sname,address from student order by roll_no desc;
-- select roll_no as code from student;

--create table stud_details(roll_no int primary key, branch varchar(10), grade varchar(5));

/*insert into stud_details values 
(100,'pcm','A'),
(101,'scs','B'),
(102,'pcmb','A'),
(103,'pcme','C'),
(104,'hum','A'),
(105,'phy','A'),
(106,'art','B'),
(107,'psy','D'),
(108,'pcmcs','B'),
(109,'psy','A'),
(110,'hoe','B');*/

-- select * from stud_details;

-- select distinct student.sname,stud_details.grade from student, stud_details where student.age=20;
-- insert into student values (111,'dyp','ajk',9577402563,21);
-- select * from student where address ~*'.*[a-c].*';
select * from student;