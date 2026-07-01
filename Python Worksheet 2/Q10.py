def soletrar():
    listacaracteres = []
    contagemcaracteres = {}
    palavra = str(input("Digite uma palavra/caractere: "))
    for letras in palavra:
        listacaracteres.append(letras)
        if letras in contagemcaracteres:
            contagemcaracteres[letras] += 1
        else:
            contagemcaracteres[letras] = 1
            
    print(listacaracteres)
    print(contagemcaracteres)

soletrar()