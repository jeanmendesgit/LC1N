# programa que le nomes até o usuário digitar "sair"

from jmutils import *

# Variaveis
title, spacing = "Leitura de Nomes", 50

# Cabeçalho
header(title, spacing)

while True:
    entry = input("Digite um NOME ou SAIR: ")

    exit = entry.lower()

    if exit != 'sair':
        highlight(f"Nome: {entry}", spacing)
    else:
        highlight(f"Encerrando o programa...", spacing)
        break
    
    print(" ")