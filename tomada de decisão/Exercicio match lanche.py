print("""
    =============================
    Bem vindo a lachonete do nias
    =============================
""")
print("1.Lanche")
print("2.bebida")
print("3.Sobremesa")
print("4.Sair")

opc = input("Digite a sua opção :")
match opc :
    case "1":
        print("Lache.......")
        print("1.Cachorro-quente - 15 reais")
        print("2.Hamburguer - 20 reais")
        opc1 = input("Digite a opção desejada de lanche")
        match opc1:
            case "1":
                print("Cachorro-quente - 15 reais")
                quantidade11 = int(input("Digite a quantidade que deseja : "))
                final = quantidade11*15
                print(f"Seu preço final e {final}")
            case"2":
                print("Hamburguer - 20 reais")
                quantidade1 = int(input("Digite a quantidade que deseja : "))
                final = quantidade1 * 20
                print(f"Seu preço final e {final}")
    case "2":
        print("bebida......")
        print("1.Refrigerante - 6 reais")
        print("2.Suco natural - 10 reais")
        opc2 = input("Digite a opção da bebida")
        match opc2:
            case "1":
                print("Refrigerante - 6 reais")
                quantidade21 = int(input("Digite a quantidade que deseja : "))
                final = quantidade21 * 6
                print(f"Seu preço final e {final}")
            case "2":
                print("Suco natural - 10 reais")
                quantidade2 = int(input("Digite a quantidade que deseja : "))
                final = quantidade2 * 10
                print(f"Seu preço final e {final}")
    case "3":
        print("Sobremesa")
        print("1.Açai - 25 reais")
        print("2.Sorvete = 2 s- 18 reais")
        opc3 = input("Digite a opção da bebida")
        match opc3:
            case "1":
                print("Açai - 25 reais")
                quantidade31 = int(input("Digite a quantidade que deseja : "))
                final = quantidade31 * 25
                print(f"Seu preço final e {final}")
            case "2":
                print("Sorvete - 18 reais")
                quantidade3 = int(input("Digite a quantidade que deseja : "))
                final = quantidade3 * 18
                print(f"Seu preço final e {final}")
    case "4":
        print("Saindo.....")
    case _:
        print("Opção invalida........")