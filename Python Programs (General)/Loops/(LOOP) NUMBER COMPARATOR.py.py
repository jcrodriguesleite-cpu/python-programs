contador = 0
sum = 0
numimpares = 0
numpares = 0
while contador < 10:
    num = int(input("DIGITE UM NÚMERO INTEIRO: "))
    sum += num
    if contador == 0:
        menor = num
        maior = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if (num % 2 == 0):
        numpares += 1
    else:
        numimpares += 1
    contador += 1
print(f"SOMA TOTAL: {sum} ")
print(f"MAIOR NÚMERO: {maior}")
print(f"MENOR NÚMERO: {menor}")
print(f"NÚMEROS PARES: {numpares}")
print(f"NÚMEROS IMPARES: {numimpares}")
