# Programa que implementa uma lista que o usuário pode digitar cinco cores e imprime a primeira e última cor que o usuário digitou.

from jmutils import *

# VARIAVEIS ___________________________________________________________________________________
title, spacing, color_main = "5 Cores", 60, 'green'

counter_init  = 5
counter       = counter_init
colors_list = []

# CABEÇALHO ___________________________________________________________________________________
header_color(title, spacing, color_main)

# PROCESSAMENTO DE DADOS ______________________________________________________________________
while counter > 0:
    i = (counter_init + 1) - counter

    color = input(f"Digite a {i}° cor: ")

    line(spacing)

    colors_list.append(color)
    counter -= 1

# SAÍDA DE DADOS ______________________________________________________________________________
header_color(title, spacing, color_main)

print(f"1ª Cor: {colors_list[0]}\n5ª Cor: {colors_list[len(colors_list) - 1]}")

footer(spacing)
    

