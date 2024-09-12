#listar archivos en un directorio
import os

directorio = "./"
archivos_directorio = os.listdir(directorio)

print("Archivos y directorios en", directorio)
for item in archivos_directorio:
    print(item)
