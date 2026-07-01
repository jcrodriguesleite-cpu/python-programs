catalogoprodutos = [
    {"nome": "Arroz", "preço": 12},
    {"nome": "Feijão", "preço": 10},
    {"nome": "Carne", "preço": 60}
]

maiscaro = 0

for produtos in catalogoprodutos:
    if produtos["preço"] > maiscaro:
        maiscaro = produtos["preço"]

print(maiscaro)