# FOR EDUCATIONAL USE ONLY

import os
from cryptography.fernet import Fernet


files = []

pwd = os.getcwd()

#   Fernet Setup

with open("Maple.key", "rb") as key:
    secret = key.read()


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
    decrypted = Fernet(secret).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted)

