lista = []
contador = 0
while contador <= 4:
    try:
        contador += 1
        lista.append(float(input("DIGITE UM NÚMERO: ")))
    except ValueError:
        print("Digite valores válidos.")

print(f"VALORES DIGITADOS: {lista}")