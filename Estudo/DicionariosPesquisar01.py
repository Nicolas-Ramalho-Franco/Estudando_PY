## Funções do Dicionarios
def perguntar ():
    return input("""
    O que deseja realizar?
    <I> para inserir usuario
    <P> para pesquisar usuario
    <E> para excluir usuario
    <L> para listar usuario
    """).upper()

def inserir(dicionario):
    dicionario[input("Digite seu login: ").upper()] = [input("Digite seu nome: ").upper(),
                                                     input("Digite a data de acesso: ").upper(),
                                                     input("Digite seu estacao: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave+":"+str(valor))