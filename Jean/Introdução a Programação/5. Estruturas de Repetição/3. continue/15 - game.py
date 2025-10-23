# jogo entre dois usuários, um deles irá digitar um número (inteiro), e outro deve fazer chutes para acertar o número imaginado

import functions as fn

# Variables
title, spacing = "|?| Adivinhe o Número |?|", 80

player_1, player_2 = "Jogador 1", "Jogador 2"

def play_game():
    attempts_init = 10
    attempts = attempts_init

    print(f"{"\n" * 200}")

    fn.header(title, spacing)

    secret_number = int(input(f"{player_1} digite um número secreto: "))

    print(f"{"\n" * 200}")

    while True:
        print(f"\n> Tentativas: {"O " * attempts}{"Ø " * (attempts_init - attempts)}")

        guess = int(input(f"\n{player_2} digite seu {(attempts_init + 1) - attempts}º palpite: "))
        attempts -= 1

        if  attempts < 1:
            fn.highlight(f"Game Over! {player_1} ganhou!!!", spacing)

            break

        if guess == secret_number:
            fn.highlight(f"Parabéns {player_2}! O número secrete realmente era {secret_number}", spacing)
            break
        elif guess > secret_number:
            fn.highlight(f"Que tal um número MENOR", spacing)
        elif guess < secret_number:
            fn.highlight(f"Que tal um número MAIOR", spacing)

def config_game():
    fn.header("Configurações", spacing)

    print("Escolha uma das opções:\n\n1) Editar Nomes\n2) Voltar ao menu\n")

    entry = input("\nDigite o número da opção: ")

    match entry:
        case '1':
            names_editor()
        case '2':
            pass

def names_editor():
    fn.header("Editar Nomes", spacing)

    print("Escolha uma das opções:\n\n1) Jogador 1\n2) Jogador 2\n3) Redefinir Nomes\n4) Voltar ao menu\n")

    entry = input("\nDigite o número da opção: ")

    match entry:
        case '1':
            fn.header("Editar Nomes", spacing)

            player_1 = input("Digite o nome do Jogador 1: ")

            fn.highlight("Nome editado com sucesso!", spacing)
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        
# Main
def main_game():
    while True:
        # Header
        fn.header(title, spacing)

        print("\nEscolha uma das opções:\n\n1) Play\n2) Tutorial\n3) Configurações\n4) Sair")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                play_game()
            case '2':
                fn.line(spacing)
                print("< Como o jogo funciona? > \n\nO Jogador 1 deve digitar um número inteiro e o\nJogador 2 terá 10 tentativas para acertar.")
                fn.line(spacing)
            case '3':
                config_game()
            case '4':
                pass

        input("\nDigite ENTER para retornar ao menu.")

# MainLoop
main_game()