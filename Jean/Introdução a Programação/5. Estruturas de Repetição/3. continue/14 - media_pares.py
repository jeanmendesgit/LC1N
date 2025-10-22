# programa que raliza a media dos 5 primeiros números pares que o usuário digitar.

import functions as fn

# Variaveis
title, spacing = "Soma dos 5 primeiros Positivos", 50

counter, numbers, total, media = 1, [], 0, 0

line = True

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
while True:
    if line:
        if counter != 1:
            fn.line(spacing)
    else:
        print(" ")

    entry = int(input(f"Digite o {counter}° número par: "))

    if entry == 0:
        break

    if entry % 2 != 0:
        fn.highlight("Ops... esse numero não é par!", spacing)
        
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
    fn.highlight(f"Total: {int(media)}", spacing)
else:
    fn.highlight(f"Total: {media:.2f}", spacing)

fn.footer(spacing)