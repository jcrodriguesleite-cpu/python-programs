def faixaetaria(idade):
    if idade <= 13:
        return "Criança"
    elif idade > 13 and idade < 18:
        return "Adolescente"
    elif idade >= 18 and idade < 60:
        return "Adulto"
    else:
        return "Idoso"

idade = int(input("Digite sua idade: "))

print(faixaetaria(idade))
