inventario = []
resposta ="S"
while resposta == "S":
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("numero serial: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Deseja continuar? [S/N]").upper()
for elemento in inventario:
    print("Nome.............",elemento[0])
    print("Valor............",elemento[1])
    print("Serial...........",elemento[2])
    print("Departamento.....",elemento[3])

buscar = input("\n Digite o nome que deseja buscar: ")
for elemento in inventario:
    if buscar == elemento[0]:
        print("Valor..........",elemento[1])
        print("Serial.........",elemento[2])

depreciacao = input("\n Digite o nome que deseja depreciar: ")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo...",elemento[1])
        elemento[1] = elemento[1] *0.9
        print("Valor novo...",elemento[1])

serial = int(input("\n Digite o numero do serial que deseja excluir: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)##isso e usado para remover algum item de dentro da lista

for elemento in inventario:
    print("Nome.............",elemento[0])
    print("Valor............",elemento[1])
    print("Serial...........",elemento[2])
    print("Departamento.....",elemento[3])
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(inventario)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos e de: ", sum(valores))
