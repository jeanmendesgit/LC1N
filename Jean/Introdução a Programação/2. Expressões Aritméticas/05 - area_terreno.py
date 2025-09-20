# Exercicio 5 | Programa que retona a Area do Terreno em M²

import functions as fn

# Variaveis

spacing = 40

# Cabecalho

fn.header("Area do Terreno", spacing)

# Entrada de Dados

width = float(input("Digite a Largura do terreno(m): "))
height =  float(input("Digite a 'Altura' do terreno(m): "))

# Processamento

area = width * height

# Saida de Dados

print("-" * spacing)
print(f"\nO Terreno possui {area}m²")
fn.footer(spacing)

