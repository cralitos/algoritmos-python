# Importamos la biblioteca Tkinter como 'tk' para crear la interfaz gráfica
import tkinter as tk

# Definimos la función 'cambiar_color' que se ejecutará cuando el botón sea presionado
def cambiar_color():
    # Cambia el color de fondo del Frame usando el valor ingresado en el Entry (campo de texto)
    frame.config(bg=color_var.get())

# Creamos la ventana principal de la aplicación
root = tk.Tk()
root.title("Ejemplo de Frame")  # Establecemos el título de la ventana

# Creamos un Frame, que es un contenedor donde podemos colocar otros widgets
# Se le da un tamaño de 200x200 píxeles y un borde sólido
frame = tk.Frame(root, width=200, height=200, borderwidth=2, relief=tk.SOLID)
frame.pack(padx=10, pady=10)  # Colocamos el Frame en la ventana con un margen de 10 píxeles en cada dirección

# Creamos una etiqueta (Label) dentro del Frame, con texto y colores de fondo (azul) y texto (blanco)
label = tk.Label(frame, text="Este es un Frame", fg="white", bg="blue")
label.pack()  # Colocamos la etiqueta dentro del Frame

# Creamos una variable de tipo StringVar que almacenará el valor ingresado por el usuario
color_var = tk.StringVar()

# Creamos un campo de entrada (Entry) dentro del Frame para que el usuario ingrese el nombre del color
color_entry = tk.Entry(frame, textvariable=color_var)
color_entry.pack()  # Colocamos el campo de entrada dentro del Frame

# Creamos un botón que, al ser presionado, ejecutará la función 'cambiar_color'
color_button = tk.Button(frame, text="Cambiar Color", command=cambiar_color)
color_button.pack()  # Colocamos el botón dentro del Frame

# Iniciamos el bucle principal de la aplicación para que la ventana permanezca abierta
root.mainloop()
