listanumerosint = []
cont = 1
listanumerosimp = []

while cont <= 50:
    listanumerosint.append(int(input("Digite um número: ")))
    cont += 1
    if (listanumerosint[-1] % 2 != 0) and listanumerosint[-1] >= 100 and listanumerosint[-1] <= 200:
        listanumerosimp.append(listanumerosint[-1])

print(sum(listanumerosimp))
