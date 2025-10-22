# programa que ofereçe um menu onde o usuário pode escolher calcular a média de um aluno ou sair

import functions as fn

# Variaveis
title, spacing = "Médias de Alunos", 50

# Functions
def calcular_media():
    fn.line(spacing)

    # Entrada de Dados
    nome = input("Digite o nome do aluno: ")

    fn.line(spacing)

    nota1 = float(input("Digite o a 1º nota: "))
    nota2 = float(input("Digite o a 2º nota: "))

    # Processamento de Dados
    media = (nota1 + nota2) / 2
    situacao = "Aprovado!" if media >= 6 else "Reprovado"
    
    # Saída de Dados
    fn.line(spacing)
    print(f"Aluno: {nome}\n> Média: .. {media:.2f}\n> Situação: {situacao}")
    fn.line(spacing)

# Main
while True:
    # Cabeçalho
    fn.header(title, spacing)

    print("Escolha uma opção do menu:\n\n1) Calcular Média\n2) Sair")

    opcao = int(input("\nDigite o número da opção: "))

    match opcao:
        case 1:
            calcular_media()
        case 2:
            fn.highlight("Programa encerrado...", spacing)
            break
        case _:
            fn.highlight("Digite uma opção válida!", spacing)

    input("\nAperte ENTER para voltar ao menu.")