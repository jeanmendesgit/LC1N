# programa que some os 5 primeiros números positivos que o usuário digitar.

import functions as fn

# Variaveis
title, spacing = "Soma dos 5 primeiros Positivos", 50

counter = 1

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
while counter < 5:

    entry = int(input(f"Digite o {counter}° número inteiro positivo: "))

    counter += 1