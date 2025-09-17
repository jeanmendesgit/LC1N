# Programa que informa o peso ideal

import functions as fn

# Variaveis
title = "Peso Ideal"
spacing = 50

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados & Processamento de Dados & Saída de Dados
try:
    gender = input("Digite seu sexo (M/F): ").upper()
    height = float(input("Digite sua altura(m): ").replace(',', '.'))

    match gender:
        case 'M':
            ideal_weight = (72.7 * height) - 58
            fn.highlight(f"Seu peso ideal é {ideal_weight:.2f}", spacing)
        case 'F':
            ideal_weight = (62.1 * height) - 44.7
            fn.highlight(f"Seu peso ideal é {ideal_weight:.2f}", spacing)
except ValueError:
        fn.highlight(f"Entrada invalida!", spacing)
fn.footer(spacing)
    


