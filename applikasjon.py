import tkinter as tk
from tkinter import Label, Entry, Menubutton, Menu

root = tk.Tk()
root.title("Login")
root.geometry("500x1000")
root.maxsize(600, 450)
root.minsize(600, 450)
root.config(bg="lightgrey")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="fil", menu=file_menu)
file_menu.add_command(label="ny")
file_menu.add_command(label="åpne")
file_menu.add_command(label="lagre")
file_menu.add_separator()
file_menu.add_command(label="avslutt", command=root.quit)

root.mainloop()