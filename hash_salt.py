import uuid
import hashlib
import os
from hasher import write_to_file

def parar(parm):
    parm = False

def hash_salt_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def register_user_salt():
    user = input("enter username: ")
    new_pass = input('Please enter a password: ')
    hashed_password = hash_salt_password(new_pass)
    filesize = os.path.getsize("database.txt")
    if filesize < 1:
        final_write = user + ":" + hashed_password
        write_to_file("database.txt",final_write)
    else:
        final_write = " \n" + user + ":" + hashed_password
        write_to_file("database.txt", final_write)

