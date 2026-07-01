lista = [1,8,9,10,53,14,74]

while True:
    try:
        posicao = int(input("DIGITE O ÍNDICE DE UM ELEMENTO DA LISTA: "))
        print(lista[posicao])
    except IndexError:
        print("Esse índice não existe.")
    else:
        break