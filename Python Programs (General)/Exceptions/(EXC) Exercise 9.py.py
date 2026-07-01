try:
    while True:
        saldo = float(input("DIGITE SEU SALDO: "))
        if saldo < 0:
            print("Digite um valor positivo.")
        else:
             break
    while True:
            saque = float(input("DIGITE O VALOR DO SAQUE: "))
            if saque > saldo:
                print("Essa operação não é possível! O valor do saque é maior que o saldo.")
            elif saque < 0:
                print("Essa operação não é possível! O valor do saque não pode ser negativo.")
            else:
                saldo -= saque
                break
            
except ValueError:
    print("Digite um valor válido.")

print(f"SACADO: {saque}")
print(f"SALDO EM CONTA: {saldo}")