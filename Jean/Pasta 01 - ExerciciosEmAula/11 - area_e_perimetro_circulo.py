# Exercicio 6 | Programa que calcula a área e perímetro de um círculo

import functions as fn

# Variaveis

PI = 3.14
spacing = 50

# Cabecalho

fn.header("Área e Perímetro de um Círculo", spacing)

# Entrada de Dados

ray = float(input("Digite o valor do Raio: "))

# Processamento

area = PI * (ray**2)
perimeter = PI * 2 * ray

# Saida de Dados

print(area)
print(perimeter)
