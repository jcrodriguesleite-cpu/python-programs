nome = str(input("Digite o nome do produto: "))
preço = float(input("Digite o preço do produto: "))
percdesconto = float(input("Digite o percentual de desconto em %: "))
print(f"O {nome} com desconto de {percdesconto}% fica {preço * (1-(percdesconto/100))}")