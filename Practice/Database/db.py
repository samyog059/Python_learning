import sqlite3
conn = sqlite3.connect('college.db')
cur=conn.cursor()  
print("Database Connected Successfully")
conn.close()
print("Database Closed")