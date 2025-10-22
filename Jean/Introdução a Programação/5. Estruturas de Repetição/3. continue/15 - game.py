# jogo entre dois usuários, um deles irá digitar um número (inteiro), e outro deve fazer chutes para acertar o número imaginado

import functions as fn

# Variables
title, spacing = "|?| Adivinhe o Número |?|", 50

player_1, player_2 = "Jogador 1", "Jogador 2"

def play_game():
    attempts = 10

    print(f"{"\n" * 200}")

    fn.header(title, spacing)

    secret_number = int(input(f"{player_1} digite um número secreto: "))

    print(f"{"\n" * 200}")

    while attempts > 0:
        
        print(f"\n> Tentativas: {"O " * attempts}{"Ø " * (10 - attempts)}")

        guess = int(input(f"\n{player_2} digite seu palpite: "))
        attempts -= 1

        if guess == secret_number:
            fn.highlight(f"Parabéns {player_2}! O número realmente era {secret_number}", spacing)
            break
        elif guess > secret_number:
            fn.highlight(f"Que tal um número MENOR", spacing)
        elif guess < secret_number:
            fn.highlight(f"Que tal um número MAIOR", spacing)

# Main
def game():
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
                pass
            case '4':
                pass

        input("\nDigite ENTER para retornar ao menu.")


# MainLoop
game()