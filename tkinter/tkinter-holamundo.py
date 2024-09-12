import tkinter as tk

#crear la raíz de nuestra aplicación usando es Clase Tk:
root = tk.Tk()

label = tk.Label(root, text="Hola mundo")
#le provee una ubicacion dentro de la ventana
label.pack(padx=500, pady=100 )

#se inicializa ingresado al loop de enventos principal
root.mainloop()