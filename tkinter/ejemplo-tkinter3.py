# Importamos la biblioteca Tkinter como 'tk' para crear la interfaz gráfica
import tkinter as tk

# Definimos la función 'mostrar_estado' que se ejecutará cuando se presione el botón
def mostrar_estado():
    # Imprime el estado actual de la casilla de verificación (True o False) en la consola
    print(var.get())

# Creamos la ventana principal de la aplicación
root = tk.Tk()

# Creamos una variable booleana que almacenará el estado de la casilla de verificación (True si está seleccionada, False si no)
var = tk.BooleanVar()

# Creamos una casilla de verificación (Checkbutton) con el texto "Seleccionado" que está vinculada a la variable 'var'
checkButton = tk.Checkbutton(root, text="Seleccionado", variable=var)

# Colocamos la casilla de verificación en la ventana
checkButton.pack()

# Creamos un botón con el texto "mostrar estado" que, al presionarlo, ejecutará la función 'mostrar_estado'
button = tk.Button(root, text="mostrar estado", command=mostrar_estado)

# Colocamos el botón en la ventana
button.pack()

# Iniciamos el bucle principal de la aplicación para mantener la ventana abierta
root.mainloop()
