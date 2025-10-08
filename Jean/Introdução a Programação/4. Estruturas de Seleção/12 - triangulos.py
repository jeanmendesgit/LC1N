# Programa que dado A, B e C se constitui um triangulo ou nao e qual seria

import functions as fn

# Variaveis
title = "Validando e Classificando Triângulos"
spacing = 80
numbers = ["Ø"]
triangle = False


# Cabeçalho
fn.header(title, spacing)

# Entrada de Dados
for i in range(3):
    numbers.append(int(input(f"Digite o valor do {i + 1}° lado: ")))
    
# Processamento & Saída de Dados
if numbers[1] < numbers[2] + numbers[3] and numbers[2] < numbers[1] + numbers[3] and numbers[3] < numbers[1] + numbers[2]:
    triangle = True
else:
    fn.highlight("Os valores infomados não constituem um triângulo.",spacing)

if triangle:
    # Equilátero
    if numbers[1] == numbers[2] and numbers[2] == numbers[3]:
        classification = "Equilátero"
    
    # Isósceles
    if (numbers[1] == numbers[2] and numbers[2] != numbers[3]) or (numbers[2] == numbers[3] and numbers[3] != numbers[1]) or (numbers[3] == numbers[1] and numbers[1] != numbers[2]):
        classification = "Isósceles"
    
    # Escaleno
    if numbers[1] != numbers[2] and numbers[1] != numbers[3] and numbers[2] != numbers[3]:
        classification = "Escaleno"
    
    fn.highlight(f"| A = {numbers[1]} | B = {numbers[2]} | C = {numbers[3]} | constituem um triângulo « {classification.upper()} »",spacing)

fn.footer(spacing)
        
        









