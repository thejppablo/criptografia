import hasher
import hash_salt

funcoes = {"1": hasher.register_user, "2": hash_salt.register_user_salt}

start = True
while start:
    choice = input("registrar usuario de que forma? ")
    if choice == "3":
        start = False
    else:
        funcoes[choice]()
