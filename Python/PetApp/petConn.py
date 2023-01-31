import psycopg2

class DBconnect:
    con = None
    cur = None

    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        cls.con = psycopg2.connect("dbname=Flask_things user=postgres password=Finserv@2023")
        cls.cur = cls.con.cursor()

    @classmethod
    def disp(cls):
        cls.cur.execute("SELECT * FROM pets_regs1")
        rows = cls.cur.fetchall()
        return rows



    @classmethod
    def latest(cls):
        cls.cur.execute("SELECT * FROM pets_regs1 WHERE CTID = (SELECT MAX(CTID) FROM pets_regs1);")
        rows = cls.cur.fetchall()
        return rows

    @classmethod
    def insert(cls,name='lorem',age='ipsum',type='dolor',ownerName="noname",ownerAddress="noaddress"):
        cls.cur.execute(f"INSERT into pets_regs1 values ('{name}','{age}','{type}','{ownerName}','{ownerAddress}')")
        cls.con.commit()

    @classmethod
    def delete(cls,name):
        cls.cur.execute(f"DELETE FROM pets_regs1 WHERE namepet='{name}'")
        # print('This is meant to delete.')
        cls.con.commit()

    @classmethod
    def update(cls,name,age,type,ownerName,ownerAddress):
        cls.cur.execute(f"UPDATE pets_regs1 SET age='{age}',typepet='{type}',ownerName='{ownerName}',ownerAddress='{ownerAddress}' WHERE namepet='{name}'")
        cls.con.commit()

    @classmethod
    def close(cls):
        cls.con.close()
        print('Closed the connection.')