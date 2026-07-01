nota = float(input("Digite a nota do aluno: "))
freq = int(input("Digite a frequência do aluno: "))
aprovado = nota >= 7 and freq >= 75
print(f"Aprovado? {aprovado}")