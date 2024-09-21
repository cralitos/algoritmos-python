import tkinter as tk

# Función que se llama cuando se hace clic en un Checkbutton
def actualizar_estado():
    estado = "Seleccionado" if check_var.get() else "No seleccionado"
    etiqueta.config(text="Estado: " + estado)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Checkbutton")

# Variable de control para el Checkbutton
check_var = tk.BooleanVar()

# Crear un Checkbutton
checkbutton = tk.Checkbutton(ventana, text="Seleccionar", variable=check_var, command=actualizar_estado)
checkbutton.pack(pady=10)

# Etiqueta para mostrar el estado del Checkbutton
etiqueta = tk.Label(ventana, text="Estado: No seleccionado")
etiqueta.pack()

# Ejecutar la ventana principal
ventana.mainloop()
