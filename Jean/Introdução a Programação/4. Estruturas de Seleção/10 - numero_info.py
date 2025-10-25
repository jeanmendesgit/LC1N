# Programa que mostra algumas infomacoes a partir de um numero

from jmutils import *

# Variaveis
title = "Informações do número"
spacing = 50

# Cabeçalho
header(title, spacing)

# Entrada de Dados
number = int(input("Digite um número: "))

# Processamento de Dados
numerical_set = "Par" if number % 2 == 0 else "Ímpar"

if number < 0:
    number_value = "Negativo"
elif number > 0:
    number_value = "Positivo"
else:
    number_value = "Nulo"

d2 = number % 2
d5 = number % 5

if d2 != 0 and d5 != 0:
    number_division = "Nenhum"
elif d2 == 0 and d5 !=0:
    number_division = "Apenas 2"
elif d2 != 0 and d5 == 0:
    number_division = "Apenas 5"
elif d2 == 0 and d5 == 0:
    number_division = "Ambos"

# Saída de Dados
highlight(f"DADOS\n> Conjuto: {numerical_set}\n> Valor: {number_value}\n> Divisão por 2 e 5: {number_division}", spacing)
footer(spacing)



