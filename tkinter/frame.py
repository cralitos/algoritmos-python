import tkinter as tk

def cambiar_color():
    frame.config(bg=color_var.get())

root = tk.Tk()
root.title("Ejemplo de Frame")

# Crear un Frame
frame = tk.Frame(root, width=200, height=100, borderwidth=2, relief=tk.SOLID)
frame.pack(padx=10, pady=10)

# Agregar widgets al Frame
label = tk.Label(frame, text="Este es un Frame", fg="white", bg="blue")
label.pack()

color_var = tk.StringVar()
color_entry = tk.Entry(frame, textvariable=color_var)
color_entry.pack()

color_button = tk.Button(frame, text="Cambiar Color", command=cambiar_color)
color_button.pack()

root.mainloop()
