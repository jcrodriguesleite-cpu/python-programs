numeros = (2,4,6,8,10,7)

soma = 0

for valores in numeros:
    if valores % 2 == 0:
        soma += valores

print(soma)