# Programa media 3 notas

# Entrada
nota_1 = float(input("Digite a 1ª nota: "))
nota_2 = float(input("Digite a 2ª nota: "))
nota_3 = float(input("Digite a 3ª nota: "))

# Processamento
media = (nota_1 + nota_2 + nota_3) / 3

# Saída de Dados paa Usuário
print(" ")

if media >= 7:
    print("Média:", media, "Aprovado!")
else:
    print("Média:", media, "Reprovado!")