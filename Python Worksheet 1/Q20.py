lista = []
cont = 1
while True:
        try:
            lista.append(int(input(f"Digite o {cont} número: ")))
            cont += 1
            if lista[-1] == 0:
                print("Número 0 digitado! Terminando a contagem e fazendo média.\n ")
                break
        except ValueError:
                print("Digite um valor válido!")
                continue

soma = sum(lista)
qtd = len(lista)
print(f"SOMA TOTAL: {soma}")
print(f"MÉDIA: {soma/qtd:.2f} ")