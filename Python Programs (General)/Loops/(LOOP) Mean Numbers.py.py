contador = 0
sum = 0
botao = "S"
while botao == "S":
    num = float(input("DIGITE UM NÚMERO: "))
    sum += num
    contador += 1
    botao = input("Deseja continuar? [S/N]: ")
    if botao == "N":
        break
    else:
        continue


média = sum/contador

print(f"MÉDIA: {média:.2f}")