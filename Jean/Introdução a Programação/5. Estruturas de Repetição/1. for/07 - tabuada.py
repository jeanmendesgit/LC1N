# Programa que mostra a tabuada de multiplicação de um número, de 1 a 10.

from jmutils import *

# Variaveis
title, spacing = "Tabuada", 50

start, stop, step = 1, 11, 1

# Cabeçalho

header(title, spacing)

# Entrada de Dados

numero = int(input("Digite um número: "))

# Saida de Dados
header(title, spacing)

for i in range(start, stop, step):
    print(f"{numero} x {i} = {numero * i}")

footer(spacing)