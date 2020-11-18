import uuid
import hashlib
import os

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def write_to_file(file ,content):
    f = open(file, "a")
    f.write(content)
    f.close()

def register_user():
    user = input("enter username: ")
    new_pass = input('Please enter a password: ')
    hashed_password = hash_password(new_pass)
    filesize = os.path.getsize("database.txt")
    if filesize < 1:
        final_write = user + ":" + hashed_password
        write_to_file("database.txt",final_write)
    else:
        final_write = " \n" + user + ":" + hashed_password
        write_to_file("database.txt", final_write)













