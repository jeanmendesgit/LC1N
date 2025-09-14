import customtkinter as ctk

# Create the window
app = ctk.CTk()
app.title('Quantidade de notas')

# L resolution ..................
width, height = 300, 560
app.geometry(f"{width}x{height}")
app.minsize(width, height)
app.maxsize(width, height)

# L grid ...............
app.columnconfigure((0, 1 , 2), weight=1)
app.rowconfigure((0, 1 , 2, 3, 4, 5, 6), weight=0)

# L theme .....................
ctk.set_appearance_mode("dark")

# Variables
# L size .................
margin = 15
spacing = 10

w_frame = 127.5
h_frame = 80

# L text .............................
txt_label_one  = "Valor em dinheiro:"
txt_button_one = "Verificar"
pht_entry_one  = "Digite a quantidade em dinheiro... "
txt_label_erro = "Atençāo! Valor inválido!"

txt_frame_title_one   = "200 Reais"
txt_frame_title_two   = "100 Reais"
txt_frame_title_three = "50 Reais"
txt_frame_title_four  = "20 Reais"
txt_frame_title_five  = "10 Reais"
txt_frame_title_six   = "5 Reais"
txt_frame_title_seven = "2 Reais"
txt_frame_title_eight = "1 Real"

# L colors .....................
default_light      = "#2B2B2B"
default_dark       = "#242424"
buttons_color      = "#58A84F"
buttons_hover      = "#387E30"
buttons2_color     = "#34656C"
buttons2_hover     = "#588D93"
text_wrong_color   = "#A84A40"
text_right_color   = "#90D288"
tview_fg_color     = "#354543"
text_disable_color = "gray"

# Functions
def fix(value):
    if ',' in value:
        value = value.replace(',', '.')
    return value

def data_processing():
    try:
        value = float(fix(entry_one.get()))
        
        notes_200 = value // 200
        value    -= notes_200 * 200
        notes_100 = value // 100
        value    -= notes_100 * 100
        notes_50  = value // 50
        value    -= notes_50 * 50
        notes_20  = value // 20
        value    -= notes_20 * 20
        notes_10  = value // 10
        value    -= notes_10 * 10
        notes_5   = value // 5
        value    -= notes_5 * 5
        notes_2   = value // 2
        value    -= notes_2 * 2
        notes_1   = value // 1
        value    -= notes_1 * 1

        frame_value_one.configure(text=str(int(notes_200)), text_color=text_right_color)  if notes_200 != 0 else frame_value_one.configure(text="0", text_color=text_disable_color)
        frame_value_two.configure(text=str(int(notes_100)), text_color=text_right_color)  if notes_100 != 0 else frame_value_two.configure(text="0", text_color=text_disable_color)
        frame_value_three.configure(text=str(int(notes_50)), text_color=text_right_color) if notes_50 != 0 else frame_value_three.configure(text="0", text_color=text_disable_color)
        frame_value_four.configure(text=str(int(notes_20)), text_color=text_right_color)  if notes_20 != 0 else frame_value_four.configure(text="0", text_color=text_disable_color)
        frame_value_five.configure(text=str(int(notes_10)), text_color=text_right_color)  if notes_10 != 0 else frame_value_five.configure(text="0", text_color=text_disable_color)
        frame_value_six.configure(text=str(int(notes_5)), text_color=text_right_color)    if notes_5 != 0 else frame_value_six.configure(text="0", text_color=text_disable_color)
        frame_value_seven.configure(text=str(int(notes_2)), text_color=text_right_color)  if notes_2 != 0 else frame_value_seven.configure(text="0", text_color=text_disable_color)
        frame_value_eight.configure(text=str(int(notes_1)), text_color=text_right_color)  if notes_1 != 0 else frame_value_eight.configure(text="0", text_color=text_disable_color)

        label_erro.grid_forget()
    except ValueError:
        label_erro.grid(column=0, columnspan=3,
               row=3,
               padx=margin,
               sticky="new")
        
        frame_value_one.configure(text="0", text_color=text_disable_color)
        frame_value_two.configure(text="0", text_color=text_disable_color)
        frame_value_three.configure(text="0", text_color=text_disable_color)
        frame_value_four.configure(text="0", text_color=text_disable_color)
        frame_value_five.configure(text="0", text_color=text_disable_color)
        frame_value_six.configure(text="0", text_color=text_disable_color)
        frame_value_seven.configure(text="0", text_color=text_disable_color)
        frame_value_eight.configure(text="0", text_color=text_disable_color)

# Fields

label_one = ctk.CTkLabel(app,
                         text=txt_label_one)

entry_one = ctk.CTkEntry(app,
                         placeholder_text=pht_entry_one)

button_one = ctk.CTkButton(app, command=data_processing,
                           text=txt_button_one,
                           fg_color=buttons_color,
                           hover_color=buttons_hover,
                           corner_radius=20)

label_erro = ctk.CTkLabel(app,
                          text=txt_label_erro,
                          text_color=text_wrong_color)

# L frame ......................................

frame_one = ctk.CTkFrame(app,
                         height=h_frame)

frame_two = ctk.CTkFrame(app,
                         height=h_frame)

frame_three = ctk.CTkFrame(app,
                         height=h_frame)

frame_four = ctk.CTkFrame(app,
                         height=h_frame)

frame_five = ctk.CTkFrame(app,
                         height=h_frame)

frame_six = ctk.CTkFrame(app,
                         height=h_frame)

frame_seven = ctk.CTkFrame(app,
                          height=h_frame)

frame_eight = ctk.CTkFrame(app,
                          height=h_frame)


# L icon .............................................................................

frame_icon_one   = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_two   = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_three = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_four  = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_five  = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_six   = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_seven = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)
frame_icon_eight = ctk.CTkLabel(app, text='💵', font=("",30), bg_color=default_light)

# L title ..................................................

frame_title_one = ctk.CTkLabel(app,
                               text=txt_frame_title_one,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_two = ctk.CTkLabel(app,
                               text=txt_frame_title_two,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_three = ctk.CTkLabel(app,
                               text=txt_frame_title_three,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_four = ctk.CTkLabel(app,
                               text=txt_frame_title_four,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_five = ctk.CTkLabel(app,
                               text=txt_frame_title_five,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_six = ctk.CTkLabel(app,
                               text=txt_frame_title_six,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_seven = ctk.CTkLabel(app,
                               text=txt_frame_title_seven,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

frame_title_eight = ctk.CTkLabel(app,
                               text=txt_frame_title_eight,
                               font=("", 14),
                               fg_color=default_light,
                               bg_color=default_light)

# L value ....................................................

frame_value_one = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_two = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_three = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_four = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_five = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_six = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_seven = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
                               font=("", 40),
                               fg_color=default_light,
                               bg_color=default_light)

frame_value_eight = ctk.CTkLabel(app,
                               text="0", text_color=text_disable_color,
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

# L frame..............................................

frame_one.grid(column=0,
               row=4,
               padx=(margin, margin // 2), pady=spacing,
               sticky="new")

frame_two.grid(column=2,
               row=4,
               padx=(margin // 2, margin), pady=spacing,
               sticky="new")

frame_three.grid(column=0,
               row=5,
               padx=(margin, margin // 2), pady=spacing,
               sticky="new")

frame_four.grid(column=2,
               row=5,
               padx=(margin // 2, margin), pady=spacing,
               sticky="new")

frame_five.grid(column=0,
               row=6,
               padx=(margin, margin // 2), pady=spacing,
               sticky="new")

frame_six.grid(column=2,
               row=6,
               padx=(margin // 2, margin), pady=spacing,
               sticky="new")

frame_seven.grid(column=0,
               row=7,
               padx=(margin, margin // 2), pady=spacing,
               sticky="new")

frame_eight.grid(column=2,
               row=7,
               padx=(margin // 2, margin), pady=spacing,
               sticky="new")



# l icon ..........................................................
frame_icon_one.grid(column=0,
                    row=4,
                    padx=margin, pady=(0, spacing * 2),
                    sticky="es")

frame_icon_two.grid(column=2,
                    row=4,
                    padx=(0, margin * 2), pady=(0, spacing * 2),
                    sticky="es")

frame_icon_three.grid(column=0,
                    row=5,
                    padx=margin, pady=(0, spacing * 2),
                    sticky="es")

frame_icon_four.grid(column=2,
                    row=5,
                    padx=(0, margin * 2), pady=(0, spacing * 2),
                    sticky="es")

frame_icon_five.grid(column=0,
                    row=6,
                    padx=margin, pady=(0, spacing * 2),
                    sticky="es")

frame_icon_six.grid(column=2,
                    row=6,
                    padx=(0, margin * 2), pady=(0, spacing * 2),
                    sticky="es")

frame_icon_seven.grid(column=0,
                    row=7,
                    padx=margin, pady=(0, spacing * 2),
                    sticky="es")

frame_icon_eight.grid(column=2,
                    row=7,
                    padx=(0, margin * 2), pady=(0, spacing * 2),
                    sticky="es")

# L title ....................................................

frame_title_one.grid(column=0,
                     row=4,
                     padx=(margin*1.5, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_two.grid(column=2,
                     row=4,
                     padx=(margin, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_three.grid(column=0,
                     row=5,
                     padx=(margin*1.5, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_four.grid(column=2,
                     row=5,
                     padx=(margin, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_five.grid(column=0,
                     row=6,
                     padx=(margin*1.5, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_six.grid(column=2,
                     row=6,
                     padx=(margin, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_seven.grid(column=0,
                     row=7,
                     padx=(margin*1.5, 0), pady=(spacing, 0),
                     sticky="nw")

frame_title_eight.grid(column=2,
                     row=7,
                     padx=(margin, 0), pady=(spacing, 0),
                     sticky="nw")

# L value ...........................................................

frame_value_one.grid(column=0,
                     row=4,
                     padx=(margin*1.5, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_two.grid(column=2,
                     row=4,
                     padx=(margin, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_three.grid(column=0,
                     row=5,
                     padx=(margin*1.5, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_four.grid(column=2,
                     row=5,
                     padx=(margin, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_five.grid(column=0,
                     row=6,
                     padx=(margin*1.5, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_six.grid(column=2,
                     row=6,
                     padx=(margin, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_seven.grid(column=0,
                     row=7,
                     padx=(margin*1.5, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

frame_value_eight.grid(column=2,
                     row=7,
                     padx=(margin, 0), pady=(0, spacing * 1.25),
                     sticky="sw")

# Start
app.mainloop()