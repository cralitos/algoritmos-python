class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"¡Hola! Soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def estudiar(self):
        return f"{self.nombre} está estudiando con la matrícula {self.matricula}."

class Profesor(Persona):
    def __init__(self, nombre, edad, codigo_empleado):
        super().__init__(nombre, edad)
        self.codigo_empleado = codigo_empleado

    def enseñar(self):
        return f"{self.nombre} está enseñando con el código de empleado {self.codigo_empleado}."

# Crear instancias de las clases
persona1 = Persona("Juan", 30)
estudiante1 = Estudiante("Ana", 20, "ES12345")
profesor1 = Profesor("Dr. Smith", 45, "P123")

# Usar métodos de las instancias
print(persona1.presentarse())
print(estudiante1.presentarse())
print(estudiante1.estudiar())
print(profesor1.presentarse())
print(profesor1.enseñar())
