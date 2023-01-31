import psycopg2

class DBConn:
    conn = None
    curr = None

    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        cls.conn = psycopg2.connect("dbname=Jks_try1 user=postgres password=Finserv@2023")
        cls.curr = cls.conn.cursor()

    @classmethod
    def create_table(cls):
        cls.curr.execute("CREATE TABLE IF NOT EXISTS pet_regs (name varchar(20), age varchar(20), type varchar(20), ownerName varchar(20), ownerAddress varchar(20));")
    
    @classmethod
    def view_data(cls):
        cls.curr.execute("SELECT * FROM pet_regs")
        rows = cls.curr.fetchall()
        return rows

    @classmethod
    def insert_data(cls,name,age,type,ownerName,ownerAddress):
        cls.curr.execute("INSERT INTO pet_regs (name,age,type,ownerName,ownerAddress) VALUES (%s,%s,%s,%s,%s)",(name,age,type,ownerName,ownerAddress))
        cls.conn.commit()

    @classmethod
    def update_data(cls,name,age,type,ownerName,ownerAddress):
        cls.curr.execute("UPDATE pet_regs SET age=%s,type=%s,ownerName=%s,ownerAddress=%s WHERE name=%s",(age,type,ownerName,ownerAddress,name))
        cls.conn.commit()

    @classmethod
    def delete_data(cls,name):
        cls.curr.execute("DELETE FROM pet_regs WHERE name=%s",(name,))
        cls.conn.commit()

    @classmethod
    def close(cls):
        cls.curr.close()
        cls.conn.close()