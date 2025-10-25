# Program que informa se uma letra é uma vogal uma consoante

from jmutils import *

# Variaveis
title = "Vogal ou Consoante?"
spacing = 50
vowels_list = ['a', 'e', 'i', 'o', 'u']

# Cabeçalho
header(title, spacing)

# Entrada de dados
entry_char = input("Digite um letra: ").lower()

# Processamento & Saída de dados
highlight(f"{entry_char.upper()} é uma vogal!", spacing) if entry_char in vowels_list else highlight(f"{entry_char.upper()} é uma consoante!", spacing)
footer(spacing)
    