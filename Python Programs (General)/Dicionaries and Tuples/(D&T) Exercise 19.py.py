alunos = []
cont = 0
while cont <= 2:
    nome = input("NOME: ")
    nota = float(input("NOTA: "))

    aluno = {
        "índice": cont,
        "nome": nome,
        "nota": nota
    }

    alunos.append(aluno)

    cont += 1


for estudantes in alunos:
    if estudantes["nota"] > 7:
        print(estudantes)
    