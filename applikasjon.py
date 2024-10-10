import tkinter as tk

root = tk.Tk()
root.title("PythonApp")

root.geometry("400x300")

label = tk.Label(root, text="Hallo")
label.pack()

button = tk.Button(root, text="Button", command=lambda:
label.config(text="Button Pressed"))
button.pack()

root.mainloop()

