
usuarios = {}
emails = ["Nicolasramalhof@gmcil.com", "XPTO@.com" ]

tupla = list(enumerate(emails))

for  chave in range (0, len(tupla)): ##len e o comprimento da tupla
     print("Email : ", tupla[chave][1])
     usuarios[tupla[chave]] = [input("Digite o seu nome:") ,input("Digite o seu nivel:")]

for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("nome....:", dado[0])
    print("Nivel...:", dado[1])