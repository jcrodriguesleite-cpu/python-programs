lista = []
cont = 1
while cont <= 20:
    lista.append(int(input(f"Digite o {cont}º número: ")))
    cont += 1
print(min(lista))
print(max(lista))