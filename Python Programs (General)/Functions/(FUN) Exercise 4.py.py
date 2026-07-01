def aumento_salarial():
    salario = float(input("SALÁRIO: "))
    percentual = float(input("PERCENTUAL DE AUMENTO: "))
    print(f"ANTIGO SALÁRIO: {salario}")
    print(f"PERCENTUAL DE AUMENTO: {percentual}% ")
    novosalario = salario * (1+(percentual/100))
    print(f"VALOR DO AUMENTO: {novosalario - salario}")
    print(f"SALÁRIO FINAL: {novosalario}")


aumento_salarial()
