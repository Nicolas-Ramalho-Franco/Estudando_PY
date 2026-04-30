notas = [1,2,3,5,6,3,7,9,5,3,6,6]
min = notas[0]
max = notas[0]

for i in notas:
    if min>i:
        min = i
    if max<i:
        max = i
print(max)
print(min)