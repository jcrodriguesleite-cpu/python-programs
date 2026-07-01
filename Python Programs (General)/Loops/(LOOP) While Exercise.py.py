senha = 345
contador = 0
while contador == 0:
    entrada = int(input("Digite a senha: "))
    if entrada == senha:
        print("Entrada permitida! Bem vindo!")
        contador = 1
    else:
        print("Entrada recusada. Senha errada.")
