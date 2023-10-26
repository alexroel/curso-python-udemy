class Persona:
    # Atributo de clase
    especie = "Homo sapiens"

    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    # Método de clase
    @classmethod
    def informacion(cls):
        return f"Las personas pertenecen a la especie {cls.especie}."

# Crear instancias de Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

# Acceder a atributos de instancia
print(persona1.nombre)  # Juan
print(persona2.nombre)  # Maria

# Acceder a atributo de clase
print(persona1.especie)  # Homo sapiens
print(persona2.especie)  # Homo sapiens

# Llamar a métodos de instancia
print(persona1.presentarse())  # Hola, soy Juan y tengo 30 años.
print(persona2.presentarse())  # Hola, soy Maria y tengo 25 años.

# Llamar a método de clase
print(Persona.informacion())  # Las personas pertenecen a la especie Homo sapiens.
