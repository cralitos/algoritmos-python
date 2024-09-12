import tkinter as tk

def convertir():
    try:
        # Obtiene el valor ingresado en el campo de entrada
        kilometros = float(entrada_kilometros.get())
        
        # Realiza la conversión a millas (1 kilómetro = 0.621371 millas)
        millas = kilometros * 0.621371
        
        # Actualiza la etiqueta de resultado
        etiqueta_resultado.config(text=f"{kilometros} kilómetros son {millas} millas")
    except ValueError:
        # Manejo de errores para entradas no válidas
        etiqueta_resultado.config(text="Ingrese un valor numérico válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Kilómetros a Millas")
ventana.geometry("300x150")  # Establece el tamaño de la ventana

# Crear etiqueta de instrucción y colocarla en la cuadrícula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kilómetros:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Crear campo de entrada y colocarlo en la cuadrícula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

# Crear botón de conversión y colocarlo en la cuadrícula
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

# Crear etiqueta de resultado y colocarla en la cuadrícula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación
ventana.mainloop()
