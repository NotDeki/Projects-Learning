import tkinter as tki

# Nizovi za grid set-up

button_values = [
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""]
]

# Varijable

prvi_broj = "0"
drugi_broj = "0"
operacija = "0"

broj_redova = len(button_values)  # 5
broj_colona = len(button_values[0])  # 3

color_orange = "#ffc067"
color_light_blue = "#66f4ff"
color_blue = "#66c4ff"
color_grey = "#7d99aa"
color_dark_blue = "#0a374f"
color_white = "white"

window = tki.Tk()
window.title("Kalkulatro prosta verzija")
window.resizable(False, False)

# funkcije za unos brojeva


def unos_broja_1():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="1")
    else:
        novi_broj = trenutni_broj + "1"
        label.config(text=novi_broj)


def unos_broja_2():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="2")
    else:
        novi_broj = trenutni_broj + "2"
        label.config(text=novi_broj)


def unos_broja_3():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="3")
    else:
        novi_broj = trenutni_broj + "3"
        label.config(text=novi_broj)


def unos_broja_4():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="4")
    else:
        novi_broj = trenutni_broj + "4"
        label.config(text=novi_broj)


def unos_broja_5():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="5")
    else:
        novi_broj = trenutni_broj + "5"
        label.config(text=novi_broj)


def unos_broja_6():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="6")
    else:
        novi_broj = trenutni_broj + "6"
        label.config(text=novi_broj)


def unos_broja_7():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="7")
    else:
        novi_broj = trenutni_broj + "7"
        label.config(text=novi_broj)


def unos_broja_8():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="8")
    else:
        novi_broj = trenutni_broj + "8"
        label.config(text=novi_broj)


def unos_broja_9():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="9")
    else:
        novi_broj = trenutni_broj + "9"
        label.config(text=novi_broj)


def unos_broja_0():
    trenutni_broj = label.cget("text")
    if trenutni_broj == "0":
        label.config(text="0")
    else:
        novi_broj = trenutni_broj + "0"
        label.config(text=novi_broj)


def unos_decimalnog_broja():
    trenutni_broj = label.cget("text")
    decimalna_tacka = "."
    if decimalna_tacka not in trenutni_broj:
        label.config(text=trenutni_broj+decimalna_tacka)

# funkcije za matematicke operacije


def kvadriranje():
    global prvi_broj, operacija
    prvi_broj = label.cget("text")
    operacija = "kvadriranje"
    label.config(text=prvi_broj + "^2")


def korenovanje():
    global operacija, prvi_broj
    prvi_broj = label.cget("text")
    koren = "√"
    operacija = "korenovanje"
    if prvi_broj == "0":
        if prvi_broj not in prvi_broj:
            label.config(text=koren)
    elif prvi_broj != "0":
        if koren not in prvi_broj:
            label.config(text=koren + prvi_broj)


def sabiranje():
    global prvi_broj, operacija
    prvi_broj = label.cget("text")
    operacija = "sabiranje"
    label.config(text="0")


def oduzimanje():
    global prvi_broj, operacija
    prvi_broj = label.cget("text")
    operacija = "oduzimanje"
    label.config(text="0")


def mnozenje():
    global prvi_broj, operacija
    prvi_broj = label.cget("text")
    operacija = "mnozenje"
    label.config(text="0")


def deljenje():
    global prvi_broj, operacija
    prvi_broj = label.cget("text")
    operacija = "deljenje"
    label.config(text="0")


def jednako():
    drugi_broj = label.cget("text")
    if operacija == "sabiranje":
        rezultat = str(float(prvi_broj)+float(drugi_broj))
        label.config(text=rezultat)
    elif operacija == "oduzimanje":
        rezultat = str(float(prvi_broj)-float(drugi_broj))
        label.config(text=rezultat)
    elif operacija == "mnozenje":
        rezultat = str(float(prvi_broj)*float(drugi_broj))
        label.config(text=rezultat)
    elif operacija == "deljenje":
        rezultat = float(prvi_broj)/float(drugi_broj)
        rezultat = str(round(rezultat, 5))
        label.config(text=rezultat)
    elif operacija == "kvadriranje":
        rezultat = float(prvi_broj)*float(prvi_broj)
        rezultat = str(round(rezultat, 5))
        label.config(text=rezultat)
    elif operacija == "korenovanje":
        rezultat = float(prvi_broj)**0.5
        rezultat = str(round(rezultat, 5))
        label.config(text=rezultat)


def resetovanje():
    label.config(text="0")


# widgeti (Ram,label i dugmici)

frame = tki.Frame(window, background=color_dark_blue)

label = tki.Label(frame, text="0", background=color_dark_blue, anchor="e",
                  foreground=color_white, font=("Arial", 45), width=broj_colona)
label.grid(row=0, column=0, columnspan=broj_colona, sticky="we")

button1 = tki.Button(frame, background=color_grey, command=resetovanje,
                     foreground=color_white, text="AC", font=("Arial", 30), width=broj_colona-1, height=1)
button1.grid(row=1, column=0)

button2 = tki.Button(frame, background=color_grey, command=unos_broja_0,
                     foreground=color_white, text="0", font=("Arial", 30), width=broj_colona-1, height=1)
button2.grid(row=1, column=1)

button3 = tki.Button(frame, background=color_grey, command=jednako,
                     foreground=color_white, text="=", font=("Arial", 30), width=broj_colona-1, height=1)
button3.grid(row=1, column=2)

button4 = tki.Button(frame, background=color_orange, command=unos_broja_9,
                     foreground=color_white, text="9", font=("Arial", 30), width=broj_colona-1, height=1)
button4.grid(row=2, column=2)

button5 = tki.Button(frame, background=color_orange, command=unos_broja_8,
                     foreground=color_white, text="8", font=("Arial", 30), width=broj_colona-1, height=1)
button5.grid(row=2, column=1)

button6 = tki.Button(frame, background=color_orange,  command=unos_broja_7,
                     foreground=color_white, text="7", font=("Arial", 30), width=broj_colona-1, height=1)
button6.grid(row=2, column=0)

button7 = tki.Button(frame, background=color_orange, command=unos_broja_6,
                     foreground=color_white, text="6", font=("Arial", 30), width=broj_colona-1, height=1)
button7.grid(row=3, column=2)

button8 = tki.Button(frame, background=color_orange, command=unos_broja_5,
                     foreground=color_white, text="5", font=("Arial", 30), width=broj_colona-1, height=1)
button8.grid(row=3, column=1)

button9 = tki.Button(frame, background=color_orange, command=unos_broja_4,
                     foreground=color_white, text="4", font=("Arial", 30), width=broj_colona-1, height=1)
button9.grid(row=3, column=0)

button10 = tki.Button(frame, background=color_orange, command=unos_broja_3,
                      foreground=color_white, text="3", font=("Arial", 30), width=broj_colona-1, height=1)
button10.grid(row=4, column=2)

button11 = tki.Button(frame, background=color_orange, command=unos_broja_2,
                      foreground=color_white, text="2", font=("Arial", 30), width=broj_colona-1, height=1)
button11.grid(row=4, column=1)

button12 = tki.Button(frame, background=color_orange, command=unos_broja_1,
                      foreground=color_white, text="1", font=("Arial", 30), width=broj_colona-1, height=1)
button12.grid(row=4, column=0)

button13 = tki.Button(frame, background=color_blue, command=sabiranje,
                      foreground=color_white, text="+", font=("Arial", 30), width=broj_colona-1, height=1)
button13.grid(row=1, column=3)

button14 = tki.Button(frame, background=color_blue, command=oduzimanje,
                      foreground=color_white, text="-", font=("Arial", 30), width=broj_colona-1, height=1)
button14.grid(row=2, column=3)

button15 = tki.Button(frame, background=color_blue, command=mnozenje,
                      foreground=color_white, text="×", font=("Arial", 30), width=broj_colona-1, height=1)
button15.grid(row=3, column=3)

button16 = tki.Button(frame, background=color_blue, command=deljenje,
                      foreground=color_white, text="÷", font=("Arial", 30), width=broj_colona-1, height=1)
button16.grid(row=4, column=3)

button17 = tki.Button(frame, background=color_orange, command=unos_decimalnog_broja,
                      foreground=color_white, text=".", font=("Arial", 30), width=broj_colona-1, height=1)
button17.grid(row=5, column=0)

button18 = tki.Button(frame, background=color_orange, command=kvadriranje,
                      foreground=color_white, text="^2", font=("Arial", 30), width=broj_colona-1, height=1)
button18.grid(row=5, column=1)

button19 = tki.Button(frame, background=color_orange, command=korenovanje,
                      foreground=color_white, text="√", font=("Arial", 30), width=broj_colona-1, height=1)
button19.grid(row=5, column=2)


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
