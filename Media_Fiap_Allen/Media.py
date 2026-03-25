### PRIMEIRA MÉDIA: M1 = ((CP1 + CP2)/2) * 0.2 + ((SP1 + SP2)/2) * 0.2 + GS1 * 0.6

### SEGUNDA MÉDIA: M2 = ((CP4 + CP5)/2) * 0.2 + ((SP3 + SP4)/2) * 0.2 + GS2 * 0.6
print("""
=====================================
bem vindo ao Calculador de nota 3000
=====================================
""")
resposta = "S"
#Media M1
while resposta == "S":
    CP1 = float(input("Digite a primeira nota da CP1: "))
    CP2 = float(input("Digite a segunda nota da CP2: "))
    CP3 = float(input("Digite a segunda nota da CP2: "))
    SP1 = float(input("Digite a primeira nota da SP1: "))
    SP2 = float(input("Digite a segunda nota da SP2: "))
    GS1 = float(input("Digite a primeira nota da GS1: "))

    print("""
    ====================================
    Notas do segundo semestre
    ====================================
    """)
    #Media M2
    CP1M2 = float(input("Digite a primeira nota da CP1 do segundo Semestre: "))
    CP3M2 = float(input("Digite a primeira nota da CP1 do segundo Semestre: "))
    CP2M2 = float(input("Digite a primeira nota da CP2 do segundo Semestre: "))
    SP1M2 = float(input("Digite a primeira nota da SP1 do segundo Semestre: "))
    SP2M2 = float(input("Digite a segunda nota da SP2 do segundo Semestre: "))
    GS2 = float(input("Digite a primeira nota da GS2 do segundo Semestre: "))

    if CP1 <= CP2 and CP1<=CP3:
        CP1 = CP3
    elif CP2 <= CP1 and CP2 <= CP3:
        CP2=CP3

    if CP1M2 <= CP2M2 and CP1M2<=CP3M2:
        CP1M2 = CP3M2
    elif CP2M2 <= CP1M2 and CP2M2 <= CP3M2:
        CP2M2=CP3M2


    M1 = (((CP1 + CP2)/2) * 0.2 + ((SP1 + SP2)/2) * 0.2 + GS1 * 0.6)*0.4

    M2 = (((CP1M2 + CP2M2)/2) * 0.2 + ((SP1M2 + SP2M2)/2) * 0.2 + GS2 * 0.6)*0.6

    media_do_ano = M1 + M2

    print("Essa e sua media do Ano na fiap" , media_do_ano)
    faltas = int(input("Digite o quanto voce faltou entre 0 a 100 :"))

    if media_do_ano >=6 and faltas <75 :
        print(f"Parabens o aluno passou com a mededia {media_do_ano}, e com esse numero de faltas {faltas}")

    else:
        print(f"O irmão voce reprovou em com a media {media_do_ano}, e com essa frequencia {faltas}")
    resposta = input("Deseja continuar? digite S para continuar :").upper()