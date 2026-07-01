# Perguntas de nome, quantidade e preço do produto

nomep1 = str(input("Diga o nome do produto 1: "))
quanp1 = float(input("Diga o peso do produto 1 em Kg:  "))
preçop1 = float(input("Diga o preço do produto 1 em reais: R$ "))

nomep2 = str(input("Diga o nome do produto 2: "))
quanp2 = float(input("Diga o peso do produto 2 em Kg: "))
preçop2 = float(input("Diga o preço do produto 2 em reais: R$ "))

nomep3 = str(input("Diga o nome do produto 3: "))
quanp3 = float(input("Diga o peso do produto 3 em Kg: "))
preçop3 = float(input("Diga o preço do produto 3 em reais: R$ "))

#Resultados

print(f"{nomep1}: {quanp1:.0} x R$ {preçop1} = R${quanp1 * preçop1}")
print(f"{nomep2}: {quanp2:.0} x R$ {preçop2} = R${quanp2 * preçop2}")
print(f"{nomep3}: {quanp3:.0} x R$ {preçop3} = R${quanp3 * preçop3}")