# Programa que mostra a tabuada de multiplicação de um número, de 1 a 10.

from jmutils import *

# Amazenamento de Dados
title, spacing = "Tabuada Python", 50
contador = 1

# Cabeçalho
header(title, spacing)

# Entrada de Dados
numero = int(input("Digite um número da tabuada: "))

# Processamento e Saída de Dados
line(spacing)

while contador < 11:
    print(f"{numero} x {contador} = {numero * contador}")

    contador += 1

footer(spacing)