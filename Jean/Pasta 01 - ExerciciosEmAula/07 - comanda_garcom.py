# Programa que informa os 10% do Garçom
#--------------------------------------#

import functions as fn

# Variaveis

percentage = 12

# Header
spacing = 50
fn.header("Restaurante", spacing)

# Entrada de Dados
valor_entry = float(input("Digite o valor da conta do cliente: "))


# Processamento
tip = (valor_entry / 100) * percentage
total = valor_entry + tip

tips_label = "10% do Garçom: "
tips_value = f" R$ {str(tip).replace(".", ",")}"

totals_label = "Valor total: "
totals_value = f" R$ {str(total).replace(".", ",")}"

# Saída de Dados
print(" ")
fn.header("Comanda", spacing)

print(f"{tips_label}{"." * int(spacing - len(tips_label) - len(tips_value))}{tips_value}")
print(f"{totals_label}{"." * int(spacing - len(totals_label) - len(totals_value))}{totals_value}")

fn.footer(spacing)