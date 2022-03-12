from cryptography.fernet import Fernet

password = input("Please enter the Password: ")
message = str(password)

key = Fernet.generate_key()
fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

ccrstr = encMessage.decode("utf-8") 

print("original string: ", message)
print("encrypted string: ", ccrstr)

decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)