#if - else
#vai saber ce usa um if ou else quando o cliente pedir, o cliente vai definir quando usar
# elif e um else seguido de um if
numero = int(input("Digite um numero inteiro entre 10 a 0"))
if numero > 5:
    print(f"Voce digitou {numero} que e numero maior que 5")
elif numero < 5:
    print(f"numero {numero} menor que 5")
else:
    print(f"numero e {numero} que e == a 5")
