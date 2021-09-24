from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
import os 


window = Tk()


window.title("Bloc-note")
window.geometry("700x600")
window.minsize(699, 599)
text1 = tk.Text(window, height=100, width=100)
text1.pack()


def save():
    rex = text1.get("1.0","end")
    open = os.open("montexte.txt", os.O_RDWR | os.O_CREAT)
    os.write(open, str(rex).encode("UTF-8"))
    os.close(open)


menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New")
menu1.add_command(label="Save", command=save())
menu1.add_command(label="Open")
menu1.add_command(label="Edit")
menu1.add_separator()
menu1.add_command(label="Quit")
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="A propos")
menubar.add_cascade(label="Help", menu=menu2)

window.config(menu=menubar)

# cree la boucle
window.mainloop()