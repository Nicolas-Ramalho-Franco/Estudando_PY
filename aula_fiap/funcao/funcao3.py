def validar(nota):
    while nota<0 or nota>10:
        nota = float(input("Digite a nota novamente(0 e 10)"))
    return nota
def media(n1,n2):
    Media = (n1+n2)/2
    if Media<=6:
        print("Passou por pouco")
    if Media==10:
        print("Ai sim chefe passou com gloria")
    if Media<=5:
        print("Ta de rec burro")


nota1 = float(input("Digita uma nota"))
nota1=validar(nota1)

nota2 = float(input("Digita uma nota"))
nota2=validar(nota1)

media(nota1,nota2)