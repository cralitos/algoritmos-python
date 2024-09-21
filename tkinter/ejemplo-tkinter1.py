import tkinter as tk  # Importamos la biblioteca Tkinter y la renombramos como 'tk' para facilitar su uso.

# Definimos una función que imprimirá el texto ingresado en el campo de entrada.
def imprimirTexto():
    print(entry.get())  # Usamos 'entry.get()' para obtener el texto del campo de entrada y lo imprimimos en la consola.

# Creamos la ventana principal.
root = tk.Tk()

# Creamos un campo de entrada de texto donde el usuario puede escribir.
entry = tk.Entry(root)
entry.pack()  # Colocamos el campo de entrada en la ventana usando el método 'pack()'.

# Creamos un botón con el texto "Imprimir" y asignamos la función 'imprimirTexto' para que se ejecute al hacer clic.
button = tk.Button(root, text="Imprimir", command=imprimirTexto)
button.pack()  # Colocamos el botón en la ventana también usando 'pack()'.

# Iniciamos el bucle principal de la aplicación. Mantiene la ventana abierta y responde a las interacciones del usuario.
root.mainloop()
