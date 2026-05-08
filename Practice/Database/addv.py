import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS college
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
c.execute("INSERT INTO college VALUES(?,?,?)", (1, 'Raju', 20))
conn.commit()
conn.close()
