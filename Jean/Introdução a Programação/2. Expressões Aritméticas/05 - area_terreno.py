# Exercicio 5 | Programa que retona a Area do Terreno em M²

from jmutils import *

# Variaveis

spacing = 40

# Cabecalho

header("Area do Terreno", spacing)

# Entrada de Dados

width = float(input("Digite a Largura do terreno(m): "))
height =  float(input("Digite a 'Altura' do terreno(m): "))

# Processamento

area = width * height

# Saida de Dados

highlight(f"O Terreno possui {area}m²", spacing)
footer(spacing)

