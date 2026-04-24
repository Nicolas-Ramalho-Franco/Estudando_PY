from DicionariosPesquisar01 import *

usuarios = {}
opc = perguntar ()
while opc == "I" or opc == "P" or opc == "E" or opc == "L":
    if opc == "I":
        inserir(usuarios)
    opc = perguntar ()
