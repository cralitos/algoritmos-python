# Importamos la biblioteca Tkinter como 'tk' para crear la interfaz gráfica
import tkinter as tk

# Definimos la función 'mostrar_opcion' que se ejecutará al presionar el botón
def mostrar_opcion():
    # Imprime en la consola la opción seleccionada (el valor de la variable 'opcion')
    print(opcion.get())

# Creamos la ventana principal de la aplicación
root = tk.Tk()

# Creamos una variable de tipo StringVar que almacenará el valor seleccionado de los botones de opción (RadioButtons)
opcion = tk.StringVar()

# Creamos el primer botón de opción (Radiobutton) con el texto "Opción 1"
# El botón está vinculado a la variable 'opcion' y, si es seleccionado, le asigna el valor "Opción 1"
radio1 = tk.Radiobutton(root, text="Opción 1", variable=opcion, value="Opción 1")

# Creamos el segundo botón de opción (Radiobutton) con el texto "Opción 2"
# Este botón asignará el valor "Opción 2" a la variable 'opcion' si es seleccionado
radio2 = tk.Radiobutton(root, text="Opción 2", variable=opcion, value="Opción 2")

# Colocamos los botones de opción en la ventana principal
radio1.pack()
radio2.pack()

# Creamos un botón que, al ser presionado, ejecuta la función 'mostrar_opcion' para mostrar la opción seleccionada
button = tk.Button(root, text="Mostrar opción", command=mostrar_opcion)
button.pack()  # Colocamos el botón en la ventana principal

# Iniciamos el bucle principal de la aplicación para mantener la ventana abierta
root.mainloop()
