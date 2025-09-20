# Programa que imforma par ou impar

import functions as fn

# Variaveis
spacing = 50

# Cabeçalho
fn.header("Par ou Impar", spacing)

# Entrada de Dados
numero = int(input("Digite um número inteiro: "))

# Processamento & Saída de Dados
if numero % 2 == 0:
    fn.highlight(str(f"{numero} é par!"), spacing)
else:
    fn.highlight(str(f"{numero} é impar!"), spacing)
    
fn.footer(spacing)