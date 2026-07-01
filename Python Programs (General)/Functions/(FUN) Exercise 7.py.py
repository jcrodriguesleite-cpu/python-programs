def contletras(palavra):
    contador = 0
    for letras in palavra:
        contador += 1

    return print(f"Essa palavra tem {contador} letras.")

pergunta = input("DIGITE UMA PALAVRA PARA SABER QUANTAS LETRAS ELA TEM: ")

contletras(pergunta)