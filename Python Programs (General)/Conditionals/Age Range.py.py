nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 7:
    print("Adolescente")
elif idade >= 18 and idade <=59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")