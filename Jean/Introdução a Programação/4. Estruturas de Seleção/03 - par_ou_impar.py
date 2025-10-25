# Programa que imforma par ou impar

from jmutils import *

# Variaveis
spacing = 50

# Cabeçalho
header("Par ou Impar", spacing)

# Entrada de Dados
numero = int(input("Digite um número inteiro: "))

# Processamento & Saída de Dados
if numero % 2 == 0:
    highlight(str(f"{numero} é par!"), spacing)
else:
    highlight(str(f"{numero} é impar!"), spacing)
    
footer(spacing)