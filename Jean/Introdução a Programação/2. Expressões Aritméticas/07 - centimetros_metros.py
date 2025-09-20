import customtkinter as ctk

# Create the Window
app = ctk.CTk()

# -resolution
width = 300
height = 260
app.title('Conversor - JM')
app.geometry(f'{width}x{height}')
app.minsize(width=width, height=height)
app.maxsize(width=width, height=height)

# -grid
app.grid_columnconfigure((0, 1, 2), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

# -theme
ctk.set_appearance_mode("dark")

# Functions
def optionmenu_callback(choice):
    match choice:
        case "Centímetros":
            main_label.configure(text="Centímetros (cm):")
            main_label.grid(column=0, columnspan=1, row=1, padx=(21, 0))
        case "Metros":
            main_label.configure(text="Metros (m):")
            main_label.grid(column=0, columnspan=1, row=1, padx=(15, 0))

def output():    
    output_frame.configure(fg_color="#2B2B2B")
    output_label.configure(fg_color="#2B2B2B")
    
    value = main_entry.get()
    
    if not value.isdigit():
         output_label_text = "Digite um valor válido!"
         output_label.configure(text_color="#A84A40")
    else:
        value = int(value)
        output_label.configure(text_color="#FFFBDE")
        match menu_options.get():
            case "Centímetros":
                output_label_text = f"Metros (m): {value / 100}m."
            case "Metros":
                output_label_text = f"Centímetros (cm): {value * 100}cm."
                  
    output_label.configure(text=str(output_label_text))
    value = 0
        
# Filds
menu_options = ctk.CTkOptionMenu(app, values=["Centímetros", "Metros"], command=optionmenu_callback, width=200, fg_color="#58A84F", button_color="#34656C")
menu_options.grid(column=0, row=0, columnspan=3, pady=(21, 0))

main_label = ctk.CTkLabel(app, text="Centímetros (cm):")
main_label.grid(column=0, row=1, padx=(21, 0))

main_entry = ctk.CTkEntry(app, placeholder_text="0", width=200)
main_entry.grid(column=0, row=1, columnspan=3, pady=(50, 0))

main_button = ctk.CTkButton(app, text="Calcular", command=output, width=200, fg_color="#58A84F", hover_color="#344442")
main_button.grid(column=0, row=2, columnspan=3)

output_frame = ctk.CTkFrame(app, height=40, width=200, fg_color="#242424")
output_frame.grid(column=0, row=3, columnspan=3)

output_label = ctk.CTkLabel(app, text="", anchor="w", bg_color="#242424")
output_label.grid(column=0, row=3, columnspan=3)


# Start
app.mainloop()