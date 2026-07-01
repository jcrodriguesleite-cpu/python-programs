def fatorialwhile_e_for():
    numero = int(input("(FOR) Digite um número: "))
    resultado = 1

    for i in range(1,numero + 1):
        resultado *= i

    print(resultado)


    numero2 = int(input("(WHILE) Digite um número: "))

    contador = 1
    resultado2 = 1
    while contador <= numero2:
        resultado2 *= contador
        contador += 1

    print(resultado2)

fatorialwhile_e_for()























