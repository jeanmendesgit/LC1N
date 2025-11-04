# Programa que soma de todos os fatoriais de todos os números entre 1 e 15

from jmutils import *

# Variaveis
init, end = 1, 15

title, spacing = f"Soma dos Fatoriais entre {init} e {end}", 60
main_color = 'green'

list_factorial, sum_factorial = [], 0

# PROCESSAMENTO DE DADOS
    # Calculados os fatoriais
for i in range(init, end + 1):
    factorial = i

    for o in range(i - 1, 1, -1):
        factorial *= o
    
    list_factorial.append(factorial)

    # Somando os fatoriais
for i in range(len(list_factorial)):
    sum_factorial += list_factorial[i]

# SAÍDA DE DADOS
header_color(title, spacing, main_color)

    # Exibindo Fatoriais
for i, item in enumerate(list_factorial, start = 1):
    if i < 10:
        print(f"> {colors[main_color]}{i}!{colors['reset']}  =  {item:,}".replace(",", "."))
    else:
        print(f"> {colors[main_color]}{i}!{colors['reset']} =  {item:,}".replace(",", "."))

    # Exibindo a Soma
highlight_color(f"Soma: {sum_factorial:,}".replace(",", "."), spacing, main_color)

input(f"Aperte {colors[main_color]}ENTER{colors['reset']} para ver o Astrobaldo.")

happy = f"""{colors['magenta']}

          _.-'''-._        
         /  _   _  \       
        /  (0) (0)  \      
       /_,         ,_\     
       | \         / |     
_      \  \._____./  /  __
\`\     \   \___/   / _|  |
 \ `\   /\         /\ \   /
  |  `\/ /`'-----'`\ \/  / 
  |_|\/ /           \   /  
  /    /|           |\_/        {colors[main_color]}ASTROBALDO ESTÁ FELIZ!{colors['magenta']}
  \___/ |           | \        {colors[main_color]}sua dúvida foi resolvida.{colors['magenta']}
   \ .  |           |  \   
    \|  |           |  |   
     |  `.         .'  |   
     \    `-.___.-'    /   
     `\       |       /'   
       `\     |     /'     
    .-.-.`\   |   /'.-.-.  
   (,(,(,`^   |   ^`,),),) 
    '-'-'-----`-----'-'-'{colors['reset']}
"""

print(happy)

footer(spacing)






