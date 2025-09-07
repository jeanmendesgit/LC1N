# Programa que converte temperaturas

import functions as fn

# Variaveis

spacing = 40

# Funcoes
def fahrenheit(value):
    fahrenheit_value = (value * (9/5)) + 32
    return fahrenheit_value

def celsius(value):
    celsius_value = (value - 32) / (9/5)
    return celsius_value

# Main
def main():
    while True:
        # Header
        fn.header("Conversor de Temperturas", spacing)

        print("Digite o número da opção:\n1) Celsius -> Fahrenheit\n2) Fahrenheit -> Celsius\n3) Sair\n")

        users_entry = input("Digite o número da opção: ")

        if users_entry not in ['1', '2', '3']:
            print("\nErro: Digite uma opção válida!")
        else:
            match int(users_entry):
                case 1:
                    celsius_entry = input("\nDigite a temperatura em Celsius: ")

                    if not celsius_entry.isdigit():
                        print("\n> Inválido! Digite apenas números!")
                    else:
                        celsius_out = f"{celsius_entry}°C equivale a {fahrenheit(float(celsius_entry)):.2f}°F"
                        
                        fn.highlight(celsius_out, spacing)
                case 2:
                    fahrenheit_entry = input("\nDigite a temperatura em Fahrenheit: ")

                    if not fahrenheit_entry.isdigit():
                        print("\n> Inválido! Digite apenas números!")
                    else:
                        fahrenheit_out = f"{fahrenheit_entry}°F equivale a {celsius(float(fahrenheit_entry)):.2f}°C"
                        
                        fn.highlight(fahrenheit_out, spacing)
                case 3:
                    print(" ")
                    print("-" * spacing)
                    print("\n> Programa Finalizado! Até mais...")
                    fn.footer(spacing)
                    break

        input("\nPressione ENTER para retonar ao menu.")
        
# Start
main()