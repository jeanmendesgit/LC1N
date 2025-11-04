# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Programa que recebe a idade, a altura e o peso de várias pessoas. Calcula e mostra:
# - A quantidade de pessoas com idade superior a 50 anos;
# - A média das alturas das pessoas com idade entre 10 e 20 anos;
# - A percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
# - Qual a opção de saída do programa

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

from jmutils import *

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# VARAIAVEIS
title, spacing, main_color = "Calculadora de Estatísticas", 100, 'green'

database = []

main_menu = [{'option' : "Adicionar Pessoas",       'title' : "Adicionar Pessoas"},
             {'option' : "Visualizar Estatísticas", 'title' : "Estatísticas"},
             {'option' : "Sair", 'title' : "Sair do Programa"}]

questions = [{'key' : 'name',   'label' : "o nome",      'type' : 'str'},
             {'key' : 'age',    'label' : "a idade",     'type' : 'int'},
             {'key' : 'height', 'label' : "a altura(m)", 'type' : 'float'},
             {'key' : 'weight', 'label' : "o peso(kg)",  'type' : 'float'}]

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# FUNCOES
def program():
    while True:
        print()
        header_color(title, spacing, main_color)

        print("Escolha uma opção:\n")

        for i in range(len(main_menu)):
            print(f"{colors[main_color]}{i + 1}){colors['reset']} {main_menu[i]['option']}")

        entry = input("\nDigite o número da opção: ")

        match entry:
            case '1':
                add(entry)
            case '2':
                average(entry)
            case '3':
                header_color(main_menu[(int(entry) - 1)]['title'], spacing, main_color)

                entry = input("Deseja realmente encerrar o programa? (y/n): ").lower()

                if entry == 'y':
                    highlight_color("Até mais... Programa encerrado com sucesso!", spacing, main_color)
                    break
        
        input(f"\nPressione {colors[main_color]}ENTER{colors['reset']} para retonar ao menu.")

def add(entry):
    print()
    header_color(main_menu[int(entry) - 1]['title'], spacing, main_color)

    while True:
        questions_entry = {}

        print(f"{colors['black']}{colors['dim']} > Digite {colors['normal']}sair{colors['dim']} no campo abaixo para finalizar!{colors['normal']}{colors['reset']}\n")

        for i in range(len(questions)):
            match questions[i]['type']:
                case 'str':
                    questions_entry.update({questions[i]['key'] : input(f"Digite {questions[i]['label']} da pessoa: ")}), print()
                case 'int':
                    questions_entry.update({questions[i]['key'] : int(input(f"Digite {questions[i]['label']} da pessoa: "))}), print()
                case 'float':
                    questions_entry.update({questions[i]['key'] : float(input(f"Digite {questions[i]['label']} da pessoa: ").replace(',', '.'))}), print()
                
            if questions_entry['name'].lower() == 'sair':
                break

        if questions_entry['name'].lower() == 'sair':
                highlight_color("Adição finalizada!", spacing, main_color)
                break
                    
        database.append(questions_entry)

        highlight_color("Pessoa adicionada com sucesso!", spacing, main_color)

def average(entry):
    print()
    header_color(main_menu[int(entry) - 1]['title'], spacing, main_color)

    if len(database) == 0:
        print(f"{colors[main_color]}> Nenhuma pessoa adicionada!{colors['reset']}")
        return
    
    elderly_person, percentage_elderly_person = 0, 0
    counter_height, total_height, average_height = 0, 0, 0
    counter_weight, percentage_weight = 0, 0
    
    # Processamento
    for i in range(len(database)):
        if database[i]['age'] >= 50:
            elderly_person += 1
        
        if database[i]['age'] >= 10 and database[i]['age'] <= 20:
            total_height += database[i]['height']
            counter_height += 1

        if database[i]['weight'] < 40:
            counter_weight += 1
    
    if elderly_person != 0:
        percentage_elderly_person = int((elderly_person / len(database)) * 100)
        
    if counter_height != 0:
        average_height = total_height / counter_height

    if counter_weight != 0:
        percentage_weight = int((counter_weight / len(database)) * 100)

    
    # Saida de Dados
    print(f"{colors[main_color]}Todas as pessoas adicionadas:{colors['reset']}\n")

    for i, person in enumerate(database, start = 1):
        print(f"{colors[main_color]}>>{colors['reset']} Pessoa {i}: {person['name']}")
        print(f" - Idade: .. {person['age']} anos")
        print(f" - Altura: . {person['height']}m")
        print(f" - Peso: ... {person['weight']}kg")
        print()

    print(f"{colors[main_color]}Pessoas com 50 anos ou mais:{colors['reset']}\n")
    print(f"> Total de pessoas: {colors[main_color]}{elderly_person}{colors['reset']} de {colors[main_color]}{len(database)}{colors['reset']}")
    print(f"> Percentual: {percentage_elderly_person}% {colors[main_color]}{"O" * (percentage_elderly_person // 10)}{colors['black']}{"O" * (10 - (percentage_elderly_person // 10))}{colors['reset']}")

    print(f"\n{colors[main_color]}Média de Altura (10 a 20 anos):{colors['reset']}\n")
    print(f"> Total de pessoas: {colors[main_color]}{counter_height}{colors['reset']} de {colors[main_color]}{len(database)}{colors['reset']}")
    print(f"> Média de : {colors[main_color]}{average_height:.2f}m{colors['reset']}")

    print(f"\n{colors[main_color]}Pessoas com Menos de 40kg:{colors['reset']}\n")
    print(f"> Total de pessoas: {colors[main_color]}{counter_weight}{colors['reset']} de {colors[main_color]}{len(database)}{colors['reset']}")
    print(f"> Percentual: {percentage_weight}% {colors[main_color]}{"O" * (percentage_weight // 10)}{colors['black']}{"O" * (10 - (percentage_weight // 10))}{colors['reset']}")

    footer(spacing)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# INIT
program()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #