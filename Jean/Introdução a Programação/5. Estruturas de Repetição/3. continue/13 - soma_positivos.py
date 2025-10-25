# programa que some os 5 primeiros números positivos que o usuário digitar.

from jmutils import *

# Variaveis
title, spacing = "Soma dos 5 primeiros Positivos", 50

counter, numbers, total = 1, [], 0

line = True

# Cabeçalho
header(title, spacing)

# Entrada de Dados
while counter < 6:
    if line:
        if counter != 1:
            line(spacing)
    else:
        print(" ")

    entry = int(input(f"Digite o {counter}° número inteiro positivo: "))

    if entry < 0:
        highlight("Ops... esse numero não é positivo!", spacing)
        
        line = False

        continue
    
    numbers.append(entry)
    counter += 1
    line = True

# Processamento de Dados
for i in range(len(numbers)):
    total += numbers[i]

# Saída de Dados
highlight(f"Total: {total}", spacing)
footer(spacing)