def juroscompostos():
    capital = float(input("Digite o capital em reais: R$ "))
    indice = float(input("Digite o valor da taxa em percentual: "))
    tempo = int(float(input("Digite o tempo do investimento em meses: ")))

    montante = capital * ((1+(indice/100))**tempo)

    print(f"MONTANTE: R$ {montante:.2f}")

juroscompostos()

