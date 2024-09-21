# Importamos la biblioteca Tkinter como 'tk' para crear la interfaz gráfica
import tkinter as tk  

# Definimos la función 'hacer_algo' que se ejecutará cuando se haga clic en el botón
def hacer_algo():
    # Imprime un mensaje en la consola cuando el botón es presionado
    print("hiciste click en el boton")  

# Creamos la ventana principal de la aplicación
root = tk.Tk()

# Creamos un botón con el texto "Haz algo" y asignamos la función 'hacer_algo' como el comando que se ejecutará al hacer clic
button = tk.Button(root, text="Haz algo", command=hacer_algo)

# Colocamos el botón en la ventana usando el método 'pack', que lo organiza de manera predeterminada
button.pack()

# Iniciamos el bucle principal de la aplicación, que mantiene la ventana abierta y activa
root.mainloop()
