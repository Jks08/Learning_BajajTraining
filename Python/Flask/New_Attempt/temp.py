import psycopg2

con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
cur = con.cursor()

cur.execute("SELECT * FROM pet_regs")
data = cur.fetchall()
print(data)