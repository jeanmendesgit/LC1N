# PROGRAMA QUE CONVERTE VALORES

from jmutils import *

# Variaveis

spacing = 40
exchange = 5.47

# Header
header("Conversor", spacing)

# Entrada de Dados

value = float(input("Digite o valor em Dólar: "))

# Processamento

value_in_real = value * exchange

# Saída de Dados

output = (f"USD ${value} em BRL R${value_in_real:.2f}")

highlight(output, spacing)
footer(spacing)

