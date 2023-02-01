import psycopg2
from config import Config

class DBconnect:
    con = None
    cur = None
    c = Config()
    table_name = c.table()
    dbname = c.db()
    userDB = c.user()
    passwordDB = c.password()

    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        cls.con = psycopg2.connect(f"dbname={cls.dbname} user={cls.userDB} password={cls.passwordDB}")
        cls.cur = cls.con.cursor()

    @classmethod
    def disp(cls):
        cls.cur.execute(f"SELECT * FROM {cls.table_name}")
        rows = cls.cur.fetchall()
        return rows

    @classmethod
    def latest(cls):
        cls.cur.execute(f"SELECT * FROM {cls.table_name} WHERE CTID = (SELECT MAX(CTID) FROM {cls.table_name});")
        rows = cls.cur.fetchall()
        return rows

    @classmethod
    def insert(cls,name='lorem',age='ipsum',type='dolor',ownerName="noname",ownerAddress="noaddress"):
        cls.cur.execute(f"INSERT into {cls.table_name} values ('{name}','{age}','{type}','{ownerName}','{ownerAddress}')")
        cls.con.commit()

    @classmethod
    def delete(cls,name):
        cls.cur.execute(f"DELETE FROM {cls.table_name} WHERE namepet='{name}'")
        # print('This is meant to delete.')
        cls.con.commit()

    @classmethod
    def update(cls,name,age,type,ownerName,ownerAddress):
        cls.cur.execute(f"UPDATE {cls.table_name} SET age='{age}',typepet='{type}',ownerName='{ownerName}',ownerAddress='{ownerAddress}' WHERE namepet='{name}'")
        cls.con.commit()

    @classmethod
    def close(cls):
        cls.con.close()
        print('Closed the connection.')