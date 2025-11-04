# pip install -i https://test.pypi.org/simple/ jmutils

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Programa que seja capaz de concluir qual dentre os seguintes animais foi escolhido, através de perguntas e respostas.
# Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.
# Utilize as seguintes classificações, Exemplo:
# É mamífero? Sim
# É quadrúpede? Sim
# É carnívoro? Não
# É herbívoro? Sim
# Então o animal que você pensou é o: cavalo

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

from jmutils import *

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# VARIAVEIS
title, spacing, main_color = "Descobrindo o Animal Segredo", 80, 'green'

animal = '?'

def play():
    print()
    header_color("Pense em um Animal", spacing, main_color)

    while True:
        print("Possiveis Animais: 🦁 🐴 👨 🐵 🦇 🐋 🦤 🐧 🦆 🦅 🐢 🐊 🐍")

        line_color(spacing, main_color)

        entry = input("Pertence aos mamíferos? (s/n): ").lower()

        if entry == 's':
            line_color(spacing, main_color)

            entry = input("Pertence aos quadrupedes? (s/n): ").lower()

            if entry == 's':
                line_color(spacing, main_color)

                entry = input("Pertence aos carnívoros? (s/n): ").lower()

                animal = "Leão" if entry == 's' else "Cavalo"
                break
            else:
                line_color(spacing, main_color)

                entry = input("Pertence aos bípedes? (s/n): ").lower()

                if entry == 's':
                    line_color(spacing, main_color)
                    
                    entry = input("Pertence aos onívoros? (s/n): ").lower()

                    animal = "Homem" if entry == 's' else "Macaco"
                    break
                else:
                    line_color(spacing, main_color)
                    
                    entry = input("Pertence aos voadores? (s/n): ").lower()

                    animal = "Morcego" if entry == 's' else "Baleia"
                    break
        else:
            line_color(spacing, main_color)

            entry = input("Pertence as aves? (s/n): ").lower()

            if entry == 's':
                line_color(spacing, main_color)

                entry = input("Pertence as não-voadoras? (s/n): ").lower()

                if entry == 's':
                    line_color(spacing, main_color)

                    entry = input("Pertence as tropicais? (s/n): ").lower()

                    animal = "Avestruz" if entry == 's' else "Pinguim"
                    break
                else:
                    line_color(spacing, main_color)

                    entry = input("Pertence as nadadoras? (s/n): ").lower()

                    animal == "Pato" if entry == 's' else "Águia"
                    break
            else:
                line_color(spacing, main_color)

                entry = input("Pertence aos com casco? (s/n): ").lower()

                if entry == 's':
                    animal = "Tartagura"
                    break
                else:
                    line_color(spacing, main_color)

                    entry = input("Pertence aos carnívoros? (s/n): ").lower()

                    animal = "Crocodilo" if entry == 's' else "Cobra"
                    break

    highlight_color(f"{animal} é o animal que você pensou! :)", spacing, main_color)

def tutorial():
    print()
    header_color("Tutorial", spacing, main_color)

    print(f"{colors[main_color]}< COMO O JOGO FUNCIONA? >{colors['reset']}\n\n"
            "- O jogo faz perguntas sobre as características de um animal.\n"
            "- Você deve responder com “s”(sim) ou “n”(não).\n"
            "- Com base nas suas respostas, o programa tentará descobrir qual animal você está pensando entre as opções disponíveis:\n"
            "- Leão, Cavalo, Homem, Macaco, Morcego, Baleia, Avestruz, Pinguim, Pato, Águia, Tartaruga, Crocodilo e Cobra.\n"
            "- No final, o programa exibirá o animal que mais combina com as respostas dadas.")
    
    footer(spacing)

def program():
    while True:
        print()
        header_color(title, spacing, main_color)
        print("Escolha uma das opções:\n")
        options = ["Play", "Tutorial", "Sair"]

        for i, item in enumerate(options, start=1):
            print(f"{colors[main_color]}{i}){colors['reset']} {item}")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                play()
            case '2':
                tutorial()
            case '3':
                highlight_color("Saindo do jogo...", spacing, main_color)
                break

        input(f"Digite {colors[main_color]}ENTER{colors['reset']} para retornar ao menu.")

if __name__ == "__main__":
    program()
