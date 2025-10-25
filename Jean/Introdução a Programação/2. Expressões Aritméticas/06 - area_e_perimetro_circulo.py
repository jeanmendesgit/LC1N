# Exercicio 6 | Programa que calcula a área e perímetro de um círculo

from jmutils import *

# Variaveis

PI = 3.14159265359
spacing = 60

# Cabecalho

header("Área e Perímetro de um Círculo", spacing)

# Entrada de Dados

ray = float(input("Digite o valor do Raio: "))

# Processamento

area      = PI * (ray**2)
perimeter = PI * 2 * ray

# Saida de Dados

output = f"Área: A = {area:.1f} | Perímetro: P = {perimeter:.1f}"

highlight(output, spacing)
footer(spacing)