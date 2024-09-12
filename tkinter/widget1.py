import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Entry")

# Función para obtener el texto del Entry cuando se presione un botón
def obtener_texto():
    texto_ingresado = entry.get()  # Obtener el texto del Entry
    etiqueta_resultado.config(text="Texto ingresado: " + texto_ingresado)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Crear un Entry
entry = tk.Entry(ventana)
entry.pack(pady=10)

# Botón para obtener el texto del Entry
boton_obtener = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton_obtener.pack()

# Ejecutar la ventana principal
ventana.mainloop()
