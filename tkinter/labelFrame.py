import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    seleccion = combo_var.get()
    resultado_label.config(text=f"Seleccionaste: {seleccion}")

root = tk.Tk()
root.title("Ejemplo de LabelFrame")

# Crear un LabelFrame
frame = ttk.LabelFrame(root, text="Selecciona una opción")

# Agregar widgets al LabelFrame
combo_var = tk.StringVar()
combo = ttk.Combobox(frame, textvariable=combo_var, values=["Opción 1", "Opción 2", "Opción 3"])
button = ttk.Button(frame, text="Mostrar selección", command=mostrar_seleccion)
resultado_label = ttk.Label(frame, text="")

combo.pack()
button.pack()
resultado_label.pack()

frame.pack(padx=10, pady=10)

root.mainloop()
