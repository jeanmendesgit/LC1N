# Program que informa se uma letra é uma vogal uma consoante

import functions as fn

# Variaveis
title = "Vogal ou Consoante?"
spacing = 50
vowels_list = ['a', 'e', 'i', 'o', 'u']

# Cabeçalho
fn.header(title, spacing)

# Entrada de dados
entry_char = input("Digite um letra: ").lower()

# Processamento & Saída de dados
fn.highlight(f"{entry_char.upper()} é uma vogal!", spacing) if entry_char in vowels_list else fn.highlight(f"{entry_char.upper()} é uma consoante!", spacing)
fn.footer(spacing)
    