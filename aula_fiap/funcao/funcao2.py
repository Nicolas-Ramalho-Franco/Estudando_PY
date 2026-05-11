def triangulo(base,altura):
    area = (base * altura)/2
    return area

def exibir(n1):
    print(f"Sua area e {n1}")

b = int(input("Digite a base"))
a = int(input("Digite a altura"))
a = triangulo(a,b)
exibir(a)