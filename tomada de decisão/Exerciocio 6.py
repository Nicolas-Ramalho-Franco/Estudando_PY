Horas = int(input("Digite uma valor de horas :"))
Minutos = int(input("Digite uma valor de minutos :"))

if Horas == 00 and Minutos == 00:
    print(f"Voce digitou essas horas  {Horas}:{Minutos}")
elif Horas <= 23  and Minutos <60 :
    print(f"Voce digitou essas horas : {Horas}:{Minutos}")
else :
    print("Voce digitou horas invalidas")