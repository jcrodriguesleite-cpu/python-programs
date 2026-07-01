def menuprincipal():
    print("=" * 35)
    print(" " * 5,"BANCO DE DADOS ALUNOS")
    print("=" * 35)
    print("[1] PARA CADASTRAR NOVO ALUNO\n[2] PARA LISTAR OS ALUNOS\n[3] PARA SAIR\n")
    
def cadastroalunos():
    while True:
        with open("dados.txt","a",encoding="utf-8") as arquivo:
            nome = input("NOME DO ALUNO: ")
            idade = input("IDADE: ")
            arquivo.write(nome + " - " + idade + "\n")
        resp = input("DESEJA CONTINUAR? [S/N]: ")
        if resp == "S":
            continue
        else:
            break
while True:
    menuprincipal()

    resp = int(input("DIGITE AQUI: "))
    if resp == 1:
        print("\n")
        cadastroalunos()
    elif resp == 2:
        print("\n")
        with open("dados.txt","r",encoding="utf-8") as arquivo:
            print(arquivo.read())
    elif resp == 3:
        break
        
