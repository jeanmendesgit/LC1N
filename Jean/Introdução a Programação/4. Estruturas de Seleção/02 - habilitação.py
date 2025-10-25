# Programa que informa se é apto a ter habilitação

from jmutils import *

# Variaveis
ano = 2025
spacing = 40

# Cabecalho
header("Apto a Habilitação", spacing)

# Entradas de Dados
idade_do_usuario = int(input("Digite o ano de nascimento: "))

# Processamento
idade = ano - idade_do_usuario

# Saida de Dados
if idade >= 18:
    highlight("Está apto a habilitação", spacing)
else:
    highlight("Não está apto a habilitação!", spacing)

footer(spacing)



