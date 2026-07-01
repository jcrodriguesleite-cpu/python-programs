try:
    try:
        numero1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))

    except ValueError:
        print("DIGITE UM VALOR VÁLIDO.")
    try:
        numero2 = int(input("DIGITE O SEGUNDO NÚMERO: "))

    except ValueError:
        print("DIGITE UM VALOR VÁLIDO.")

    divisao = numero1/numero2
    print(divisao)

except ZeroDivisionError:
    print("Divisão por zero não é válida!")

