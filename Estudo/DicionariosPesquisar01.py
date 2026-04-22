## Funções do Dicionarios
def perguntar ():
    input("""
    O que deseja realizar?
    <I> para inserir usuario
    <P> para pesquisar usuario
    <E> para excluir usuario
    <L> para listar usuario
    """).upper()

def inserir(usuarios):
    usuarios[input("Digite seu login: ").upper()] = [input("Digite seu nome: ").upper(),
                                                     input("Digite a data de acesso: ").upper(),
                                                     input("Digite seu estacao: ").upper()]
