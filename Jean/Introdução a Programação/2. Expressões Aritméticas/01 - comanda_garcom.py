# Programa que informa os 10% do Garçom
#--------------------------------------#

from jmutils import *

# Variaveis

percentage = 10

# Header
spacing = 50
header("Restaurante", spacing)

# Entrada de Dados
valor_entry = float(input("Digite o valor da conta do cliente: "))


# Processamento
tip = (valor_entry / 100) * percentage
total = valor_entry + tip

tips_label = f"{percentage}% do Garçom: "
tips_value = f" R$ {str(tip).replace(".", ",")}"

totals_label = "Valor total: "
totals_value = f" R$ {str(total).replace(".", ",")}"

# Saída de Dados
print(" ")
header("Comanda", spacing)

print(f"{tips_label}{"." * int(spacing - len(tips_label) - len(tips_value))}{tips_value}")
print(f"{totals_label}{"." * int(spacing - len(totals_label) - len(totals_value))}{totals_value}")

footer(spacing)