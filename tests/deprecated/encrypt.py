import sqlite3 as sql
from cryptography.fernet import Fernet

username = input("Username: ")
password = input("Password: ")
pw = str(password)
uname = str(username)

key = Fernet.generate_key()
fernet = Fernet(key)

encMessage = fernet.encrypt(pw.encode())

encryptedPw = encMessage.decode("utf-8") 

print("original string: ", pw)
print("encrypted string: ", encryptedPw)

decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)

conn = sql.connect('users-encrypted.db')
conn.execute(f"INSERT INTO users (name,password) VALUES ('{uname}', '{encryptedPw}')")
conn.commit()
conn.close()
