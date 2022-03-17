import sqlite3 as sql
from Cryptodome.Hash import SHAKE256
username = input("Username: ")
password = input("Password: ")

byte_pw = str.encode(password)

Hashed_Password = SHAKE256.new()
Hashed_Password.update(byte_pw)

conn = sql.connect("D:/Projekte/SecureCloud/db/users-hashed.db")
conn.execute(f"INSERT INTO users (name,password) VALUES ('{username}', '{Hashed_Password.read(26).hex()}')")
conn.commit()
conn.close()

print("Values has been inserted to the Database")
