# programa que raliza a media dos 5 primeiros números pares que o usuário digitar.

from jmutils import *

# Variaveis
title, spacing = "Soma dos 5 primeiros Positivos", 50

counter, numbers, total, media = 1, [], 0, 0

line = True

# Cabeçalho
header(title, spacing)

# Entrada de Dados
while True:
    if line:
        if counter != 1:
            line(spacing)
    else:
        print(" ")

    entry = int(input(f"Digite o {counter}° número par: "))

    if entry == 0:
        break

    if entry % 2 != 0:
        highlight("Ops... esse numero não é par!", spacing)
        
        line = False

        continue
    
    numbers.append(entry)
    counter += 1
    line = True

# Processamento de Dados
size = len(numbers)

for i in range(size):
    total += numbers[i]

media = total / size

# Saída de Dados
if media % 1 == 0:
    highlight(f"Total: {int(media)}", spacing)
else:
    highlight(f"Total: {media:.2f}", spacing)

footer(spacing)