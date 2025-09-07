import customtkinter as ctk

# Create thw Window

app = ctk.CTk()

app.title("Calcule Média - JM")
app.geometry("300x300")

# Fields

label_1 = ctk.CTkLabel(app, )

entry_1 = ctk.CTkEntry(app, placeholder_text="Digite a primeira nota...")
entry_1.grid()

# Start

app.mainloop()