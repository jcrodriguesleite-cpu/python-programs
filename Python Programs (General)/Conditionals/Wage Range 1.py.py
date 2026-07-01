sal = float(input("Digite o salário do funcuionário: "))
sal1 = sal * 1.15
sal2 = sal * 1.10
sal3 = sal * 1.07
sal4 = sal * 1.05

if (sal <= 1500):
    print(f"Salário inicial: {sal}")
    print(f"Percentual de aumento: 15% ")
    print(f"Valor do aumento: {(sal1 - sal):.2f}")
    print(f"Novo salário: {(sal1):.2f} ")

elif (sal > 1500 and sal <= 3000):
    print(f"Salário inicial: {sal}")
    print(f"Percentual de aumento: 10% ")
    print(f"Valor do aumento: {(sal2 - sal):.2f}")
    print(f"Novo salário: {(sal2):.2f} ")

elif (sal > 3000 and sal <= 5000):
    print(f"Salário inicial: {sal}")
    print(f"Percentual de aumento: 7% ")
    print(f"Valor do aumento: {(sal3 - sal):.2f}")
    print(f"Novo salário: {(sal3):.2f} ")

else:
    print(f"Salário inicial: {sal}")
    print(f"Percentual de aumento: 5% ")
    print(f"Valor do aumento: {(sal4 - sal):.2f}")
    print(f"Novo salário: {(sal4):.2f} ")

