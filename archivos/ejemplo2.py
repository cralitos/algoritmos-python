# Abre un archivo en modo de lectura y lee línea por línea
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina los caracteres de nueva línea al final de cada línea
