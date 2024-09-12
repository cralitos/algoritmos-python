# Abre un archivo en modo de añadir (si no existe, se crea)
with open('archivo_prueba.txt', 'a') as archivo:
    archivo.write('\nEste es un nuevo contenido añadido al archivo.')
