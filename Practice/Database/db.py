import sqlite3
conn = sqlite3.connect('college.db')
cur=conn.cursor()  
cur.execute("""CREATE TABLE student(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL)
""")
conn.commit()
print("Table created successfully")
conn.close()
# show table content
conn = sqlite3.connect('college.db')
cur=conn.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)