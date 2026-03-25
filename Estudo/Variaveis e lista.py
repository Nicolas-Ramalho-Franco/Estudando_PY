inventario=[]
resposta = "s"
while resposta == "s":
    inventario.append(input("Equipamento :")) ##desta maneira o .append e usado para incerir o dado dentro da lista
    inventario.append(float(input("Valor :")))
    inventario.append(int(input("Numero Seral :")))
    inventario.append(input("Departamento :"))
    resposta = input("Deseja continuar? digite s para continuar :")

for elemento in inventario: # desta maneira eu mostro os elementos dentro da lista
    print(elemento)