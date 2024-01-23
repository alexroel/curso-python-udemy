from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, padding = 10)
frame.grid()
ttk.Label(frame, text="Hola mundo").grid(column=0, row=0)
ttk.Button(frame, text="Salir", command=root.destroy).grid(column=1, row=0)
root.mainloop()