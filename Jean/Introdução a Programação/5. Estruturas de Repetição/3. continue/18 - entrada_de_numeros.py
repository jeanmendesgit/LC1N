# Algoritmo que le vários números até obter o finalizador 0, e ao final indicar:
# - Quantos números foram lidos
# - Quantos números lidos são primos

from jmutils import *

# VARIAVEIS
title, spacing, main_color = "Leitor de Números", 150, 'green'


# FUNÇÕES
def is_prime(number: int):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** .5) + 1, 2):
        if number % i == 0:
            return False
    return True

def program():
    counter = 1
    numbers = list()
    primes  = list()

    while True:
        print(f"{colors['black']}> Digite 0 para finalizar a contagem.{colors['reset']}\n")

        try:
            entry = int(input(f"Digite o {counter}º número: "))
        except ValueError:
            highlight("Entrada inválida, tente novamente!", spacing)
            continue

        if entry in numbers:
            highlight("Número já existente, tente novamente!", spacing)
            continue

        line(spacing)

        if entry == 0:
            break
        
        counter += 1
        numbers.append(entry)
        if is_prime(entry): primes.append(entry)
    
    print("\n" * spacing)
    header_color("Todos os Números", spacing, main_color)
    print(f"Números: {numbers}")
    print(f"\nTotal: {len(numbers)}")
    print()
    highlight_color("Todos os Primos", spacing, main_color)
    print(f"Primos: {primes}")
    print(f"\nTotal: {len(primes)}")
    
# SAÍDA DE DADOS
header_color(title, spacing, main_color)
program()
footer(spacing)
