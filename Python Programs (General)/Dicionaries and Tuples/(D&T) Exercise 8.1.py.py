palavra = "banana"
dicioletras = {}

for letras in palavra:
    dicioletras[letras] = dicioletras.get(letras,0) + 1

print(dicioletras)