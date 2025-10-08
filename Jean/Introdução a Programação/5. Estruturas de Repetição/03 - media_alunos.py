# Programa que calcula a media de 10 alunos

database = {}

# Entradas de Dados
for i in range(10):
    name = input(f"O nome do {i + 1}° aluno: ")
    n1 = float(input(f"Digite a 1° nota: "))
    n2 = float(input(f"Digite a 2° nota: "))

    media = (n1 + n2) / 2
    
    status = "Aprovado!" if media >= 7 else "Reprovado"

    database[i] = {"name" : name,  "media" : media, "status" : status}

# Saida de Dados
for i in range(len(database)):
    print(f"Aluno: {database[i]["name"]} Media: {database[i]["media"]} Situação: {database[i]["status"]}")