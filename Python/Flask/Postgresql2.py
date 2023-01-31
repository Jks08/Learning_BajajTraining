import psycopg2
from flask import *

class Student:
    def __init__(self, sid, sname, saddr):
        self.sid = sid
        self.sname = sname
        self.saddr = saddr

class DB_Connection:
    con = None
    cur = None

    def __init__(self):
        pass

    @classmethod
    def connect_bds(cls):
        cls.con = psycopg2.connect("dbname = Tutorial1 user=postgres password=Finserv@2023")
        cls.cur = cls.con.cursor()

    @classmethod
    def create_table(cls,table_name,v1,v2,v3):
        cls.cur.execute("create table {} ({} integer, {} varchar, {} varchar);".format(table_name,v1,v2,v3))
        cls.con.commit()

    @classmethod
    def insert_data(cls,table_name,v1,v2,v3):
        cls.cur.execute(f"insert into {table_name} values ({v1},'{v2}','{v3}');")
        cls.con.commit()

    @classmethod
    def select_values(cls,table_name):
        cls.cur.execute(f"select * from {table_name};")
        students = cls.cur.fetchall()
        for i in students:
            print(i)

    @classmethod
    def update_values(cls,table_name,v1,v2,v3):
        cls.cur.execute(f"update {table_name} set {v2} = '{v3}' where {v1} = {v3};")
        cls.con.commit()

    @classmethod
    def delete_values(cls,table_name,v1,v2):
        cls.cur.execute(f"delete from {table_name} where {v1} = {v2};")
        cls.con.commit()

    @classmethod
    def close_connection(cls):
        cls.con.close()
        cls.cur.close()

# Now we take user inputs and call the functions. 

if __name__ == '__main__':
    DB_Connection.connect_bds()
    # DB_Connection.create_table('student','sid','sname','saddr')
    # DB_Connection.insert_data('student',1,'jks','chem')
    # DB_Connection.insert_data('student',2,'ab','chem')
    # DB_Connection.insert_data('student',3,'sa','chem')
    # DB_Connection.insert_data('student',4,'pky','chem')
    # DB_Connection.insert_data('student',5,'ps','chem')
    # DB_Connection.select_values('student')
    # DB_Connection.update_values('student','sname','jks','jks1')
    # DB_Connection.select_values('student')
    # DB_Connection.delete_values('student','sid',1)
    # DB_Connection.select_values('student')
    DB_Connection.close_connection()