# Uma outra tupla com informações sobre vocês: seu nome, idade cidade.

from jmutils import *

# VARIAVEIS _________________________________________________________________________________________________________________
title, spacing, color = "Minhas Informações", 50, 'green'

I = ("Jean Mendes", 21, "Afogados da Ingazeira")

# SAÍDA DE DADOS ____________________________________________________________________________________________________________
header_color(title, spacing, color)

print(f"> Nome:   {I[0]}\n> Idade:  {I[1]}\n> Cidade: {I[2]}")

footer(spacing)

