numeros = []
while True:
    try:
        numero = float(input("DIGITE UM NÚMERO: "))
        if numero == 0:
            print("Encerrando!")
            break
    except ValueError:
        print("Digite um valor válido.")
    else:
        numeros.append(numero)

print("Os números digitados foram: ")
print(numeros)