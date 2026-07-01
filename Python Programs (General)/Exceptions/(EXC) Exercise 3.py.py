nome = input("Digite seu nome: ")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <= 0:
            print("Idades negativas não são válidas.")
    except ValueError:
        print("Digite uma idade válida.")
    else:
        break

print("\nDados Válidos!")
print("NOME:",nome)
print("IDADE:",idade)
    
        

    

