contador = 1
listadeprodutos = []
produtos = {}
while contador <= 3:
    print("=" * 30)
    produtos[contador] = {
            "nome": input("Nome do produto: "),
            "preço": float(input("Preço do Produto: ")),
            "estoque": int(input("QTD em Estoque: ")),
            "codigo": int(input("Código: "))
        }
    contador += 1
    print("=" * 30)
    listadeprodutos.append(produtos)

for chave,valor in produtos.items():
    print(chave," : ",valor)

