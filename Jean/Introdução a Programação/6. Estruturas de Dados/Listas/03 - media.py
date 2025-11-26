# Programa que tira a média de 5 números

from jmutils import *

# VARIAVEIS ________________________________________________________________________________________________
title, spacing, color = "Média de 5 Números", 50, 'green'

numbers = [1, 2, 3, 4, 5]

# PROCESSAMENTO DE DADOS ___________________________________________________________________________________

# =-= Possibilidade 1 =-=
# soma  = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# media = soma / 5 

# =-= Possibilidade 2 =-=
# soma = 0
# for i in range(5):
#     soma = numbers[i] + soma
# media = soma / 5

# =-= Possibilidade 3 =-=
media = sum(numbers) / len(numbers)

# SAÍDA DE DADOS ___________________________________________________________________________________________
header_color(title, spacing, color)

print(f"> Números: {numbers}\n\n> Média: {media:.2f}")

footer(spacing)
