nome = input("Digite seu nome: ")

salario = float(input("Digite o seu salário: R$ "))

numerodependentes = int(input("Digite o número de dependentes: "))




if salario <= 1500:
    inss = 0.92
elif salario >= 1500 and salario <= 3000:
    inss = 0.91
elif salario > 3000:
    inss = 0.89

if salario < 2000:
    irrf = 0
elif salario >= 2000 and salario < 3500:
    irrf = 0.93
elif salario >= 3500 and salario <=5000:
    irrf = 0.85
elif salario > 5000:
    irrf = 0.78

beneficiodependentes = 100 * numerodependentes

salariofinal = beneficiodependentes + (salario * inss * irrf)


print(f"NOME: {nome}")

print(f"SALÁRIO BRUTO: R$ {salario}")

print(f"DESCONTO INSS: R$ {salario-(salario * inss)}")

print(f"DESCONTO IRRF: R$ {salario-(salario * irrf)}")

print(f"BENEFÍCIO POR DEPENDENTES: R$ {beneficiodependentes}")

print(f"SALÁRIO FINAL: R$ {salariofinal:.2f}")
