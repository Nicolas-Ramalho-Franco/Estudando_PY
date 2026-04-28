impar = []
par = []
contagem = 0
for i in range (1,11):
    n = int(input("Digite um numero ai"))
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)

print(impar)
print(par)