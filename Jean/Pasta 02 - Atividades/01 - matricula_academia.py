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
        student_entry_registration[i]["value"] = input(f"Digite {student_entry_registration[i]["label"]}: ")

    mapping = {"student_name" : "Nome do Aluno",
               "student_email" : "Email do Aluno",
               "student_number" : "Telefone do Aluno",
               "stundet_whastapp" : "Possui Whatsapp",
               "student_address" : "Endereço do Aluno",
               "student_birthday" : "Data de Nascimento do Aluno",
               "student_gender" : "Sexo do Aluno",
               "student_weight" : "Peso do Aluno",
               "student_height" : "Altura do Aluno"}
    
    registration = {}
    
    for key, label in mapping.items():
        value = next(entry["value"] for entry in student_entry_registration if entry["label"] == label)
        registration[key] = value
        

    database.append(registration)

    print("\nCadastro finalizado:")
    for k, v in registration.items():
        print(f"{k}: {v}")
        
    
#main

def main():
    while True:
        print("-------------------------------")
        print("     Sistema de Matriculas     ")
        print("-------------------------------")
        
        print(" 1) Adicionar matrícula.\n 2) Visualizar matrícula\n 3) Editar matrícula\n 4) Sair\n")
        
        users_choose = input("-> Digite o número da opção: ")
        
        options = ['1', '2', '3', '4']
        
        if users_choose not in options:
            print(" ")
            print("Erro: Opção inválida!")
            print(" ")
            
        match int(users_choose):
            case 1:
                add()
            case 4:
                print(" ")
                print("Até mais! Seção encerrada...")
                print(" ")
                break
            
        input("Pressione ENTER para retonar ao menu.")

#start

main()