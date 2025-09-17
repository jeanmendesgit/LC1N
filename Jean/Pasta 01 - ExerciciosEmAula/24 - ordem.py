# Program que ordena números

import functions as fn

# Variaveis
entry_number = []
spacing = 50

# Cabecalho
fn.header("Ordenação de 3 Números", spacing)

# Entrada de dados
for i in range(3):
    entry_number.append(int(input(f"Digite o {i + 1}° número: ")))
    
# Processamento de dados
"""
(̲3 x ̲2 x ̲1) v 3! → 6

|1| (1, 2, 3)
|2| (1, 3, 2)
|3| (2, 1, 3)
|4| (2, 3, 1)
|5| (3, 1, 2)
|6| (3, 2, 1)

"""

if   entry_number[0] <= entry_number[1] and entry_number[1] <= entry_number[2]:
    numbers = [entry_number[0], entry_number[1], entry_number[2]]
elif entry_number[0] <= entry_number[2] and entry_number[2] <= entry_number[1]:
    numbers = [entry_number[0], entry_number[2], entry_number[1]]
elif entry_number[1] <= entry_number[0] and entry_number[0] <= entry_number[2]:
    numbers = [entry_number[1], entry_number[0], entry_number[2]]
elif entry_number[1] <= entry_number[2] and entry_number[2] <= entry_number[0]:
    numbers = [entry_number[1], entry_number[2], entry_number[0]]
elif entry_number[2] <= entry_number[0] and entry_number[0] <= entry_number[1]:
    numbers = [entry_number[2], entry_number[0], entry_number[1]]
elif entry_number[2] <= entry_number[1] and entry_number[1] <= entry_number[0]:
    numbers = [entry_number[2], entry_number[1], entry_number[0]]
else:
    pass

# Saída de Dados
fn.highlight(f"Ordem Crescente: {numbers[0]}, {numbers[1]}, {numbers[2]}", spacing)
fn.footer(spacing)