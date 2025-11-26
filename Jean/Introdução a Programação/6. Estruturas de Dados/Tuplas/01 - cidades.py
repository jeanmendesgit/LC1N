# Programa com uma tupla com o nome de cinco cidades que você gostaria de visitar.
# Em seguida imprima a primeira e última cidade da tupla.
# Verifique também se a cidade de Manaus está na tupla, usando in.

from jmutils import *

# VARIAVEIS _________________________________________________________________________________________________________________
title, spacing, color = "Cinco Cidades para Visitar", 50, 'green'

citys = ("Cidade 1", "Cidade 2", "Cidade 3", "Cidade 4", "Cidade 5")
first_city = citys[0]
last_city  = citys[len(citys) - 1]
manaus = "Sim" if "Manaus" in citys else "Não"

# SAÍDA DE DADOS ____________________________________________________________________________________________________________
header_color(title, spacing, color)

print(f"> Primeira cidade: {first_city}\n> Última cidade: . {last_city}\n> Manaus está? ... {manaus}")

footer(spacing)





