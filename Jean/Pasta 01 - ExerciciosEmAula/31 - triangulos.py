# Programa que dado A, B e C se constitui um triangulo ou nao e qual seria

import functions as fn

# Variaveis
title = "Triangulos"
spacing = 50
numbers = []
triangle = False

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
for i in range(3):
    numbers.append(int(input(f"Digite o {i + 1}° número: ")))

# Processamento de Dados

if numbers[0] < numbers[1] + numbers[2] and numbers[1] < numbers[0] + numbers[2] and numbers[2] < numbers[0] + numbers[1]:
    triangle = True
else:
    pass

if triangle:
    if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
        # Equilátero









