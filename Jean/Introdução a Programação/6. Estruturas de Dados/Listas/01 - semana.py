#  Programa que mostras os dias da semana

from jmutils import *

# VARIAVEIS ______________________________________________________________________________________
title, spacing, color = "Dias da Semana", 50, 'green'

week = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# SAÍDA DE DADOS _________________________________________________________________________________
header_color(title, spacing, color)

for i in range(len(week)):
    if i < 5:
        print(f"{week[i]}-feira")
        continue

    print(week[i])

footer(spacing)




