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
    relation = "<"
elif number_1 > number_2:
    relation = ">"
else:
    relation = "="

# Saída de Dados
output = f"DADOS de N1°: {number_1} e N2°: {number_2}\n» {number_1} {relation} {number_2}\n» {number_1} + {number_2} = {sum}\n» {number_1} - {number_2} = {one_sub}\n» {number_2} - {number_1} = {two_sub}\n» {number_1} * {number_2} = {multiply}\n» {number_1} / {number_2} = {division:.2f}\n» {number_1} % {number_2} = {rest}\n» {number_1} ^ {number_2} = {high}"

fn.highlight(output, spacing)
fn.footer(spacing)
