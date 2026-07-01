produto = {
    "nome":"arroz",
    "preço": 10
}

resp = input("DESEJA ALTERAR O PREÇO DO PRODUTO? [S/N]: ")
if resp == "S":
    produto["preço"] = float(input("Digite o novo preço: "))

print(produto)







