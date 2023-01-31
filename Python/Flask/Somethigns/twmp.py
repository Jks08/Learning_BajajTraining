import psycopg2

class DBconnect:
    con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
    cur = con.cursor()
    @classmethod
    def disp(cls):
        cls.cur.execute("SELECT * FROM pet_regs")
        rows = cls.cur.fetchall()
        return rows


print(DBconnect.disp())