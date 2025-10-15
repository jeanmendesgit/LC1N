# Programa que imprime imprimi todos os números de 1 até o número que o usuário digitou.

# Amazenamento de Dados
contador = -1

# Entrada de Dados
valor = int(input("Digite o tamanho da lista de números: "))

# Processamento e Saída de Dados
while contador < valor:
    contador += 1
    print(f"{contador}º")
