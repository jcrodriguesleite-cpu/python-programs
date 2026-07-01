def area_e_perimetro():
    raio = float(input("Digite o raio do círculo em cm: "))
    pi = 3.14
    area = pi*(raio**2)
    perimetro = 2*pi*raio

    print(f"ÁREA: {area} cm²")
    print(f"PERÍMETRO: {perimetro:.2f} cm")

area_e_perimetro()