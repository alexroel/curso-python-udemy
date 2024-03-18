print("Hola Mundo")

# Hola este es un comentario 

# Creando una clase en python 

class Person:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Persona[Nombre: {self.nombre}, Edad: {self.edad}]"

# Instancia de una clase

p1 = Person("Alex", 29)

print(p1)