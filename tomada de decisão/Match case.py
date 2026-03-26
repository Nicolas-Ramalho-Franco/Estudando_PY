
print("2.Editar nota")
print("3.Incerir nota")
print("4.Excluir nota")
print("5.Sair")
print("6. para continuar")

opc = input("Digite a sua opção : ")
match opc :
    case "1":
        print("Voce escolheu a opção de verificar a nota do aluno")
    case "2":
        print("Voce escokheu editar a nota do aluno")
    case "3":
        print("Voce escolheu incerir nota")
    case "4":
        print("Voce vai excluir nota")
    case "5":
        print("Saindo.....")
    case _:
        print("Opção invalida........")
