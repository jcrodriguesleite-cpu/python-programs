listalunos = []

def cadastro_aluno ():
    while True:
        nome = input("NOME DO ALUNO: ")
        n1 = float(input("NOTA 1: "))
        n2 = float(input("NOTA 2: "))
        media = (n1+n2)/2
        alunos = {
            "nome": nome,
            "nota1": n1,
            "nota2": n2,
            "média": media
        }
        listalunos.append(alunos)
        resp = input("DESEJA CONTINUAR? [S/N]: ")
        if resp == "S":
            continue
        else:
            break

def consultarsituacao():
    while True:
        nome = input("DIGITE O NOME DO ALUNO: ")
        for alunos in listalunos:
            if alunos["nome"] == nome:
                print(alunos)
        resp = input("DESEJA CONTINUAR? [S/N]: ")
        if resp == "S":
            continue
        else:
            break


def menuprincipal():
    print("=" * 10, "BANCO DE DADOS DOS ALUNOS","=" * 10)
    print("DIGITE UMA DAS OPÇÕES ABAIXO \n [0] PARA CHECAR SITUAÇÃO DO ALUNO \n [1] PARA CADASTRAR UM NOVO ALUNO \n [2] PARA LISTAR TODO O BANCO DE DADOS \n [3] PARA SAIR")
    print("=" * 47)

while True:

    menuprincipal()

    resp = input("DIGITE AQUI: ")
    if resp == "0":
        consultarsituacao()
    elif resp == "1":
        cadastro_aluno()
    elif resp == "2":
        for alunos in listalunos:
            print(alunos)
    elif resp == "3":
        break
    else:
        print("Opção Inválida!")

     
       
             

