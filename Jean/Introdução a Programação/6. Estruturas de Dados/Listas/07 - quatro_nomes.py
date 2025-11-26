# Programa que cria uma lista contendo 4 nomes digitados pelo usuário.
# Em seguida, exiba a lista e permita que o usuário escolha um nome para ser removido.

from jmutils import *

# VARIAVEIS ___________________________________________________________________________________
title, title2, spacing, color_main = "Quatro Nomes", "Remova 1 Nome", 60, 'green'

counter    = 4
names_list = []

# CABEÇALHO ___________________________________________________________________________________
header_color(title, spacing, color_main)

# PROCESSAMENTO DE DADOS ______________________________________________________________________
for i in range(counter):
    name = input(f"Digite o {i + 1}° nome: ")
    names_list.append(name)
    line(spacing)

# SAÍDA DE DADOS ______________________________________________________________________________
header_color(title2, spacing, color_main)

for i, name in enumerate(names_list):
    print(f"{i + 1}) {name}")

entry = int(input("\nDigite o número do nome que deseja remover: "))

del names_list[entry - 1]

highlight_color("Nome removido com sucesso!", spacing, color_main)

for i, name in enumerate(names_list):
    print(f"{i + 1}) {name}")

footer(spacing)
    

