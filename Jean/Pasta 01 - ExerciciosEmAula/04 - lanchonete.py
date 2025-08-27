# Programa que gerencia uma lanchonete

print(" ")
print("Gerenciamento Lanchonete")
print(" ")

# Entradas

nome_do_produto = input("Nome do produto: ")
descr_do_produto = input("Descrição do produto: ")
quant_do_produto = int(input("Quatidade do produto: "))
custo_do_produto = float(input("Custo do produto: "))
preco_do_produto = float(input("Preço do produto: "))
categ_do_produto = input("Categoria do produto: ")

# Saída

print(" ")
print("Produto", nome_do_produto)
print("> Descrição:", descr_do_produto)
print("> Quantidade:", quant_do_produto)
print("> Custo: R$", custo_do_produto)
print("> Preço: R$", preco_do_produto)
print("> Categoria:", categ_do_produto)