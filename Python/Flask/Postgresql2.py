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
        cls.con = psycopg2.connect("dbname = Jks_try1 user=postgres password=Finserv@2023")
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

# Now we run a loop to get the user input and perform the operations on the database accordingly using the above class methods. 

if __name__ == '__main__':
    while True:
        print(" 1. Create Table ")
        print(" 2. Insert Data ")
        print(" 3. Select Data ")
        print(" 4. Update Data ")
        print(" 5. Delete Data ")
        print(" 6. Exit ")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            table_name = input("Enter table name: ")
            v1 = input("Enter column 1 name: ")
            v2 = input("Enter column 2 name: ")
            v3 = input("Enter column 3 name: ")
            DB_Connection.connect_bds()
            DB_Connection.create_table(table_name,v1,v2,v3)
            DB_Connection.close_connection()
        elif choice == 2:
            table_name = input("Enter table name: ")
            v1 = int(input("Enter value 1: "))
            v2 = input("Enter value 2: ")
            v3 = input("Enter value 3: ")
            DB_Connection.connect_bds()
            DB_Connection.insert_data(table_name,v1,v2,v3)
            DB_Connection.close_connection()
        elif choice == 3:
            table_name = input("Enter table name: ")
            DB_Connection.connect_bds()
            DB_Connection.select_values(table_name)
            DB_Connection.close_connection()
        elif choice == 4:
            table_name = input("Enter table name: ")
            v1 = input("Enter column 1 name: ")
            v2 = input("Enter column 2 name: ")
            v3 = input("Enter column 3 name: ")
            DB_Connection.connect_bds()
            DB_Connection.update_values(table_name,v1,v2,v3)
            DB_Connection.close_connection()
        elif choice == 5:
            table_name = input("Enter table name: ")
            v1 = input("Enter column 1 name: ")
            v2 = input("Enter column 2 name: ")
            DB_Connection.connect_bds()
            DB_Connection.delete_values(table_name,v1,v2)
            DB_Connection.close_connection()
        elif choice == 6:
            break
        else:
            print("Invalid Choice")
