nuemro= []
par =[]
for i in range (10):
    n = int(input("Digite um numero ai:"))
    nuemro.append(n)
    if n%2==0:
        par.append(n)

print(sum(par))
print(len(nuemro)/(sum(nuemro)))
