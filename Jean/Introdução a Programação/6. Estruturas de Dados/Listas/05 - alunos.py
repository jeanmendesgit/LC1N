# Programa que contém uma lista que recebe o nome de 10 alunos e outra lista para suas respectivas notas.
# Após a inserção dos dados, imprima tudo que foi inserido no sistema.

from jmutils import *

# VARIAVEIS ___________________________________________________________________________________
title, spacing, color = "Notas Estudantes", 60, 'green'

amount        = 2
students_list = []
grade_list    = []

# CABEÇALHO ___________________________________________________________________________________
header_color(title, spacing, color)

# PROCESSAMENTO DE DADOS ______________________________________________________________________
for i in range(amount):
    student = input(f"Digite o NOME do {i + 1}° aluno: ")
    grade   = float(input(f"Digite a NOTA do {i + 1}° aluno: "))

    line(spacing)

    students_list.append(student), grade_list.append(grade)

# SAÍDA DE DADOS ______________________________________________________________________________
header_color(title, spacing, color)

for i, students in enumerate(students_list):
    print(f">> Aluno {i + 1}: {students}\n - Nota: {grade_list[i]}")

    if i != amount - 1:
        print()

footer(spacing)
    

