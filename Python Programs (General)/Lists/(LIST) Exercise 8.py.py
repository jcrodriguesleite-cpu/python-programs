lista = []
while True:
    lista.append(float(input("Digite um número [0 para cancelar]: ")))
    if lista[-1] == 0:
        del lista[-1]
        break
print(f"QTD DE TERMOS DA LISTA: {len(lista)}")
print(f"SOMA TOTAL: {sum(lista)}")
media = sum(lista)/len(lista)
print(f"MÉDIA: {media:.2f}")
for i in range(len(lista)):
    print(f"ÍNDICE: {i}   DADO: {lista[i]}")
