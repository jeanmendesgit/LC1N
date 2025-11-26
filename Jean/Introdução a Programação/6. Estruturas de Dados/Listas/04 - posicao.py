# Programa que mostra a posição de 10 números

from jmutils import *

# VARIAVEIS ___________________________________________________________________
title, spacing, color = "Posição de 10 Números", 50, 'green'

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# SAÍDA DE DADOS ______________________________________________________________
header_color(title, spacing, color)

print(f"Lista: {numbers}\n")

for i, number in enumerate(numbers):

    print(f"Posição {i}: {number}")

footer(spacing)