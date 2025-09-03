# PROGRAMA QUE CONVERTE VALORES

import functions as fn

# Variaveis

spacing = 40
exchange = 5.47

# Header
fn.header("Conversor", spacing)

# Entrada de Dados

value = float(input("Digite o valor em Dólar: "))

# Processamento

value_in_real = value * exchange

# Saída de Dados

print(" ")
print("-" * spacing)
print(f"\nUSD ${value} em BRL R${value_in_real:.2f}")
fn.footer(spacing)

