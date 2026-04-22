def captacaoDeDados(nota):
    print("""
<<<<<<< HEAD
            =====================================
            bem vindo ao Calculador de nota 3000
            =====================================
=======
        =====================================
        bem vindo ao Calculador de nota 3000
        =====================================
>>>>>>> e70f7ae921729a635c10b3b17d3d7123cf641a34
        """)
    resposta = "S"

    while resposta == "S":
        # Media M1
        print("""
            ===================================
            Notas do primeiro semestre
            ====================================
            """)
        global nome ,CP1,CP2,CP3,SP1,SP2,GS1
        nome = input("Digite o nome do Aluno : ")
        CP1 = float(input("Digite a primeira nota da CP1: "))
        CP2 = float(input("Digite a segunda nota da CP2: "))
        CP3 = float(input("Digite a segunda nota da CP2: "))
        SP1 = float(input("Digite a primeira nota da SP1: "))
        SP2 = float(input("Digite a segunda nota da SP2: "))
        GS1 = float(input("Digite a primeira nota da GS1: "))
        cpsm1 = [CP1, CP2, CP3]
        maiorm1 = sorted(cpsm1, reverse=True)[:2]  ##isso funciona para pegar os dois maiores e localizar
        totalm1 = sum(maiorm1)  ## esses sum e para somar o valor
        print("""
        ====================================
        Notas do segundo semestre
        ====================================
        """)
        # Media M2
        global CP1M2,CP2M2,CP3M2,SP1M2,SP2M2,GS2
        CP1M2 = float(input("Digite a primeira nota da CP1 do segundo Semestre: "))
        CP2M2 = float(input("Digite a primeira nota da CP2 do segundo Semestre: "))
        CP3M2 = float(input("Digite a primeira nota da CP3 do segundo Semestre: "))
        SP1M2 = float(input("Digite a primeira nota da SP1 do segundo Semestre: "))
        SP2M2 = float(input("Digite a segunda nota da SP2 do segundo Semestre: "))
        GS2 = float(input("Digite a primeira nota da GS2 do segundo Semestre: "))
        cpsm2 = [CP1M2, CP2M2, CP3M2]
        maiorm2 = sorted(cpsm2, reverse=True)[:2]
        totalm2 = sum(maiorm2)

        M1 = (((totalm1) / 2) * 0.2 + ((SP1 + SP2) / 2) * 0.2 + GS1 * 0.6) * 0.4

        M2 = (((totalm2) / 2) * 0.2 + ((SP1M2 + SP2M2) / 2) * 0.2 + GS2 * 0.6) * 0.6

        media_do_ano = M1 + M2

        print("Essa e sua media do Ano na fiap", media_do_ano)
        faltas = int(input("Digite o quanto voce faltou entre 0 a 100 :"))

        if media_do_ano >= 6 and faltas < 75:
            print(f"Parabens o {nome} passou com a mededia {media_do_ano}, e com esse numero de faltas {faltas}")

        else:
            print(f"O {nome} voce reprovou em com a media {media_do_ano}, e com essas faltas {faltas}")
        resposta = input("Deseja continuar? digite S para continuar :").upper()

def demostracaoDeNota(mostrar):
    print(f"""
        Ola {nome}, essas foram as sua notas.
        Notas do primeiro semestre.
        CP1 = {CP1}, CP2 = {CP2}, CP3 = {CP3},
        SP1 = {SP1}, SP2 = {SP2}, 
        GS1 = {GS1}
        Essas foram são as notas do {nome} do segundo semestre.
        CP1M2 = {CP1M2}, CP2M2 = {CP2M2},CP3M2 = {CP3M2},
        SP1M2 = {SP1M2}, SP2M2 = {SP2M2},
        GS2 = {GS2} 
    """)
