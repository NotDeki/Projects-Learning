'''
Kreirati aplikaciju koja sadrzi dva dugmeta.
Jedno dugme klikom omogucava dodavanje jednog boda na ekran,dok drugo dugme oduzima bod sa ekrana.
'''

import tkinter as tki

pocetni_broj = 0


def dodavanje():
    global pocetni_broj
    pocetni_broj += 1
    label.config(text=str(pocetni_broj))


def oduzimanje():
    global pocetni_broj
    pocetni_broj -= 1
    label.config(text=str(pocetni_broj))


def resetovanje():
    global pocetni_broj
    pocetni_broj = 0
    label.config(text=str(pocetni_broj))


color_black = "#000000"
color_white = "#ffffff"
color_light_blue = "#75bfff"
color_light_red = "#ff4242"

window = tki.Tk()
window.title("Manual-Counter")
window.resizable(False, False)

frame = tki.Frame(window)

label = tki.Label(frame, background=color_black,
                  foreground=color_white, text="0", font=("Arial", 45), anchor="e")

label.grid(row=0, column=0, columnspan=2, sticky="we")

button_plus = tki.Button(frame, background=color_light_blue, command=dodavanje,
                         foreground=color_white, text="+", font=("Arial", 45))

button_plus.grid(row=1, column=0)

button_minus = tki.Button(frame, background=color_light_red, command=oduzimanje,
                          foreground=color_white, text="-", font=("Arial", 45))

button_minus.grid(row=1, column=1)

reset_button = tki.Button(frame, text="RESET", background=color_white, command=resetovanje,
                          foreground=color_black, font=("Arial", 30))
reset_button.grid(row=2, column=0, columnspan=2, sticky="we")

frame.pack()

# centrirati aplikaciju
window.update()  # azurirati prozor sa novim velicnima
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

