import psycopg2

con = psycopg2.connect("dbname=Jks_Try1 user=postgres password=Finserv@2023")
cur = con.cursor()
# cur.execute("create table test (id serial primary key, num integer, data varchar);")
# con.commit()

# cur.execute("insert into test (num, data) values (%s, %s)", (100, "abcdef"))
# cur.execute("insert into test (num, data) values (%s, %s)", (110, "gfgdef"))
# con.commit()

# cur.execute("update test set data='chem' where data='abcdef';")
# con.commit()

cur.execute("select * from test;")
print(cur.fetchall())
con.commit()