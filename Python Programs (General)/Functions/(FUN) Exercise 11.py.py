def contadornumerolista(lista,numero):
    contnumero = 0
    for itens in lista:
        if itens == numero:
            contnumero += 1
    return contnumero

lista = []
while True:
    lista.append(int(input(f"Digite um termo para a lista: ")))
    resp1 = input("DESEJA CONTINUAR? [S/N]: ")
    if resp1 == "S":
        continue
    else:
        break

while True:
    resp2 = input("DESEJA PROCURAR ALGUM NÚMERO NA LISTA? [S/N]: ")
    if resp2 == "S":
        numero = int(input("DIGITE O NÚMERO QUE DESEJA PROCURAR: "))
        print(contadornumerolista(lista,numero))
        break
    else:
        break
    


    