# programa que le nomes até o usuário digitar "sair"

import functions as fn

# Variaveis
title, spacing = "Leitura de Nomes", 50

# Cabeçalho
fn.header(title, spacing)

while True:
    entry = input("Digite um NOME ou SAIR: ")

    exit = entry.lower()

    if exit != 'sair':
        fn.highlight(f"Nome: {entry}", spacing)
    else:
        fn.highlight(f"Encerrando o programa...", spacing)
        break
    
    print(" ")