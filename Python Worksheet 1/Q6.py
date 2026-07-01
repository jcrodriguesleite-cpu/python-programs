lista1 = []
lista2 = []
for i in range(7):
    lista1.append(int(input("Digite um número: ")))

for j in lista1:
    lista2.append(lista1[j] * 4)

print(lista1)

print(lista2)