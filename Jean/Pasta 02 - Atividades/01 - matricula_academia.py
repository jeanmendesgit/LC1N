# PROGRAMA DE REGISTRA MATRICULAS

#variables

database = []

#functions

def add():
    student_entry_registration = [{"label" : "o Nome do Aluno",               "value" : None},
                                  {"label" : "o Email do Aluno",              "value" : None},
                                  {"label" : "o Telefone do Aluno",           "value" : None},
                                  {"label" : "se possui Whatsapp",            "value" : None},
                                  {"label" : "o Endereço do Aluno",           "value" : None},
                                  {"label" : "a Data de Nascimento do Aluno", "value" : None},
                                  {"label" : "o Sexo do Aluno",               "value" : None},
                                  {"label" : "o Peso do Aluno",               "value" : None},
                                  {"label" : "a Altura do Aluno",             "value" : None}]
    
    for i in range(len(student_entry_registration)):
        student_entry_registration[i]["value"] = input(f"\nDigite {student_entry_registration[i]["label"]}: ")

    registration = {"student_name"      : student_entry_registration[0]["value"],
                    "student_email"     : student_entry_registration[1]["value"],
                    "student_number"    : student_entry_registration[2]["value"],
                    "student_whatsapp"  : student_entry_registration[3]["value"],
                    "student_address"   : student_entry_registration[4]["value"],
                    "student_birthday"  : student_entry_registration[5]["value"],
                    "student_gender"    : student_entry_registration[6]["value"],
                    "student_weight"    : student_entry_registration[7]["value"],
                    "student_height"    : student_entry_registration[8]["value"]}
    
    database.append(registration)

    print(" ")
    print("Cadrastro Finalizado!")

def view():
    print(" ")
    print("-" * 31)
    print("      Livro de Matriculas   ")
    print("-" * 31)

    if len(database) == 0:
        print("\nNão há matrículas no momento...")

    for i, registration in enumerate(database):
        print(" ")
        print(f"Matrícula: 2025AC{i + 1:04d}")
        print(f"-> Nome do aluno: ... {registration["student_name"]}")
        print(f"-> Email do aluno: .. {registration["student_email"]}")
        print(f"-> Telefone do aluno: {registration["student_number"]}")
        print(f"-> Whatsapp ativo: .. {registration["student_whatsapp"]}")
        print(f"-> Endereço do aluno: {registration["student_address"]}")
        print(f"-> Data de nascimeno: {registration["student_birthday"]}")
        print(f"-> Sexo do aluno: ... {registration["student_gender"]}")
        print(f"-> Peso do aluno: ... {registration["student_weight"]}")
        print(F"-> Altura do aluno: . {registration["student_height"]}")
    
    
#main

def main():
    while True:
        print("-" * 31)
        print("     Sistema de Matriculas     ")
        print("-" * 31)
        
        print(" 1) Adicionar matrícula.\n 2) Visualizar matrícula\n 3) Editar matrícula\n 4) Sair\n")
        
        users_choose = input("-> Digite o número da opção: ")
        
        options = ['1', '2', '3', '4']
        
        if users_choose not in options:
            print(" ")
            print("Erro: Opção inválida!")
        else:  
            match int(users_choose):
                case 1:
                    add()
                case 2:
                    view()
                case 4:
                    print(" ")
                    print("Até mais! Seção encerrada...")
                    print(" ")
                    break

        print(" ")  
        input("Pressione ENTER para retonar ao menu.")

#start

main()