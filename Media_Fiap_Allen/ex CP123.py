#resp = 1
#cont = 0
#while resp <10:
    #idade =int(input("Digite 10 idades :"))
   # if idade >=18:
  #      cont += 1
 #   resp += 1
#print("Esses foram os maiores de idade :" , cont)

numero = int(input("Digite um numero inteiro"))
digitos = [int(nPorN) for nPorN in str(numero)]
print(sum (digitos))

