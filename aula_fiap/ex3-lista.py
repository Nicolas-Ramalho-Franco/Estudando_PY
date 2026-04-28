import random
lista =[]
for i in range(20):
    a = random.randint(1, 50)
    lista.append(a)

print(lista)
print(sum(lista))
print(max(lista))
print(min(lista))