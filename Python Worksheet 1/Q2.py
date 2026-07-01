alturapessoa = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo [M/F]: ")

if sexo == "M":
    pesoideal = (72.7 * alturapessoa) - 58
else:
    pesoideal = (61,1 * alturapessoa) - 44.7

print(f"PESO IDEAL: {pesoideal:.2f} ")

