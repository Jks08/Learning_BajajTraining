import psycopg2
from config import table_name,accessDBname,userDB,passwordDB
from logger import logger

class DBconnect:
    con = None
    cur = None
    # c = Config()
    # table_name = c.table()
    # dbname = c.db()
    # userDB = c.user()
    # passwordDB = c.password()

    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        cls.con = psycopg2.connect(f"dbname={accessDBname} user={userDB} password={passwordDB}")
        cls.cur = cls.con.cursor()
        logger.info("Connected to the database")

    @classmethod
    def disp(cls):
        cls.cur.execute(f"SELECT * FROM {table_name}")
        rows = cls.cur.fetchall()
        logger.info("Data displayed")
        return rows

    @classmethod
    def latest(cls):
        cls.cur.execute(f"SELECT * FROM {table_name} WHERE CTID = (SELECT MAX(CTID) FROM {table_name});")
        rows = cls.cur.fetchall()
        logger.info("Latest data displayed")
        return rows

    @classmethod
    def insert(cls,name='lorem',age='ipsum',type='dolor',ownerName="noname",ownerAddress="noaddress"):
        cls.cur.execute(f"INSERT into {table_name} values ('{name}','{age}','{type}','{ownerName}','{ownerAddress}')")
        cls.con.commit()
        logger.info("Data inserted")

    @classmethod
    def delete(cls,name):
        cls.cur.execute(f"DELETE FROM {table_name} WHERE namepet='{name}'")
        # print('This is meant to delete.')
        cls.con.commit()
        logger.info("Data deleted")

    @classmethod
    def update(cls,name,age,type,ownerName,ownerAddress):
        cls.cur.execute(f"UPDATE {table_name} SET age='{age}',typepet='{type}',ownerName='{ownerName}',ownerAddress='{ownerAddress}' WHERE namepet='{name}'")
        cls.con.commit()
        logger.info("Data updated")

    @classmethod
    def close(cls):
        cls.con.close()
        print('Closed the connection.')
        logger.info("Connection closed")