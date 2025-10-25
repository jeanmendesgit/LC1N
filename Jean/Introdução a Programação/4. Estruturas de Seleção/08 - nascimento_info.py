# Programa que da algumas infomações a patir do ano de nascimento

from jmutils import *

# Variaveis
title = "Dados a partir do nascimento"
spacing = 50
year = 2025

# Cabeçalho
header(title, spacing)

# Entrada de Dados
birth = int(input("Digite seu ano de nascimento: "))

# Processamento de Dados
age = year - birth

if age > 0 and age <= 12:
    age_range = "Criança"
elif age > 12 and age < 18:
    age_range = "Adolescente"
elif age >= 18 and age <= 59:
    age_range = "Adulto"
elif age >= 60:
    age_range = "Idoso"

vote    = "Permitida" if age >= 16 else "Não permitida"
license = "Permitida" if age >= 18 else "Não permitida"

# Saída de Dados
highlight(f"DADOS\n> Idade: ......... {age}\n> Faixa Etária: .. {age_range}\n> Votação: ....... {vote}\n> Habilitação: ... {license}", spacing)
footer(spacing)