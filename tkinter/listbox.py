import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()
    for idx in seleccion:
        print(listbox.get(idx))

root = tk.Tk()
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")

button = tk.Button(root, text="Mostrar selección", command=mostrar_seleccion)
button.pack()
root.mainloop()


