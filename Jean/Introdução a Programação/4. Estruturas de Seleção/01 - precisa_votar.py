# Programa que informa se e necessario votar

from jmutils import *

# Variaveis
ano     = 2025
spacing = 40

# Cabecalho
header("Saiba mais Votação", spacing)

# Entrada de dados
idade_do_usuario = int(input("Digite o ano de nascimento: "))

# Processamento de Dados
idade = ano - idade_do_usuario

# Estrutura & Saída de Dados
if idade < 16:
    highlight("Não pode votar!", spacing)

if idade >= 16 and idade < 18:
    highlight("Votação Facultativa!", spacing)

if idade >= 18 and idade < 70:
    highlight("Votação Obrigatoria!", spacing)

if idade >= 70:
    highlight("Votação Facultativa!", spacing)

footer(spacing)