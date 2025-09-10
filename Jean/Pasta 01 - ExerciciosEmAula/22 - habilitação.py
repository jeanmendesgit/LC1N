# Programa que informa se é apto a ter habilitação

import functions as fn

# Variaveis
ano = 2025
spacing = 40

# Cabecalho
fn.header("Apto a Habilitação", spacing)

# Entradas de Dados
idade_do_usuario = int(input("Digite o ano de nascimento: "))

# Processamento

idade = ano - idade_do_usuario

# Saida de Dados

if idade >= 18:
    fn.highlight("Está apto a habilitação", spacing)
else:
    fn.highlight("Não está apto a habilitação!", spacing)

fn.footer(spacing)



