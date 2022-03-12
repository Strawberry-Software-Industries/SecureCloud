import sqlite3

conn = sqlite3.connect('./db/users.db')
c = conn.cursor()
c.execute('DELETE FROM user;',);			
conn.commit()
conn.close()

#conn = sql.connect('./db/users.db')
#conn.execute(f"INSERT INTO users (name,password) VALUES ('admin', 'python')")
#conn.commit()
#conn.close()

