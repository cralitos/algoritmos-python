# Abre un archivo en modo de lectura y lee los primeros 50 caracteres
with open('archivo.txt', 'r') as archivo:
    primeros_50_caracteres = archivo.read(50)
    print(primeros_50_caracteres)
