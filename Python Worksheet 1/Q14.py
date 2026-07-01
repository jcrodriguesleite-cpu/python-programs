medias = []
contalunos = 0
while contalunos < 10:
    contalunos += 1
    try:
        nota1 = float(input(f"Digite a primeira nota do {contalunos}º aluno: "))
        nota2 = float(input(f"Digite a segunda nota do {contalunos}º aluno: "))
    except ValueError:
            print("Digite um valor válido.")
            continue
    medias.append((nota1+nota2)/2)
    nota1 = nota2 = 0


qtd = len(medias)
soma = sum(medias)
print(f"MÉDIA TOTAL: {(soma/qtd):.2f}")

