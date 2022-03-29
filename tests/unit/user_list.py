import sqlite3 as sql

con = sql.connect("./db/users.db")
c = con.cursor()

c.execute("SELECT name FROM users")
users = c.fetchall()
user_list_mapped = '\n'.join(map(str, users))
user_list = user_list_mapped.replace("(", "").replace(")", "").replace("'", "").replace(",", "")
print(user_list)
