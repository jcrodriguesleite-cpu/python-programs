def conversaotemp():
    Tf = float(input("Digite uma Temperatura em graus Fahrenheit: "))
    Tc = (Tf - 32) * (5/9)
    print(f"O equivalente em graus Celsius é: {Tc}")

conversaotemp()