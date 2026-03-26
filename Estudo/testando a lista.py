notas = []
resposta = "S"
while resposta == "S":
    notasm1 =[float(input("Digite a primeira nota m1: ")),
              float(input("Digite a segunda nota m1: ")),
              float(input("Digite a terceira nota m1: ")),
              float(input("Digite a quarta nota m1: "))]
    notas.append(notasm1)
    resposta = input("Deseja continuar? [S/N]").upper()

for elementes in notas:
    print("Sua primeira e ", elementes[0])
    print("Sua segunda e ", elementes[1])
    print("Sua terceira e ", elementes[2])
    print("Sua quarta e ", elementes[3])
    print("sua nota e essa aqui",elementes[0]+elementes[1]+elementes[2]+elementes[3])