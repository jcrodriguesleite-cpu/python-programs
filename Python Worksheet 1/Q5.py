lista = []
while True:
    lista.append(float(input("Digite um número: ")))
    if lista[-1] == 999:
        break
soma = sum(lista)
media = soma/len(lista)
print(soma)
print(media)