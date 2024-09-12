import tkinter as tk

def crear_ventana(nombre):
    ventana = tk.Toplevel(root)
    ventana.title(nombre)
    label = tk.Label(ventana, text=f"Esta es la ventana {nombre}")
    label.pack()
    ventana.geometry("200x100")

def abrir_ventana1():
    crear_ventana("Ventana 1")

def abrir_ventana2():
    crear_ventana("Ventana 2")

def abrir_ventana3():
    crear_ventana("Ventana 3")

# Configuración principal
root = tk.Tk()
root.title("Programa de Ventanas")

# Crear un menú
menu = tk.Menu(root)
root.config(menu=menu)

# Crear un menú desplegable "Ventanas"
ventanas_menu = tk.Menu(menu)
menu.add_cascade(label="Ventanas", menu=ventanas_menu)
ventanas_menu.add_command(label="Ventana 1", command=abrir_ventana1)
ventanas_menu.add_command(label="Ventana 2", command=abrir_ventana2)
ventanas_menu.add_command(label="Ventana 3", command=abrir_ventana3)
ventanas_menu.add_separator()
ventanas_menu.add_command(label="Salir", command=root.quit)

root.mainloop()
