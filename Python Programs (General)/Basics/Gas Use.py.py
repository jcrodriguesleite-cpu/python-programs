dist = float(input("Digite a distância percorrida em KM: "))
combus = float(input("Digite os litros de combustível gastos: "))
plitro = float(input("Digite o preço do litro de combustível: \n"))

kmporl = dist/combus

print(f"Consumo em KM/L: {kmporl}")
print(f"Custo da viagem: {combus * plitro}")

