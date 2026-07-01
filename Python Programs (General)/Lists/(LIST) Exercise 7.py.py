lista = []
for i in range(5):
    lista.append(float(input("Digite um número: ")))

print(lista)
print(f"MÁXIMO: {max(lista)}")
print(f"MÍNIMO: {min(lista)}")
soma = sum(lista)
qtdtermos = len(lista)
media = soma/qtdtermos
print(f"MÉDIA: {media}")