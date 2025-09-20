# Programa que da algumas infomações a patir do ano de nascimento

import functions as fn

# Variaveis
title = "Dados a partir do nascimento"
spacing = 50

year = 2025

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
birth_year = int(input("Digite seu ano de nascimento: "))

# Processamento de Dados | Diga se de passagem, ficou muitooo feio... tentar fazer melhor depois :(

age = year - birth_year

if age > 0 and age <= 12:
    lifes_stage = "Criança"
    vote = "Não permitida"
    drivers_license = "Não permitida"
elif age > 12 and age < 18:
    lifes_stage = "Adolescente"
    vote = "Não permitida"
    drivers_license = "Não permitida"
elif age >= 16 and age < 18:
    lifes_stage = "Adolescente"
    vote = "Facultativo"
    drivers_license = "Não permitida"
elif age >= 18 and age <= 59:
    lifes_stage = "Adulto"
    vote = "Obrigatoria"
    drivers_license = "Permitida"
elif age >= 60 and age < 70:
    lifes_stage = "Idoso"
    vote = "Obrigatoria"
    drivers_license = "Permitida"
elif age >= 70:
    lifes_stage = "Idoso"
    vote = "Facultativo"
    drivers_license = "Permitida"
else:
    pass

# Saída de Dados
fn.highlight(f"DADOS\n> Idade: {age}\n> Estágio da vida: {lifes_stage}\n> Votação: {vote}\n> Habilitação: {drivers_license}", spacing)
fn.footer(spacing)