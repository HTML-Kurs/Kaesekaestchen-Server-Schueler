from tkinter import *
import os
from tkinter.ttk import Combobox
from gui.player_util import create_game

def load_bots(folder="./bots/"):
    return [(folder + f) for f in os.listdir(folder) if f.split(".")[-1]=="py"]



def startgame():
    bot = selected_bot.get()
    tm = float(time_nput.get())
    rnd = both_val.get()
    create_game(bot, tm, rnd)


def setup():
    window = Tk()

    window.title("Käsekästchen Server")

    window.configure(width=500, height=300)

    available_ais = load_bots()

    global selected_bot
    selected_bot = StringVar()
    combobox_selected1 = Combobox(window, textvariable=selected_bot)
    combobox_selected1['values'] = available_ais
    combobox_selected1.grid(column=1, row=6)
    combobox_selected1.current()
    selected_bot.set(available_ais[0])
    combobox_selected1.set(available_ais[0])

    vs_label = Label(window, text="vs")
    vs_label.grid(column=2, row=6)

    time_label = Label(window, text="Zeit für KI: ")
    time_label.grid(column=1, row=4)

    global time_nput
    time_nput = Entry(window)
    time_nput.insert(0, "1.0")
    time_nput.grid(column=2, row=4)

    round_label = Label(window, text="Als zweites Spielen: ")
    round_label.grid(column=1, row=3)
    global both_val
    both_val = BooleanVar()
    both_val.set(True)
    both_nput = Checkbutton(variable=both_val)
    both_nput.grid(column=2, row=3)



    b = Button(window, command=startgame, text="Spiel Starten")
    b.grid(column=2, row=7)

    window.mainloop()

setup()