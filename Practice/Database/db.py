import sqlite3
conn=sqlite3.connect('college.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS college
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cur.execute("INSERT INTO college VALUES(1,'John Doe',20)")
cur.execute("INSERT INTO college VALUES(2,'Jane Smith',22)")
conn.commit()
print("Data Inserted")
conn.close()
