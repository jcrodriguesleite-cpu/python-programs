resultado = 0
while True:
    try:
        operacao = int(input("DIGITE A OPERAÇÃO QUE DESEJA FAZER: \n[1] PARA SOMA\n[2] PARA SUBTRAÇÃO\n[3] PARA MULTIPLICAÇÃO\n[4] PARA DIVISÃO\n DIGITE AQUI: "))
        num1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
        num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
        if operacao == 1:
            resultado = num1 + num2
        elif operacao == 2:
            resultado = num1 - num2
        elif operacao == 3:
            resultado = num1 * num2
        elif operacao == 4:
            resultado = num1 / num2
    except ZeroDivisionError:
        print("DIVISÕES POR ZERO NÃO SÃO VÁLIDAS, REFAÇA A OPERAÇÃO.")
    except ValueError:
        print("DIGITE VALOR(ES) VÁLIDOS.")
    else:
        print(f"RESULTADO: {resultado}")
        break