alunos = []
while True:
    nome = input("DIGITE O NOME DO ALUNO: ")
    try:
        n1 = float(input("DIGITE A NOTA 1: "))
        if n1 < 0 or n1 > 10:
            print("Valores negativos/Maiores que 10 não são considerados notas.")
            continue
        n2 = float(input("DIGITE A NOTA 2: "))
        if n2 < 0 or n2 > 10:
            print("Valores negativos/Maiores que 10 não são considerados notas.")
            continue
    except ValueError:
        print("Digite um valor válido.")
    except TypeError:
        print("Caracteres de tipo errado. Insira novamente.")
    else:
        media = (n1+n2)/2
        aluno = [
            {"NOME: ":nome},
            {"NOTA 1:":n1},
            {"NOTA 2:":n2},
            {"MÉDIA:":media}
        ]
        alunos.append(aluno)
        resp = input("DESEJA CONTINUAR? [S/N]: ")
        if resp == "S":
            continue
        else:
            break


