import customtkinter as ctk

# Create the Window
app = ctk.CTk()

# -resolution
app.title("Calculadora de Média - JM")
app.geometry("300x400")
app.minsize(300, 400)

# -grid
app.columnconfigure((0, 1, 2), weight=1)
app.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# -theme
ctk.set_appearance_mode("dark")

# Variables
spacing = 25
entry_width = 220

# Fucntions
def fix(entry):
    if "," in entry:
        entry = entry.replace(",", ".")
    return entry

def media():
    try:
        value_1, value_2, value_3 = float(fix(entry_1.get())), float(fix(entry_2.get())), float(fix(entry_3.get()))

        media_output = (value_1 + value_2 + value_3) / 3

        media_label.configure(text=str(f"Média das notas: {media_output:.2f}"), text_color="#FFFBDE")
    except ValueError:
        media_label.configure(text="Digite valores validos!", text_color="#A84A40")

    frame.configure(fg_color="#2B2B2B")
    media_label.configure(fg_color="#2B2B2B")


# Fields
label_1 = ctk.CTkLabel(app, text="Nota 1°:")
label_1.grid(column=0, row=0, pady=(0, spacing), padx=spacing, sticky="w")

entry_1 = ctk.CTkEntry(app, placeholder_text="Digite a primeira nota...", width=entry_width)
entry_1.grid(column=0, columnspan=3, row=0, pady=(spacing, 0), padx=spacing, sticky="we")

label_2 = ctk.CTkLabel(app, text="Nota 2°:")
label_2.grid(column=0, row=1, pady=(0, spacing), padx=spacing, sticky="w")

entry_2 = ctk.CTkEntry(app, placeholder_text="Digite a segunda nota...", width=entry_width)
entry_2.grid(column=0, columnspan=3, row=1, pady=(spacing, 0), padx=spacing, sticky="we")

label_3 = ctk.CTkLabel(app, text="Nota 3°:")
label_3.grid(column=0, row=2, pady=(0, spacing), padx=spacing, sticky="w")

entry_3 = ctk.CTkEntry(app, placeholder_text="Digite a terceira nota...", width=entry_width)
entry_3.grid(column=0, columnspan=3, row=2, pady=(spacing, 0), padx=spacing, sticky="we")

button = ctk.CTkButton(app, text="Calcular Média", command=media, fg_color="#58A84F", hover_color="#344442")
button.grid(column=0, columnspan=3, row=3, pady=spacing, padx=spacing, sticky="we")

frame = ctk.CTkFrame(app, width=entry_width, height=60, fg_color="#242424")
frame.grid(column=0, columnspan=3, row=4, padx=spacing, sticky="we")

media_label = ctk.CTkLabel(app, text="", fg_color="#242424")
media_label.grid(column=0, row=4, padx=(spacing * 1.5, 0), sticky="w")

# Start
app.mainloop()