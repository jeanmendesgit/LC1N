# Estruturas de Dados - LISTAS

from jmutils import *
header_color("Listas", 50, 'green')

# LISTA __________________________________________________________
numeros = [2, 5, 10]

print(f"1º Lista:   {numeros}")     # >> [2, 5, 10]
print(f"Elemento 2:  {numeros[1]}") # >> 5

# INSERIR ELEMENTOS ______________________________________________
numeros.append(8)

print(f"Nova lista: {numeros}")    # >> [2, 5, 10, 8]

# INSERIR ELEMENTOS EM UMA POSIÇÃO _______________________________
numeros.insert(3, 6)

print(f"Nova lista: {numeros}")    # >> [2, 5, 10, 6, 8]

footer(50)