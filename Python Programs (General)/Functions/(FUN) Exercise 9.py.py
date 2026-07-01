def somapar(numero):
    somadosnumeros = 0
    for i in range(1,numero):
        if i % 2 == 0:
            somadosnumeros += i
    return somadosnumeros

numero = int(input("DIGITE UM NÚMERO: "))

print(somapar(numero))