nome = str(input("Digite o nome do funcionário: "))
salario = float(input("Digite o valor do salário do funcionário: "))
percbonus = float(input("Digite o percentual do bônus em %: \n"))

print(f"Funcionário: {nome}\n")
print(f"Salário: {salario}\n")
print(f"Valor do Bônus: {(salario * (1+(percbonus/100))) - salario}\n")
print(f"Salário Final: {salario * (1+(percbonus/100))}")