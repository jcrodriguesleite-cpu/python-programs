aluno = {
    
    "nome": input("Nome: "),
    "idade": int(input("Idade: ")),
    "nota": float(input("Nota: "))

}

print("\n Dados do Aluno: ")
for chave, valor in aluno.items():
    print(chave," : ",valor)