lista = []
try:
    for i in range(1,50):
        lista.append(float(input(f"Digite a nota do aluno {i}: ")))
except ValueError:
    print("Digite uma nota válida. ")
soma = sum(lista)
qtd = len(lista)

print(soma/qtd)