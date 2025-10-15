# Programa que calcula a media de 10 alunos

import functions as fn

database = {}
spacing  = 50

# Entradas de Dados
def calculate(amount):
    database.clear()

    for i in range(amount):
        print("-" * spacing)
        name = input(f"O nome do {i + 1}° aluno: ")
        print(" ")
        n1 = float(input(f"Digite a 1° nota: "))
        n2 = float(input(f"Digite a 2° nota: "))

        media = (n1 + n2) / 2
        
        status = "Aprovado!" if media >= 7 else "Reprovado!"

        database[i] = {"name" : name,  "media" : media, "status" : status}

        fn.highlight(f"MÉDIA\n > Aluno {i + 1}°: {name}\n L Média: {media}\n L Situação: {status}", spacing)

def view():
    for i in range(len(database)):
        fn.highlight(f"> Aluno {i + 1}°: {database[i]["name"]}\n L Média: {database[i]["media"]}\n L Situação: {database[i]["status"]}", spacing)

def mainloop():
    while True:
        fn.header("Calculadora de Médias", spacing)

        print("Escolha uma opção: ")
        print("1) Calcular Médias\n2) Histórico de Médias\n3) Sair\n")

        option = int(input("Digite o número da opção: "))

        match option:
            case 1:
                # Cabeçalho
                fn.header("Calculadora de Médias", spacing)

                # Entrada de Dados
                amount = int(input("Deseja calcular a média de quantos alunos? "))
                print(" ")
                
                # Processamento de Dados
                calculate(amount)

                # Finalizaçao
                fn.highlight("Todas as médias foram calculdadas com sucesso!", spacing)
            case 2:
                if len(database) == 0:
                    fn.highlight("Ainda não foram calculadas nenhuma média!", spacing)
                else:
                    # Cabeçalho
                    fn.highlight("Histórico de Médias", spacing)

                    # Saída de Dados
                    view()
            case 3:
                print("\nAté Mais! Fechando...")
                break

        input("\nPressione ENTER para retonar ao menu.")

mainloop()







