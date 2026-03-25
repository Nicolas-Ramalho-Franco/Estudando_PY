#Da para usar na questão das notas
equipamentos=[]
valores=[]
series=[]
departamento=[]

resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento :")) ##desta maneira o .append e usado para incerir o dado dentro da lista
    valores.append(float(input("Valor :")))
    series.append(int(input("Numero Seral :")))
    departamento.append(input("Departamento :"))
    resposta = input("Deseja continuar? digite S para continuar :").upper() ##Esse .upper ele aceita a resposta como maiusculo ou minusculo

for indice in range(0,len(equipamentos)): # desta maneira eu mostro os elementos dentro da lista
    print("\n Equipamento.. :",(indice+1))
    print("nome............ :",equipamentos[indice])
    print("Valor........... :", valores[indice])
    print("Sereal.......... :", series[indice])
    print("Departamento.... :", departamento[indice])

