import sqlite3 as sql
from cryptography.fernet import Fernet

conn = sql.connect('users-encrypted.db')
c = conn.cursor()

username = input("Username: ")
password = input("Password: ")

c.execute('SELECT * FROM users WHERE name = ? AND password = ?', (username, password))
encMessage = c.fetchone()
print(encMessage)
key = Fernet.generate_key()
fernet = Fernet(key)
decMessage = fernet.decrypt(encMessage).decode()
encryptedPw = encMessage.decode("utf-8") 

print(decMessage)

c.execute('SELECT * FROM users WHERE name = ? AND password = ?', (username, password))

if c.fetchall():
    print(f'Logged in')


else:
    print(f'Wrong Username or Password')
    