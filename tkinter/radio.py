

import tkinter as tk

def mostrar_opcion():
    print(opcion.get())

root = tk.Tk()
opcion = tk.StringVar()

radio1 = tk.Radiobutton(root, text="Opción 1", variable=opcion, value="Opción 1")
radio2 = tk.Radiobutton(root, text="Opción 2", variable=opcion, value="Opción 2")

radio1.pack()
radio2.pack()

button = tk.Button(root, text="Mostrar opción", command=mostrar_opcion)
button.pack()
root.mainloop()
