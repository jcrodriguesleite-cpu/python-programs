lista = []
contador = 0

while contador < 2:
    try:
        nota = (float(input("DIGITE UMA NOTA: ")))
        if nota < 0 and nota > 10:
            print("Digite um valor entre 0 e 10.")
        else:
            lista.append(nota)
            contador += 1
    except ValueError:
        print("Digite um valor válido.")

    