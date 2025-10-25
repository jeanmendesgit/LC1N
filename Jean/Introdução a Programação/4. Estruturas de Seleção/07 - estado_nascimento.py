# Programa que informa a nomeação a partir da sigla do estado

from jmutils import *

# Variaveis
title = "Gentílicos Brasileiros"
spacing = 50

database = {
    "MG": "Mineiro",
    "SP": "Paulista",
    "RJ": "Carioca",
    "ES": "Capixaba",
    "PR": "Paranaense",
    "SC": "Catarinense",
    "RS": "Gaúcho",
    "DF": "Brasiliense",
    "GO": "Goiano",
    "MT": "Mato-grossense",
    "MS": "Sul-mato-grossense",
    "TO": "Tocantinense",
    "RO": "Rondoniense",
    "AC": "Acriano",
    "AM": "Amazonense",
    "RR": "Roraimense",
    "PA": "Paraense",
    "AP": "Amapaense",
    "MA": "Maranhense",
    "PI": "Piauiense",
    "CE": "Cearense",
    "RN": "Potiguar",
    "PB": "Paraibano",
    "PE": "Pernambucano",
    "AL": "Alagoano",
    "SE": "Sergipano",
    "BA": "Baiano"
}

# Cabeçalho
header(title, spacing)

# Entrada de Dados
initialism = input("Digite apenas a sigla do estado: ").upper()

# Saída de Dados
try:
    highlight(f"Quem nasce em {initialism} é {database[initialism]}!", spacing)
except KeyError:
    highlight(f"Estado não catalogado ou inexistente :(", spacing)

footer(spacing)
