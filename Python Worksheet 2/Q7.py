def vogais_empalavras():   
    palavra = str(input("Digite uma palavra: "))
    contvogais = 0
    for letras in palavra:
        if letras in 'aeiou':
            contvogais += 1

    print(contvogais)

vogais_empalavras()

