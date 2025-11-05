from jmutils import *

class Game:
    def __init__(self):
        self.title = "⟪ Adivinhe o Número ⟫"
        self.spacing = 80
        self.player_1 = "Jogador 1"
        self.player_2 = "Jogador 2"

        self.main_color = 'green'
        self.player_1_color = 'red'
        self.player_2_color = 'blue'

    # Menu
    def main(self):
        while True:
            header_color(self.title, self.spacing, self.main_color)
            print("Escolha uma das opções:\n")
            options = ["Play", "Tutorial", "Configurações", "Sair"]

            for i, item in enumerate(options, start=1):
                print(f"{colors[self.main_color]}{i}){colors['reset']} {item}")

            entry = input("\nDigite o número da opção: ")

            match entry:
                case '1':
                    self.play()
                case '2':
                    self.tutorial()
                case '3':
                    self.config()
                case '4':
                    highlight("Saindo do jogo...", self.spacing)
                    break

            input(f"\nDigite {colors[self.main_color]}ENTER{colors['reset']} para retornar ao menu.\n")

    # Game
    def play(self):
        attempts_init = 10
        attempts = attempts_init

        print("\n" * 200)
        header_color(self.title, self.spacing, self.main_color)

        secret_number = int(input(f"{colors[self.player_1_color]}{self.player_1}{colors['reset']} digite um número secreto: "))

        print("\n" * 1000)
        print(f"{colors[self.player_1_color]}{self.player_1}{colors['reset']} digite um número secreto: {'*' * len(str(secret_number).replace('-', ''))}")
        line(self.spacing)

        while attempts > 0:
            print(f"\n> Tentativas: {'O ' * attempts}{'Ø ' * (attempts_init - attempts)}")
            guess = int(input(f"\n{colors[self.player_2_color]}{self.player_2}{colors['reset']} digite seu {(attempts_init + 1) - attempts}º palpite: "))
            attempts -= 1

            if guess == secret_number:
                highlight(f"Parabéns {colors[self.player_2_color]}{self.player_2}{colors['reset']}! O número era {secret_number}", self.spacing)
                return
            elif guess > secret_number:
                highlight("Tente um número MENOR", self.spacing)
            else:
                highlight("Tente um número MAIOR", self.spacing)

        highlight(f"Game Over! {colors[self.player_1_color]}{self.player_1}{colors['reset']} venceu!", self.spacing)

    # Tutorial
    def tutorial(self):
        header("Tutorial", self.spacing)
        print(f"< COMO O JOGO FUNCIONA? >\n\n"
              "- O Jogador 1 digita um número secreto.\n"
              "- O Jogador 2 tem 10 tentativas para adivinhar.\n"
              "- O jogo informa se o palpite está acima ou abaixo.\n"
              "- Se acertar antes das tentativas acabarem, vence.\n"
              "- Caso contrário, o Jogador 1 vence.")
        footer(self.spacing)

    # Configurações
    def config(self):
        header("Configurações", self.spacing)
        print("1) Editar Nomes\n2) Voltar ao menu\n")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                self.edit_names()
            case '2':
                pass
            case _:
                pass

    def edit_names(self):
        header("Editar Nomes", self.spacing)
        print("1) Jogador 1\n2) Jogador 2\n3) Redefinir Nomes\n4) Voltar\n")

        entry = input("\nEscolha: ")
        match entry:
            case '1':
                line(self.spacing)

                self.player_1 = input("Novo nome do Jogador 1: ")

                highlight("Nome editado!", self.spacing)
            case '2':
                line(self.spacing)

                self.player_2 = input("Novo nome do Jogador 2: ")
                
                highlight("Nome editado!", self.spacing)
            case '3':
                self.player_1, self.player_2 = "Jogador 1", "Jogador 2"
                highlight("Nomes redefinidos!", self.spacing)

if __name__ == "__main__":
    game = Game()
    game.main()