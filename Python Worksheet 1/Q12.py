lista = []
contiguais = 0
for i in range(9):
    lista.append(int(input("Digite um número: ")))

for numero in set(lista):
    contiguais += lista.count(numero) - 1

print(f"Existem {contiguais} repetições de números")
