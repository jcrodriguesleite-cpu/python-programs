listasoma = []
for i in range(1,11):
    try:
        num = listasoma.append(int(input(f"Digite o {i}º número inteiro: ")))

    except ValueError:
        print("Digite um valor válido.")
    

print(sum(listasoma))
