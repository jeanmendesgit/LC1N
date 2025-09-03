# Tabuada.py

# Header
spacing = 50
title_1 = "Tabuada Python"
print("=" * spacing)
print("-" * spacing)
print(" " * (((spacing - len(title_1)) // 2) - 1),title_1)
print("-" * spacing)
print(" ")

# Amazenamento e Entrada de Dados
numero1 = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))

# Processamento dos Dados
soma          = numero1 + numero2
subtracao     = numero1 - numero2
multiplicacao = numero1 * numero2
divisao_float = numero1 / numero2
divisao_resto = numero1 % numero2
divisao_int   = numero1 // numero2
potenciacao   = numero1 ** numero2


# Main
title_2 = "Tabuada"
print("-" * spacing)
print(" " * (((spacing - len(title_2)) // 2) - 1),title_2)
print("-" * spacing)
print(" ")

# Saída de Dados
print("> Soma          -> ", numero1, " + ", numero2, "  = ", soma)
print("> Subtração     -> ", numero1, " - ", numero2, "  = ", subtracao)
print("> Multiplicação -> ", numero1, " * ", numero2, "  = ", multiplicacao)
print("> Divisão       -> ", numero1, " / ", numero2, "  = ", divisao_float)
print("> Resto         -> ", numero1, " % ", numero2, "  = ", divisao_resto)
print("> Resto Inteiro -> ", numero1, " // ", numero2, " = ", divisao_int)
print("> Potenciação   -> ", numero1, " ** ", numero2, " = ", potenciacao)
print("-" * spacing)









