n1 = float(input("Digite a sua primeira nota : "))
n2 = float(input("Digite a sua segunda nota : "))
n3 = float(input("Digite a sua terceira nota : "))

media = (n1 + n2 + n3) / 3
if media >= 6:
    print(f"Aprovado com a media {media}")
else:
    print(f"Reprovado com essa media {media}")