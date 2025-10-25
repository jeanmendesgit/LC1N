from jmutils import *

# Programa que informa se um número é positivo, negativo ou nulo

# Variaveis
title   = "Positivo, Negativo ou Nulo"
spacing = 60

# Cabeçalho
header(title, spacing)

# Entrada de Dados
number = int(input("Digite um número: "))

# Processamento de Dados
if   number > 0:
    value = "Positivo"
elif number < 0:
    value = "Negativo"
else:
    value = "Nulo"
    
# Saída de Dados
highlight(f"O número {number} tem o valor « {value} »",spacing)
footer(spacing)