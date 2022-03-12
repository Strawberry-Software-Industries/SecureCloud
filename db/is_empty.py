import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("SELECT * FROM users")
exist = c.fetchone()

print(exist)
if exist is None:
    print("Val 0")
else:
    print("Val 1")