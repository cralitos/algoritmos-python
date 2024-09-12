#obtener informacion de un archivo
import os

archivo_o_directorio = "archivo2.txt"

if os.path.exists(archivo_o_directorio):
    info = os.stat(archivo_o_directorio)
    print("Información de", archivo_o_directorio)
    print("Tamaño:", info.st_size, "bytes")
    print("Última modificación:", info.st_mtime)
