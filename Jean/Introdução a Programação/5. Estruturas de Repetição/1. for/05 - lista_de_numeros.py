# Programa que imprime imprimi todos os números de 1 até o número que o usuário digitou.

from jmutils import *

# Variaveis

title, spacing = "Lista de Números", 50

# Cabeçalho

header(title, spacing)

# Entrada de Dados

valor = int(input("Digite o tamanho da lista de números: "))

# Saida de Dados
header(title, spacing)

for i in range(1, valor + 1):
    print(f"{i}º")

print("\n✓ Lista de números concluida!")
footer(spacing)