def inverterordemnumero():
    numero = str(input("Digite um número para inverte-lo: "))
    numeroinvertido = numero[::-1]
    for numeros in numeroinvertido:
        print(numeros,end="")

inverterordemnumero()