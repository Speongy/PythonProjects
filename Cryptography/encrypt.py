from cryptography.fernet import Fernet

key = Fernet.generate_key()                 #generate key
with open('filekey.key', 'wb') as filekey:  #string key into file
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()                    #open key

fernet = Fernet(key)                        #generated key

with open('pass.txt', 'rb') as f:           #open file to encrypt
    original = f.read()
    

encrypted = fernet.encrypt(original)        #encrypt

with open('pass.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

