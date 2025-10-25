# Calculadora Simples

from jmutils import *

# Variaveis
title, spacing = "Calculadora Simples", 50

def calc(option):
    line(spacing)

    # Entrada de Dados
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))

    # Processamento de Dados
    match option:
        case '1':
            value, label = n1 + n2, "+"
        case '2':
            value, label = n1 - n2, "-"
        case '3':
            value, label = n1 / n2, "÷"
        case '4':
            value, label = n1 * n2, "x"
    
    # Saída de Dados
    highlight(f"{n1} {label} {n2} = {value}", spacing) if option != '3' else highlight(f"{n1} {label} {n2} = {value:.1f}", spacing)

# Main
def main():
    while True:
        header(title, spacing)

        print("Escolha uma operação entre dois números: \n\n1) Somar       (+)\n2) Subtrair    (-)\n3) Dividir     (÷)\n4) Multiplicar (x)\n5) Sair")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                calc(entry)
            case '2':
                calc(entry)
            case '3':
                calc(entry)
            case '4':
                calc(entry)
            case '5':
                highlight("Encerrando o Programa", spacing)
            case _:
                highlight("Digite uma opção válida!", spacing)
                break
        
        input("\nDigite ENTER para voltar ao menu.")

        line(spacing)

# Start
main()
