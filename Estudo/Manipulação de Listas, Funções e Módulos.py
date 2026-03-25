equipamentos=[]
valores=[]
series=[]
departamento=[]
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento :")) ##desta maneira o .append e usado para incerir o dado dentro da lista que sera antes do .append
    valores.append(float(input("Valor :")))
    series.append(int(input("Numero Seral :")))
    departamento.append(input("Departamento :"))
    resposta = input("Deseja continuar? digite S para continuar :").upper() ##Esse .upper ele aceita a resposta como maiusculo ou minusculo

buscar = input("\n Digite o nome do equipamento que deseja buscar: ") ## isso funciona para buscar algo que esta nas matriz
for indice in range(0,len(equipamentos)): # desta maneira eu mostro os elementos dentro da lista
    print("Valor........... :", valores[indice])
    print("Sereal.......... :", series[indice])