listaA = []
listaB = []
listaC = []

for i in range(19):
    listaA.append(float(input("Digite um número para a lista A: ")))

for j in range(19):
    listaB.append(float(input("Digite um número para a lista B: ")))

for z in range(19):
    listaC.append(listaA[z] - listaB[z])

print(listaC)