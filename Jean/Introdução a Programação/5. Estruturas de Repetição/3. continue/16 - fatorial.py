# programa que pede um número do usuário e calcule o fatorial desse número

from jmutils import *

# Variables
title, spacing = "Calculadora de Fatorial", 60
menu = ["Calcular Fatorial", "Sair"]
main_color = 'green'

# Functions
def calculate_factorial():
    line(spacing)

    # Entrada de Dados
    number = int(input("Digite o número: "))
    factorial = number

    # Processamento de Dados
    for i in range(number - 1, 1, -1):
        factorial *= i
    
    # Saída de Dados
    highlight_color(f"{number}! = {factorial}", spacing, main_color)
    
def main():
    while True:
        print()
        header_color(title, spacing, main_color)

        print("Escolha uma opção:\n")

        for i, option in enumerate(menu, start=1):
            print(f"{colors[main_color]}{i}){colors['reset']} {option}")
        
        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                calculate_factorial()
            case '2':
                highlight_color(f"Programa Encerrado...", spacing, main_color)
                break
            case _:
                highlight_color("Opção inválida! Tente novamente...", spacing, 'red')
        
        input(f"\nAperte {colors[main_color]}ENTER{colors['reset']} para retonar ao menu.")

# Start
main()





