-- Create table emp_data(name varchar(30), address text);
-- insert into emp_data values ('Rahul','Pune'), ('Ram','Mumbai');
-- copy emp_data to '/tmp/emp.txt' with (format csv,header,delimiter '|');
-- copy emp_data from '/tmp/emp.txt' with (format csv,header,delimiter '|');
-- select fname from teachers where salary = (select max(salary) from teachers);
-- select * from teachers;
-- select * from emp;
-- create view emp_view as select * from emp;

/* New */

-- create table licenses(license_id varchar(20),fname varchar(20),lname varchar(20), constraint license_key primary key(license_id));
-- create table registrations(registration_id varchar(20), registration_date date,license_id varchar(20) references licenses(license_id),constraint registration_key primary key(registration_id,license_id));

-- insert into licenses(license_id,fname,lname) values ('T229901','Lynn','Malero');
-- insert into registrations(registration_id,registration_date,license_id) values ('A203391','2017-03-17','T229901');
-- select * from licenses, registrations;

-- select registration_date,registrations.license_id from registrations,licenses where registrations.license_id=licenses.license_id;

/*create table check_constraint_demo
(user_id serial,user_role varchar(20),
 salary int,
 constraint user_id_key primary key(user_id),
 constraint check_role_in_list check(user_role in ('Admin','Staff')), constraint check_salary_not_zero check(salary>0)
);
*/