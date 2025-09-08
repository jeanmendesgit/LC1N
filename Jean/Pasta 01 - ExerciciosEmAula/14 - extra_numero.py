import customtkinter as ctk

# Create the Window
app = ctk.CTk()

# -resolution
app.title("Type number - JM")
app.geometry(f"{400}x{200}")
app.minsize(400, 200)
app.maxsize(600, 400)

# -window's grid
app.columnconfigure((0, 1, 2), weight=1)
app.rowconfigure((0, 1, 2), weight=1)

# -theme
ctk.set_appearance_mode("dark")

# Functions
def main():
    try:
        value = int(value_entry.get())
        
        half, double, triple, successor, predecessor = (value / 2), (value * 2), (value * 3), (value + 1), (value - 1)
        
        output_half_label.configure(text=str(half), text_color=green_color)
        output_double_label.configure(text=str(double), text_color=green_color)
        output_triple_label.configure(text=str(triple), text_color=green_color)
        output_successor_label.configure(text=str(successor), text_color=green_color)
        output_predecessor_label.configure(text=str(predecessor), text_color=green_color)
    except ValueError:
        output_half_label.configure(text="Inválido!", text_color=red_color)
        output_double_label.configure(text="Inválido!", text_color=red_color)
        output_triple_label.configure(text="Inválido!", text_color=red_color)
        output_successor_label.configure(text="Inválido!", text_color=red_color)
        output_predecessor_label.configure(text="Inválido!", text_color=red_color)

# Variables
margin = 30

value_label_text = "Seu número:"
value_entry_placeholder_text = "Digite um número..."
entry_button_text = "Enter"

entry_button_width = 60
output_tview_height = 40

buttons_color = "#58A84F"
buttons_hover = "#588D93"
buttons_hover_2 = "#387E30"
red_color = "#A84A40"
green_color = "#90D288"
bg_color = "#34656C"
bg_color_2 = "#354543"

# Fields

value_label = ctk.CTkLabel(app, text=str(value_label_text))

value_entry = ctk.CTkEntry(app, placeholder_text=str(value_entry_placeholder_text))

entry_button = ctk.CTkButton(app,
                             command=main,
                             text=entry_button_text,
                             width=entry_button_width,
                             fg_color=buttons_color,
                             hover_color=buttons_hover_2)

output_tview = ctk.CTkTabview(app, command=main,
                             height=output_tview_height,
                             segmented_button_selected_color=buttons_color,
                             segmented_button_selected_hover_color=buttons_hover_2,
                             segmented_button_unselected_hover_color=buttons_hover,
                             segmented_button_unselected_color=bg_color,
                             segmented_button_fg_color=bg_color_2)
output_tview.add("Metade")
output_tview.add("Dobro")
output_tview.add("Triplo")
output_tview.add("Sucessor")
output_tview.add("Antecessor")

output_half_label = ctk.CTkLabel(output_tview.tab("Metade"), text="",font=("default", 32))
output_double_label = ctk.CTkLabel(output_tview.tab("Dobro"), text="",font=("default", 32))
output_triple_label = ctk.CTkLabel(output_tview.tab("Triplo"), text="",font=("default", 32))
output_successor_label = ctk.CTkLabel(output_tview.tab("Sucessor"), text="",font=("default", 32))
output_predecessor_label = ctk.CTkLabel(output_tview.tab("Antecessor"), text="",font=("default", 32))

    
# -grid
value_label.grid(column=0,
                 row=0,
                 sticky="w",
                 pady=(0, margin * 2),
                 padx=margin)

value_entry.grid(column=0, columnspan=3,
                 row=0,
                 sticky="ew",
                 padx=(margin, 0))

entry_button.grid(column=3,
                  row=0,
                  sticky="ew",
                  padx=(0, margin))

output_tview.grid(column=0, columnspan=4,
                  row=1,
                  sticky="new",
                  padx=margin)

output_half_label.pack()
output_double_label.pack()
output_triple_label.pack()
output_successor_label.pack()
output_predecessor_label.pack()

# Start
app.mainloop()

