# Programa que o usuário diz quantas notas ele deseja inserir. Em seguida, calcula e exiba a média aritmética delas.

import functions as fn

# Variaveis
title, spacing = "Média de Notas", 50
notes, media, sum = [], 0, 0

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
amount = int(input("Digite quantas notas serão calculadas: "))

fn.line(spacing)

for i in range(amount):
    note = float(input(f"Digite a {i + 1}º nota: ").replace(',', '.'))
    notes.append(note)

# Processamento de Dados
for i in range(len(notes)):
    sum  += notes[i]

media = sum / amount

# Saída de Dados
fn.highlight(f"A média das {amount}º notas equivale a {media:.1f}",spacing)
fn.footer(spacing)
