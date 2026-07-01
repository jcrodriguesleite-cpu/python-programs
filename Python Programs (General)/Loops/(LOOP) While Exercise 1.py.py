print("Olá! Esse programa lê números e os soma no final. Se deseja parar o programa, digite 0 em qualquer leitura.")
num = 0
contador = 1
soma = 0
while contador != 0:
    num = int(input(f"Digite o {contador}º número: "))
    contador += 1
    soma += num
    if num == 0:
        print(f"Você escolheu finalizar a operação!\nO resultado da soma é: {soma}")
        contador == 0
