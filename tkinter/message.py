import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Message")

# Crear un widget Message
mensaje = tk.Message(root, text="Este es un ejemplo de un mensaje multilínea en Tkinter.", width=200)

# Configurar el ancho máximo del mensaje (en píxeles) antes de que se ajuste automáticamente
mensaje.config(width=52)

# Configurar el fondo del mensaje
mensaje.config(bg='lightblue')

# Añadir el mensaje a la ventana
mensaje.pack()

root.mainloop()
