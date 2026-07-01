quant = int(input("Digite a quantidade de números que deseja calcular a média: "))
soma = 0
for i in range(1,quant+1):
    num = float(input(f"Digite o {i}º número: "))
    if num > 10:
        i = quant + 1
        print("Você não pode digitar um valor maior que 10!")
    soma += num

med = soma/quant
print(f"{med:.2f}")

if med >= 7:
    print("Parabéns! Você foi aprovado!")
else:
    print("Você está de recuperação.")