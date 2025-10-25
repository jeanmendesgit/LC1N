# Programa com ferramentas simples de apoio as aulas de matematica

from jmutils import *

# Variaveis
PI = 3.14159265359

title   = "Calcular áreas de Figuras Geométricas"
spacing = 60

formulas = {1 : "A = L²",
            2 : "A = b • h",
            3 : "A = b • h / 2",
            4 : "A = π • r²"}

def main():
    while True:   
        header(title, spacing)
        
        print("Qual figura será calculada:")
        print("1) Quadrado\n2) Retângulo\n3) Triângulo\n4) Círculo\n5) Sair\n")
        
        try:
            user_choice = int(input("Digite o número da opção: "))
            
            match user_choice:
                # Quadrado
                case 1:
                    side = float(input("\nDigite a medida do lado do quadrado: "))
                    
                    area = side * side
                    
                    output = f"A = {side}² = {area}"
                # Retângulo
                case 2:
                    base   = float(input("\nDigite a medida da Base: "))
                    height = float(input("\nDigite a medida da Altura: "))
                        
                    area = base * height
                    
                    output = f"A = {base} • {height} = {area}"
                # Triângulo
                case 3:
                    base   = float(input("\nDigite a medida da Base: "))
                    height = float(input("\nDigite a medida da Altura: "))
                        
                    area = base * height / 2
                    
                    output = f"A = {base} • {height} / 2 = {area:.2f}"
                # Círculo
                case 4:
                    radius = float(input("\nDigite a medida da Raio: "))
                        
                    area = PI * (radius * radius)
                    
                    output = f"A = π • {radius}² = {area:.2f}"
                case 5:
                    highlight("Até mais!", spacing)
                    break
                case _:
                    print("\nOpção não encontrada!\n")
                    
            highlight(f"Fórmula: {formulas[user_choice]}", spacing)
            highlight(f"Calculo: {output}", spacing)
            footer(spacing)
        except ValueError:
            print("\nErro: Valor inválido!\n")
            
            input("Pressione ENTER para retonar ao menu\n")
            
            main()
            
        input("\nPressione ENTER para retonar ao menu\n")
        
main()


    
            