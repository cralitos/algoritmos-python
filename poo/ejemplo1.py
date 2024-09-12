class Animal:

    #Metodo constructor
    def __init__(self, nombre, especie):
        #atributos de clase
        self.nombre = nombre
        self.especie = especie
        self.hambre = 100

    #Metodo alimentar
    def alimentar(self, cantidad):
        self.hambre -= cantidad
        if self.hambre < 0:
            self.hambre = 0

    #Metodo hacer sonido
    def hacer_sonido(self):
        #el metodo no tiene logica
        pass


mi_perro = Animal("Rex", "Perro")
mi_gato = Animal("Whiskers", "Gato")

mi_perro.alimentar(20)
mi_gato.alimentar(30)

print(f"{mi_perro.nombre} tiene un nivel de hambre de {mi_perro.hambre}")
print(f"{mi_gato.nombre} tiene un nivel de hambre de {mi_gato.hambre}")
