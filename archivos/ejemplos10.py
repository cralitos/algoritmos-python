#borrar un archivo o carpeta
import os

archivo_o_directorio = "archivo11.txt"

if os.path.exists(archivo_o_directorio):
    if os.path.isfile(archivo_o_directorio):
        os.remove(archivo_o_directorio)  # Eliminar un archivo
    else:
        os.rmdir(archivo_o_directorio)  # Eliminar un directorio vacío
else:
    print(archivo_o_directorio, "no existe")
