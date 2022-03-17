import sqlite3 as sql
from Cryptodome.Hash import SHAKE256
username = input("Username: ")
password = input("Password: ")

byte_pw = str.encode(password)

Hashed_Password = SHAKE256.new()
Hashed_Password.update(byte_pw)

conn = sql.connect("D:/Projekte/SecureCloud/db/users-hashed.db")
c = conn.cursor()
c.execute('SELECT * FROM users WHERE name = ? AND password = ?', (username, Hashed_Password.read(26).hex()))


if c.fetchall():
    print(f'Welcome {username}')

else:
    print(f'Error: Wrong Username or Password')

