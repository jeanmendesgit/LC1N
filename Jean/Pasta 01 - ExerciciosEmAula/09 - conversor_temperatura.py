# Programa que converte temperaturas

import functions as func

# Variaveis

spacing = 50

# Funcoes
def celsius(value):
    fahrenheit = (value * (9/5)) + 32
    return fahrenheit

def fahrenheit(value):
    celsius = (value - 32) * (9/2)

# Main
def main():
    while True:
        # Header
        func.header("Conversor de Temperturas", spacing)

        print("Digite o número da opção:")
        print("1) Celsius ⇥ Fahrenheit\n2) Fahrenheit ⇥ Celsius\n")

        users_entry = input("Digite o número da opção: ")

        if users_entry not in ['1', '2']:
            print("Erro: Opção Invalida!")
            main()
        
        match int(users_entry):
            case 1:
                celsius_entry = input("Digite a temperatura em Celsius: ")

                # Tratamento de Dados: Vazio...

                print(f"{celsius_entry}°C em Fahrenheit {celsius(float(celsius_entry))}°F")
            case 2:
                fahrenheit_entry = input("Digite a temperatura em Fahrenheit: ")

                # Tratamento de Dados: Vazio...

                print()

        input("")
# Start
    
main()






