# Programa | Operadores Relacionais

# Entrada de Dados
numero_1 = int(input("Digite o 1° número: "))
numero_2 = int(input("Digite o 2° número: "))

# Processamento
igual = numero_1 == numero_2
maior = numero_1  > numero_2
menor = numero_1  < numero_2
maior_igual    = numero_1 >= numero_2
menor_igual    = numero_1 <= numero_2
diferente      = numero_1 != numero_2
numero_1_par   = numero_1 % 2 == 0
numero_2_impar = numero_2 % 2 != 0

# Saida de Dados
print(" ")
print("O 1° número é igual ao 2° número?", igual)
print("O 1° número é maior que 2° número?", maior)
print("O 1° número é menor que 2° número?", menor)
print("O 1° número é maior ou igual ao 2° número?", maior_igual)
print("O 1° número é menor ou igual ao 2° número?", menor_igual)
print("O 1° número é diferente do 2° número?", diferente)
print("O 1° número é par?", numero_1_par)
print("O 2° número é par?", numero_2_impar)

