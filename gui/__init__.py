from tkinter import *
import os
from tkinter.ttk import Combobox

from gui.util import create_game


def load_bots(folder="./bots/"):
    return [(folder + f) for f in os.listdir(folder) if f.split(".")[-1]=="py"]

def startgame():
    bot1 = selected_bot_1.get()
    bot2 = selected_bot_2.get()
    tm = float(time_nput.get())
    rnd = both_val.get()
    tv = t_val.get()
    create_game(bot1, bot2, tm, rnd, tv)


def setup():
    window = Tk()

    window.title("Käsekästchen Server")

    window.configure(width=500, height=300)

    available_ais = load_bots()

    global selected_bot_1
    selected_bot_1 = StringVar()
    combobox_selected1 = Combobox(window, textvariable=selected_bot_1)
    combobox_selected1['values'] = available_ais
    combobox_selected1.grid(column=1, row=6)
    combobox_selected1.current()
    selected_bot_1.set(available_ais[0])
    combobox_selected1.set(available_ais[0])

    vs_label = Label(window, text="vs")
    vs_label.grid(column=2, row=6)

    global selected_bot_2
    selected_bot_2 = StringVar()
    combobox_selected2 = Combobox(window, textvariable=selected_bot_2)
    combobox_selected2['values'] = available_ais
    combobox_selected2.grid(column=3, row=6)
    combobox_selected2.current()
    selected_bot_2.set(available_ais[0])
    combobox_selected2.set(available_ais[0])

    time_label = Label(window, text="Zeit: ")
    time_label.grid(column=1, row=4)

    global time_nput
    time_nput = Entry(window)
    time_nput.insert(0, "1.0")
    time_nput.grid(column=2, row=4)

    round_label = Label(window, text="Beide Richtungen: ")
    round_label.grid(column=1, row=3)
    global both_val
    both_val = BooleanVar()
    both_val.set(True)
    both_nput = Checkbutton(variable=both_val)
    both_nput.grid(column=2, row=3)

    round_label = Label(window, text="Langsam spielen: ")
    round_label.grid(column=1, row=5)
    global t_val
    t_val = BooleanVar()
    both_nput = Checkbutton(variable=t_val)
    t_val.set(True)
    both_nput.grid(column=2, row=5)


    b = Button(window, command=startgame, text="Spiel Starten")
    b.grid(column=2, row=7)

    window.mainloop()
