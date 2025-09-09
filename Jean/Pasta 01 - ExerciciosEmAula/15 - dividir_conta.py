import customtkinter as ctk

# Create the Window
app = ctk.CTk()
app.title("Se Não Matar Engondar")

# L resolution ..................
width, height = 300, 315
app.geometry(f"{width}x{height}")
app.minsize(width, height)

# L grid ..................................
app.columnconfigure((0, 1, 2), weight=1)
app.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=0)

# L theme .....................
ctk.set_appearance_mode("dark")

# Variables

# L size .........
margin = 10
margin_frame = 10
spacing = 10
w_optionmenu = 40
w_entry_two = 60
h_frame_all = 30
cr_frame_all = 30

# L text ......................................................................
txt_label_one   = "Valor da conta(R$):"
txt_label_two   = "Qdt:"
txt_label_three_v1, txt_label_three_v2 = "Valor da conta:", "Valor por Pessoa:"
txt_label_four  = "Gorjeta para o garçom:"
txt_label_five  = "Total:"
pht_entry_one   = "Digite o valor da conta..."
txt_switch_one  = "Dividir a conta"
pht_entry_two   = "1..."
txt_button_one  = "Calcular"

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


# Functions
def state_entry_two():
    match switch_one.get():
        case 'disable':
            label_two.grid_forget()
            entry_two.grid_forget()
        case 'enable':
            label_two.grid(column=2,
                row=2,
                padx=(0, (margin * 3) + w_entry_two), pady=(0, spacing),
                sticky="ens")
        
            entry_two.grid(column=2,
                row=2,
                padx=(0, margin + margin_frame), pady=(0, spacing),
                sticky="ens")
            
def fix(entry):
    if "," in entry:
        entry = entry.replace(",", ".")
    return entry
            
def data_processing():
    match switch_one.get():
        case 'disable':
            try:
                value = float(fix(entry_one.get()))
                percentage = int(optionmenu.get().replace("%", ""))
                tip   = (value / 100) * percentage
                total = value + tip
                
                label_three.configure(text=str(f"{txt_label_three_v1} R${value:.2f}"), text_color=text_right_color, bg_color=default_dark)
                label_four.configure(text=str(f"{txt_label_four} R${tip:.2f}"), text_color=text_right_color, bg_color=default_dark)
                label_five.configure(text=str(f"{txt_label_five} R${total:.2f}"), text_color=text_right_color, bg_color=default_dark)
                
                frame_one.configure(fg_color=default_dark)
                frame_two.configure(fg_color=default_dark)
                frame_three.configure(fg_color=default_dark)
            except ValueError:
                pass
        case 'enable':
            try:
                value   = float(fix(entry_one.get()))
                percentage = int(optionmenu.get().replace("%", ""))
                amount  = int(entry_two.get())
                tip     = (value / 100) * percentage
                total   = value + tip
                divalue = total / amount
                
                label_three.configure(text=str(f"{txt_label_three_v2} R${divalue:.2f}"), text_color=text_right_color, bg_color=default_dark)
                label_four.configure(text=str(f"{txt_label_four} R${tip:.2f}"), text_color=text_right_color, bg_color=default_dark)
                label_five.configure(text=str(f"{txt_label_five} R${total:.2f}"), text_color=text_right_color, bg_color=default_dark)
                
                frame_one.configure(fg_color=default_dark)
                frame_two.configure(fg_color=default_dark)
                frame_three.configure(fg_color=default_dark)
            except (ValueError, ZeroDivisionError):
                pass
            

# Fields
frame_bg = ctk.CTkFrame(app)

label_one = ctk.CTkLabel(app,
                         text=txt_label_one,
                         fg_color=default_light)

entry_one = ctk.CTkEntry(app,
                         placeholder_text=pht_entry_one,
                         corner_radius=margin * 2,
                         bg_color=default_light)

optionmenu = ctk.CTkOptionMenu(app,
                               values=["08%", "10%", "13%", "15%"],
                               width=w_optionmenu,
                               bg_color=default_light)

optionmenu.set("Taxa")

switch_one = ctk.CTkSwitch(app,
                           command=state_entry_two,
                           onvalue="enable", offvalue="disable",
                           text=txt_switch_one,
                           bg_color=default_light)

label_two = ctk.CTkLabel(app,
                         text=txt_label_two,
                         bg_color=default_light)

entry_two = ctk.CTkEntry(app,
                         width=w_entry_two,
                         placeholder_text=pht_entry_two,
                         corner_radius=margin * 2,
                         bg_color=default_light,)

button_one = ctk.CTkButton(app, command=data_processing,
                           text=txt_button_one,
                           corner_radius=20,
                           bg_color=default_light)

frame_one = ctk.CTkFrame(app,
                         height=h_frame_all,
                         corner_radius=cr_frame_all,
                         fg_color=default_light,
                         bg_color=default_light,)

frame_two = ctk.CTkFrame(app,
                         height=h_frame_all,
                         corner_radius=cr_frame_all,
                         fg_color=default_light,
                         bg_color=default_light,)

frame_three = ctk.CTkFrame(app,
                         height=h_frame_all,
                         corner_radius=cr_frame_all,
                         fg_color=default_light,
                         bg_color=default_light,)

label_three = ctk.CTkLabel(frame_one,
                           text="", text_color=default_light,
                           fg_color=None,
                           corner_radius=margin,
                           bg_color=default_light)

label_four = ctk.CTkLabel(frame_two,
                           text="", text_color=default_light, 
                           fg_color=None,
                           corner_radius=margin,
                           bg_color=default_light)

label_five = ctk.CTkLabel(frame_three,
                           text="", text_color=default_light,
                           fg_color=None,
                           corner_radius=margin,
                           bg_color=default_light)

# L grid ...................................................................................................
frame_bg.grid(column=0, columnspan=3,
              row=0, rowspan=8,
              padx=margin_frame, pady=(margin_frame, 0),
              sticky="news")

label_one.grid(column=0,
               row=0, rowspan=1,
               padx=margin + margin_frame, pady=(margin * 2, 0),
               sticky="ws")

entry_one.grid(column=0, columnspan=3,
               row=1,
               padx=(margin + margin_frame, (margin * 5) + margin_frame + w_optionmenu), pady=(0, spacing),
               sticky="wen")

optionmenu.grid(column=2,
                row=1,
                padx=(spacing, margin + margin_frame), pady=(0, spacing),
                sticky="en")

switch_one.grid(column=0,
                row=2,
                padx=margin + margin_frame, pady=(3, spacing + 3),
                sticky="wns")

button_one.grid(column=0, columnspan=3,
                row=3,
                padx=margin + margin_frame, pady=(0, spacing),
                sticky="wen")

frame_one.grid(column=0, columnspan=3,
                row=4,
                padx=margin + margin_frame, pady=spacing,
                sticky="we")

frame_two.grid(column=0, columnspan=3,
                row=5,
                padx=margin + margin_frame, pady=(0, spacing),
                sticky="we")

frame_three.grid(column=0, columnspan=3,
                row=6,
                padx=margin + margin_frame, pady=(0, spacing * 2),
                sticky="we")

label_three.grid(column=0,
                row=0,
                padx=margin,
                sticky="we")

label_four.grid(column=0,
                row=0,
                padx=margin,
                sticky="we")

label_five.grid(column=0,
                row=0,
                padx=margin,
                sticky="we")

# Start
app.mainloop()