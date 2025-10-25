# jogo entre dois usuários, um deles irá digitar um número (inteiro), e outro deve fazer chutes para acertar o número imaginado

from jmutils import *

# Variables
title, spacing = "⟪ Adivinhe o Número ⟫", 80

player_1, player_2 = "Jogador 1", "Jogador 2"

def play_game():
    attempts_init = 10
    attempts = attempts_init

    print(f"{"\n" * 200}")

    header_color(title, spacing, 'green')

    secret_number = int(input(f"{colors['red']}{player_1}{colors['reset']} digite um número secreto: "))

    print("\x1b[1A\x1b[2K" + f"{player_1} digite um número secreto: " + "*" * len(str(secret_number)))

    while True:
        print(f"\n> Tentativas: {"O " * attempts}{"Ø " * (attempts_init - attempts)}")

        guess = int(input(f"\n{colors['blue']}{player_1}{colors['reset']} digite seu {(attempts_init + 1) - attempts}º palpite: "))
        attempts -= 1

        if  attempts < 1:
            highlight(f"Game Over! {colors['red']}{player_1}{colors['reset']} ganhou!!!", spacing)

            break

        if guess == secret_number:
            highlight(f"Parabéns {colors['blue']}{player_2}{colors['reset']}! O número secrete realmente era {secret_number}", spacing)
            break
        elif guess > secret_number:
            highlight(f"Que tal um número MENOR", spacing)
        elif guess < secret_number:
            highlight(f"Que tal um número MAIOR", spacing)

def config_game():
    header("Configurações", spacing)

    print("Escolha uma das opções:\n\n1) Editar Nomes\n2) Voltar ao menu\n")

    entry = input("\nDigite o número da opção: ")

    match entry:
        case '1':
            names_editor()
        case '2':
            pass

def names_editor():
    header("Editar Nomes", spacing)
    print("Escolha uma das opções:\n\n1) Jogador 1\n2) Jogador 2\n3) Redefinir Nomes\n4) Voltar ao menu\n")

    entry = input("\nDigite o número da opção: ")

    match entry:
        case '1':
            header("Editar Nomes", spacing)

            player_1 = input("Digite o nome do Jogador 1: ")

            highlight("Nome editado com sucesso!", spacing)
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        
# Main
def main_game():

    while True:
        i, menu = 0, ["Play", "Tutorial", "Configurações", "Sair"]

        # Header
        header_color(title, spacing, 'green')

        print("Escolha uma das opções:\n")

        while i < len(menu):
            print(f"{colors['green']}{i + 1}){colors['reset']} {menu[i]}")
            i += 1

        # print("Escolha uma das opções:\n\n1) Play\n2) Tutorial\n3) Configurações\n4) Sair")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                play_game()
            case '2':
                header("Tutorial", spacing)
                print(f"{str("< Como o jogo funciona? >").upper()}\n\n- O Jogador 1 deve digitar um número inteiro secreto.\n- O Jogador 2 terá 10 tentativas para descobrir qual é esse número.\n- A cada tentativa, o jogo pode indicar se o palpite está acima ou abaixo do número correto.\n- Se o Jogador 2 acertar antes de esgotar as tentativas, ele vence.\n- Mas se não conseguir, o Jogador 1 vence a rodada.")
                footer(spacing)
            case '3':
                config_game()
            case '4':
                pass

        input("\nDigite ENTER para retornar ao menu.")

# MainLoop
main_game()