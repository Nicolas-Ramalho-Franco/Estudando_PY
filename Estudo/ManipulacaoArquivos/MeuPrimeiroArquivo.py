with open("primeiroarquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readline():
        print(conteudo)