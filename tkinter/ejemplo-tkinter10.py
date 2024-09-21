
#ttk es una submódulo de tkinter que proporciona widgets mejorados con temas (themed widgets). 
#Estos widgets tienen un aspecto más moderno y coherente en diferentes sistemas operativos. 
#Para usar widgets temáticos, debes importar el submódulo ttk por separado y luego usar widgets de ttk

from tkinter import *
from tkinter import ttk
root = Tk()
#se cra un frame del root
frm = ttk.Frame(root, padding=10)
#se crea un grid para organizar los widgets
frm.grid()
#se agrega un label en la primera fila y primera columna
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#se agrega un boton en la primera fila y segunda columna
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()