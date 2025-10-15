# Programa que mostra a tabuada de multiplicação de um número, de 1 a 10.

import functions as fn

# Amazenamento de Dados
title, spacing = "Tabuada Python", 50
contador = 1

# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
numero = int(input("Digite um número da tabuada: "))

# Processamento e Saída de Dados
fn.line(spacing)

while contador < 11:
    print(f"{numero} x {contador} = {numero * contador}")

    contador += 1

fn.footer(spacing)