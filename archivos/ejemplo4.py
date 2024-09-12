# Abre múltiples archivos en un contexto
with open('archivo1.txt', 'r') as archivo1, open('archivo2.txt', 'r') as archivo2:
    contenido1 = archivo1.read()
    contenido2 = archivo2.read()
    print(contenido1)
    print(contenido2)
