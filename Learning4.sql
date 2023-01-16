/*insert into teachers values 
(002,'jishnu','sriv','DPS','2001-08-18',60000),
(003,'parkul','singh','SRM','2001-05-31',120000),
(004,'sparsh','agar','NGO','2001-02-28',50000),
(005,'prakash','yada','SUPRK','2001-12-02',200000);
*/
-- select * from teachers where school='don bosco';
-- select * from teachers where school<>'don bosco';
-- select * from teachers where salary<>20000;
-- select * from teachers where salary<80000;
-- select * from teachers where salary between 55000 and 200000;
-- select * from teachers where lname in ('sriv','bhatta','singh','yada') and salary>70000;
-- select * from teachers where school<>'SRM' and (salary<35000 or salary>50000);
-- select * from teachers where lname like 's%' or lname like 'b%';

-- select fname,lname,school from teachers order by school asc,lname asc;

-- select * from teachers where fname like 's%' and salary>40000

-- select * from teachers where hire_date>'2001-01-01' order by salary desc;