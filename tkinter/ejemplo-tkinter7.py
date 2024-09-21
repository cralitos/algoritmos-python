# Importamos la biblioteca Tkinter como 'tk' para crear la interfaz gráfica
import tkinter as tk

# Creamos la ventana principal de la aplicación
root = tk.Tk()

# Establecemos el título de la ventana
root.title("Ejemplo de Message")

# Crear un widget 'Message' que permite mostrar texto multilínea
# El texto es un mensaje largo que se ajustará automáticamente según el ancho definido
mensaje = tk.Message(root, text="Este es un ejemplo de un mensaje multilínea en Tkinter.", width=200)

# Configuramos el ancho máximo del mensaje a 300 píxeles, lo que hará que el texto se ajuste en varias líneas si es necesario
mensaje.config(width=30)

# Configuramos el color de fondo del widget 'Message' a azul claro ('lightblue')
mensaje.config(bg='lightblue')

# Colocamos el widget 'Message' en la ventana principal
mensaje.pack()

# Iniciamos el bucle principal de la aplicación para mantener la ventana abierta
root.mainloop()
