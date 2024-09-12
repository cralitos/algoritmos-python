#verifica si un archivo existe
import os

archivo_o_directorio = "./archivo4.txt"

if os.path.exists(archivo_o_directorio):
    print(archivo_o_directorio, "existe")
else:
    print(archivo_o_directorio, "no existe")
