try:
    numero = int(input("DIGITE UM NÚMERO INTEIRO: "))

except ValueError:
    print("Digite um número válido! ")
except TypeError:
    print("Símbolos ou palavras não são permitidos! ")