import customtkinter as ctk

# Create the window
app = ctk.CTk()
app.title('Coversor de Minutos')

# L resolution ..................
width, height = 300, 250
app.geometry(f"{width}x{height}")
app.minsize(width, height)

# L grid ...............
app.columnconfigure((0, 1 , 2), weight=1)
app.rowconfigure((0, 1 , 2, 3, 4), weight=0)


# L theme .....................
ctk.set_appearance_mode("dark")

# Variables
# L size .................
margin = 15
spacing = 10

h_frame = 80

# L text .............................
txt_label_one = "Minutos:"
txt_button_one   = "Converter"

pht_entry_one = "Digite a quantidade de minutos... "

# L colors ...................
default_light    = "#2B2B2B"
default_dark     = "#242424"
buttons_color    = "#58A84F"
buttons_hover    = "#387E30"
buttons2_color   = "#34656C"
buttons2_hover   = "#588D93"
text_wrong_color = "#A84A40"
text_right_color = "#90D288"
tview_fg_color   = "#354543"

def data_processing():
    try:
        value = int(entry_one.get())
        
        hours   = value // 60
        minutes = value % 60
        
        if hours < 10 and minutes >= 10:
            label_out.configure(text=str(f"0{hours}h:{minutes}m"))
        elif hours >= 10 and minutes < 10:
            label_out.configure(text=str(f"{hours}h:0{minutes}m"))
        elif hours < 10 and minutes < 10:
            label_out.configure(text=str(f"0{hours}h:0{minutes}m"))
        else:
            label_out.configure(text=str(f"{hours}h:{minutes}m"))
        
    except ValueError:
        label_out.configure(text="Inválido!")

# Fields

label_one = ctk.CTkLabel(app,
                         text=txt_label_one)

entry_one = ctk.CTkEntry(app,
                         placeholder_text=pht_entry_one)

button_one = ctk.CTkButton(app, command=data_processing,
                           text=txt_button_one)

frame_one = ctk.CTkFrame(app,
                         height=h_frame)

label_out = ctk.CTkLabel(app,
                        text="00h:00m",
                        font=("", 40),
                        fg_color=default_light,
                        bg_color=default_light)

# L grid ......................................
label_one.grid(column=0,
               row=0,
               padx=margin, pady=(spacing, 0),
               sticky="wn")

entry_one.grid(column=0, columnspan=3,
               row=1,
               padx=margin, pady=(0, spacing * 2),
               sticky="new")

button_one.grid(column=0, columnspan=3,
                row=2,
                padx=margin, pady=(0, spacing),
                sticky="new")

frame_one.grid(column=0, columnspan=3,
               row=3,
               padx=margin, pady=(spacing, 0),
               sticky="new")

label_out.grid(column=0, columnspan=3,
               row=3,
               padx=margin,
               sticky="ew")


# Start
app.mainloop()