sal = int(input("Digite o salário: "))

if sal <= 1500:
    reajuste = 1.15
elif sal > 1500 and sal <= 3000:
    reajuste = 1.10
elif sal > 3000 and sal <= 5000:
    reajuste = 1.07
else:
    reajuste = 1.05


print(f"Valor inicial: {sal}")
print(f"Valor do Reajuste: {((sal * reajuste) - sal):.2f}")
print(f"Valor Final com Reajuste: {(sal*reajuste):.2f}")