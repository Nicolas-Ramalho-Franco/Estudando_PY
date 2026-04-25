import json

with open("db.json", "r") as arq_json:
    dic = json.load(arq_json) #.load carregar a informação em algo
    for chave,dados in dic.items():
        print(chave + "|"+ str(dados)) # colocando o [] pode pegar o indice
