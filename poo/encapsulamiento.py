class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Atributo privado
        self.__salario = salario  # Atributo privado

    def obtener_nombre(self):
        return self.__nombre  # Método para obtener el nombre

    def obtener_salario(self):
        return self.__salario  # Método para obtener el salario

    def modificar_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario  # Método para modificar el salario

# Crear una instancia de la clase Empleado
empleado1 = Empleado("Juan", 50000)

# Intentar acceder directamente a los atributos privados (esto generará un error)
# print(empleado1.__nombre)
# print(empleado1.__salario)

# Acceder a los atributos a través de los métodos públicos
nombre_empleado = empleado1.obtener_nombre()
salario_empleado = empleado1.obtener_salario()
print(f"Nombre: {nombre_empleado}, Salario: ${salario_empleado}")

# Modificar el salario a través de un método público
empleado1.modificar_salario(55000)
print(f"Nuevo salario: ${empleado1.obtener_salario()}")
