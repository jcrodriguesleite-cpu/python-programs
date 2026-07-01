palavra = "banana"

diciopalavra = {}

for letras in palavra:
    if letras not in diciopalavra:
        diciopalavra[letras] = 1
    else:
        diciopalavra[letras] += 1

print(diciopalavra)