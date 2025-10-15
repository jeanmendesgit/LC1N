# Programa que mostra a tabuada de multiplicação de um número, de 1 a 10.

# Amazenamento de Dados
contador = 1

# Entrada de Dados
numero = int(input("Digite um número: "))

# Processamento e Saída de Dados
while contador < 11:
    print(f"{numero} x {contador} = {numero * contador}")

    contador += 1