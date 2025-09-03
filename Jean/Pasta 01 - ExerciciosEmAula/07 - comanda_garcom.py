# Programa que informa os 10% do Garçom
#--------------------------------------#

import functions as fn

# Variaveis

percentage = 10

# Header
spacing = 50
fn.header("Restaurante", spacing)

# Entrada de Dados & Processamento
valor_entry = float(input("Digite o valor da conta do cliente: "))
print(" ")
tip = (valor_entry / 100) * percentage
all = valor_entry + tip


# Saída de Dados
title_2 = "Comanda"
print("-" * spacing)
print(" " * (((spacing - len(list(title_2))) // 2) - 1),title_2)
print("-" * spacing)

print(" ")
print("10% do Garçom:", "." * 24, "R$",tip)
print("Valor total:", "." * 26, "R$",all)
print(" ")
print("-" * spacing)
print("=" * spacing)