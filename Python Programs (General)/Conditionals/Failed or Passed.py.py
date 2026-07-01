nome = str(input("Digite o nome do aluno: "))
n1 = float(input("Digite a nota 1 dele: "))
n2 = float(input("Digite a nota 2 dele: "))
n3 = float(input("Digite a nota 3 dele: "))

if ((n1+n2+n3/3)) >= 7:
    print(f"{nome} foi aprovado")
else:
    print(f"{nome} foi reprovado")