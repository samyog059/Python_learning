import sqlite3
conn = sqlite3.connect('college.db')
print("Database Connected")
conn.close()
print("Database Closed")