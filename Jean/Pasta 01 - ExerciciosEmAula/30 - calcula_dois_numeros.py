# Programa que lê dois numeros, calcula e imprime

import functions as fn

# Variaveis
title = "Calculos entre 2 números"
spacing = 50

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
number_1 = int(input("Digite o 1° número: "))
number_2 = int(input("Digite o 2° número: "))

# Processamento de Dados

sum = number_1 + number_2
one_sub = number_1 - number_2
two_sub = number_2 - number_1
multiply = number_1 * number_2
division = number_1 / number_2
rest = number_1 % number_2
high = number_1 ** number_2

if number_1 < number_2:
    relation = "Menor"
elif number_1 > number_2:
    relation = "Maior"
else:
    relation = "Igual"

# Saída de Dados
output = f"DADOS\n> Soma: {sum}\n> 1° - 2°: {one_sub}> 2° - 1°: {two_sub}\n> Produto: {multiply}\n> Divisão 1°: {division}\n> Resto 1°: {rest}\n> Relação: {relation}\n> Potenciação: {high}"


