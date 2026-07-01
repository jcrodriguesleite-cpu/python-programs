while True:
    login = input("USUÁRIO: ")
    senha = input("SENHA: ")
    if login == "admin" and senha == "1234":
        print("Acesso permitido.")
        break
    else:
        print("Acesso negado.")
        continue