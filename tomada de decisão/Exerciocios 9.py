L1 = float(input("Digite um lado"))
L2 = float(input("Digite um lado"))
L3 = float(input("Digite um lado"))

if L1 == L2 and L2 ==L3:
    print("isso e um triangulo equilatero")
elif L1 == L2 or L3 == L2 or L3 == L1:
    print("Seu triangulo e isoceles")
else:
    print("E um triangulo escaleno")