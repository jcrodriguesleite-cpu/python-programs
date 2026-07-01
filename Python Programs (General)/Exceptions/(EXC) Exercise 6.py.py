while True:
    try:
        usuario = input("DIGITE O USUÁRIO:  ")
        senha = input("DIGITE A SENHA:  ")
        if usuario == "admin" and senha == "1234":
            print("Acesso Permitido.")
            break
        else:
            print("Login ou Senha incorretos.")
    except:
        print("Erro na entrada de dados.")
