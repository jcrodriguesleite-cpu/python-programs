def verificar_par(numero):
    if numero % 2 == 0:
        print("Esse número é par.")
    else:
        print("Esse número é impar.")

parouimpar = int(input("Digite o número: "))

verificar_par(parouimpar)