rainbow_table = {
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8":  "password",
    "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92":  "123456",
    "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5":  "12345",
          }
def recover_data():
    f = open("database.txt")
    conteudo = f.readlines()
    recovered_hash = []
    for x in conteudo:
        for y in x:
            if y ==":":
                position = x.index(y)
                recovered_pass = x[position+1:]
                recovered_hash.append(recovered_pass)

    for z in recovered_hash:
        position = recovered_hash.index(z)
        recovered_hash[position] = z[:64]

    return recovered_hash

def check_pass(hash_list, rainbow):
    for hash in hash_list:
        if hash in rainbow:
            print("Há hashes compatíveis. Senhas descobertas: ", rainbow[hash])
        else:
            print("não tem")
            return

recovered = recover_data()
check_pass(recovered, rainbow_table)


