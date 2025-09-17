# Programa que infoma a nomeação apartir da sigla do estado

import functions as fn

# Variaveis
title = "Nomeção por Estado"
spacing = 50

database = [{"MG" : "Mineiro",
             "SP" : "Paulista",
             "RJ" : "Carioca",
             "ES" : "Capixaba"}]

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
acronym = input("Digite a sigla do seu estado: ").upper()

# Saída de Dados
try:
    fn.highlight(f"Você é {database[0][acronym]}!", spacing)
except KeyError:
    fn.highlight(f"Estado não catalogado :(", spacing)

fn.footer(spacing)
