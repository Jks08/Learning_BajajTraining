-- create table emptable(empcode varchar(20),empname text,age int,designation text,emplocation text);
/*insert into emptable values ('E001','JKS',21,'Intern','Pune'),
('E002','PS',21,'Intern','Pune'),('E003','AB',21,'Intern','Pune'),('E004','PY',21,'Intern','Pune'),
('E005','SA',21,'Intern','Pune');*/
-- create view EmptableView as select empcode,designation,emplocation from emptable;
-- delete from EmptableView where empcode='E001';
-- select * from emptable, EmptableView;
-- delete from emptable where empcode='E002';
-- select * from emptable, EmptableView;
-- update emptable set designation='CEO' where empcode='E003';
-- select * from emptable, EmptableView;
-- create view qview as select * from emptable where emplocation='Mumbai' or emplocation='Pune';
-- select * from qview;