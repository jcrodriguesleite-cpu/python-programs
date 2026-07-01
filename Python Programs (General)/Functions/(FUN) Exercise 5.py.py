def soma(a,b):
    return a + b


def subtracao(a,b):
    return a - b


def multipli(a,b):
    return a * b

def divisao(a,b):
    return a/b

numero1 = int(input("N1: "))
numero2 = int(input("N2: "))
resp = input("QUAL OPERAÇÃO DESEJA FAZER COM ESSES NÚMEROS? \n [D] -> DIVISÃO \n [M] -> MULTIPLICAÇÃO \n [SO] -> SOMA \n [SU] -> SUBTRAÇÃO \n DIGITE AQUI SUA RESPOSTA: ")
if resp == "D":
    print(f"RESULTADO: {divisao(numero1,numero2)}")
elif resp == "SO":
    print(f"RESULTADO: {soma(numero1,numero2)}")
elif resp == "SU":
    print(f"RESULTADO: {subtracao(numero1,numero2)}")
elif resp == "M":
    print(f"RESULTADO: {multipli(numero1,numero2)}")
