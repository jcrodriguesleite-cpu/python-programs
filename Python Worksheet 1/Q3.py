idade = int(input("Digite sua idade: "))

match idade:
    case idade if idade >= 5 and idade <= 7:
        print("Você é da categoria Infantil A")
    
    case idade if idade >= 8 and idade <= 10:
        print("Você é da categoria Infantil B")

    case idade if idade >= 11 and idade <= 13:
        print("Você é da categoria Juvenil A")
    
    case idade if idade >= 14 and idade <= 17:
        print("Você é da categoria Juvenil B")
    
    case idade if idade > 18:
        print("Você é da categoria Sênior")

