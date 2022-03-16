import sqlite3

conn = sqlite3.connect('./db/users.db')
c = conn.cursor()
c.execute('DELETE FROM user;',);			
conn.commit()
conn.close()
