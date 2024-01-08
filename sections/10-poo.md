# Programación Orientada a Objetos (POO)

1. [Introducción](#introducción)
2. [Clases y objetos en Python](#clases-y-objetos-en-python)
3. [Métodos y atributos de clase](#métodos-y-atributos-de-clase)
4. [Herencia y polimorfismo](#herencia-y-polimorfismo)
5. [Encapsulación y abstracción](#encapsulación-y-abstracción)
6. [Proyecto de sección](#proyecto-de-sección)
7. [Resumen](#resumen)

---
## Introducción
La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en la organización del código en torno a objetos, que son instancias de clases. Aquí tienes algunos conceptos básicos de la POO, acompañados de ejemplos simples en lenguaje Python:

1. **Clase**:
   - Definición: Una clase es un plano o plantilla que describe cómo deben ser los objetos. Contiene atributos (variables) y métodos (funciones) que definen el comportamiento de los objetos.
   - Ejemplo:

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"{self.marca} {self.modelo} arrancando")

    def detener(self):
        print(f"{self.marca} {self.modelo} deteniendo")
```

2. **Objeto**:
   - Definición: Un objeto es una instancia de una clase. Representa una entidad con atributos y comportamientos específicos.
   - Ejemplo:

```python
mi_coche = Coche("Toyota", "Camry")
mi_coche.arrancar()
mi_coche.detener()
```

3. **Atributo**:
   - Definición: Un atributo es una variable que pertenece a un objeto y define sus propiedades.
   - Ejemplo:

```python
mi_coche.marca  # Acceder al atributo 'marca' del objeto
```

4. **Método**:
   - Definición: Un método es una función asociada a una clase que define el comportamiento de los objetos de esa clase.
   - Ejemplo:

```python
mi_coche.arrancar()  # Llamar al método 'arrancar' del objeto
```

5. **Encapsulación**:
   - Definición: La encapsulación es el concepto de ocultar los detalles internos de una clase y proporcionar una interfaz pública para interactuar con los objetos.
   - Ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

juan = Persona("Juan", 30)
print(juan.obtener_nombre())  # Accediendo al atributo 'nombre' a través del método
```

6. **Herencia**:
   - Definición: La herencia permite que una clase (llamada subclase) herede atributos y métodos de otra clase (llamada superclase). La subclase puede agregar o modificar comportamientos.
   - Ejemplo:

```python
class Camion(Coche):
    def cargar(self):
        print(f"Cargando en el {self.marca} {self.modelo}")

mi_camion = Camion("Ford", "F150")
mi_camion.arrancar()
mi_camion.cargar()
```

7. **Polimorfismo**:
   - Definición: El polimorfismo permite que diferentes objetos respondan de manera única a los mismos métodos, lo que facilita la programación genérica.
   - Ejemplo:

```python
def realizar_accion(objeto):
    objeto.arrancar()

realizar_accion(mi_coche)  # Llama al método 'arrancar' de Coche
realizar_accion(mi_camion)  # Llama al método 'arrancar' de Camion
```

Estos son conceptos básicos de la Programación Orientada a Objetos. La POO es una forma poderosa de modelar el mundo real en código y promueve la reutilización y la organización del código.

---
## Clases y objetos en Python
En Python, las clases y los objetos son fundamentales en la programación orientada a objetos (POO). La POO es un paradigma de programación que se basa en la creación de clases para modelar objetos del mundo real y luego crear instancias (objetos) de esas clases para interactuar con ellos. Aquí hay una introducción a cómo trabajar con clases y objetos en Python:

1. **Definir una clase**:

   Para definir una clase en Python, utiliza la palabra clave `class`, seguida del nombre de la clase y un colon. Aquí hay un ejemplo simple de una clase `Persona`:

   ```python
   class Persona:
       def __init__(self, nombre, edad):
           self.nombre = nombre
           self.edad = edad
   ```

   En este ejemplo, hemos definido una clase llamada `Persona` con un constructor `__init__` que inicializa dos atributos: `nombre` y `edad`.

2. **Crear objetos (instancias de la clase)**:

   Para crear un objeto a partir de una clase, simplemente llama al nombre de la clase seguido de paréntesis y asigna la instancia a una variable. Por ejemplo:

   ```python
   persona1 = Persona("Juan", 30)
   persona2 = Persona("María", 25)
   ```

   Ahora tienes dos objetos `persona1` y `persona2` basados en la clase `Persona`.



---
## Métodos y atributos de clase
En Python, puedes definir tanto atributos de instancia como atributos de clase. Los atributos de instancia son específicos de cada objeto creado a partir de la clase, mientras que los atributos de clase son compartidos por todas las instancias de la clase. Además, puedes definir tanto métodos de instancia como métodos de clase. Los métodos de instancia actúan en relación con una instancia específica de la clase, mientras que los métodos de clase actúan en relación con la clase en su conjunto. Aquí tienes un ejemplo que ilustra esto:

```python
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
```

En este ejemplo, "especie" es un atributo de clase que es compartido por todas las instancias de la clase "Persona." El método `presentarse` es un método de instancia que trabaja con los atributos de instancia, mientras que el método `informacion` es un método de clase que puede acceder al atributo de clase.

---
## Herencia y polimorfismo
La herencia y el polimorfismo son conceptos importantes en la programación orientada a objetos que permiten crear jerarquías de clases y trabajar con objetos de diferentes clases de manera más generalizada.

**Herencia:**

La herencia en la programación orientada a objetos es un mecanismo que permite crear una nueva clase basada en una clase existente. La nueva clase hereda los atributos y métodos de la clase base (superclase) y puede agregar nuevos atributos y métodos o modificar los existentes según sea necesario. La clase derivada se llama subclase o clase hija.

Por ejemplo:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

perro = Perro("Fido")
gato = Gato("Whiskers")

print(perro.hablar())  # Output: Woof!
print(gato.hablar())  # Output: Miau!
```

En este ejemplo, la clase `Animal` es la superclase, y `Perro` y `Gato` son subclases que heredan de `Animal`. Cada subclase implementa su propio método `hablar` para proporcionar un comportamiento específico para ese tipo de animal.

**Polimorfismo:**

El polimorfismo es un concepto que permite que los objetos de diferentes clases se comporten de manera similar a través de una interfaz común. En otras palabras, diferentes clases pueden responder de manera específica a las mismas operaciones o métodos.

En el ejemplo anterior, el polimorfismo se manifiesta en el hecho de que tanto el objeto `perro` como el objeto `gato` pueden responder al método `hablar()`, a pesar de que son instancias de clases diferentes. Esto permite escribir un código más genérico que puede funcionar con objetos de diferentes clases que comparten una interfaz común.

El polimorfismo facilita la escritura de código más flexible y reutilizable, ya que se pueden crear funciones y clases que trabajen con objetos polimórficos sin necesidad de conocer la clase concreta de cada objeto.

---
## Encapsulación y abstracción
La encapsulación y la abstracción son dos conceptos fundamentales en la programación orientada a objetos (POO) que ayudan a organizar y gestionar el código de manera eficiente y segura.

**Encapsulación:**

La encapsulación se refiere a la práctica de ocultar los detalles internos de un objeto y proporcionar una interfaz clara y controlada para interactuar con él. En POO, se logra utilizando modificadores de acceso, como públicos, privados y protegidos, para restringir el acceso directo a los atributos y métodos de una clase. La encapsulación se utiliza para proteger los datos internos de una clase y para garantizar que solo se puedan modificar o acceder a través de métodos específicos.

Por ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def hablar(self):
        print(f"{self.__nombre} dice: ¡Hola!")

# Crear una instancia de Persona
persona = Persona("Juan", 30)

# Acceder y modificar atributos mediante métodos
print(persona.get_nombre())  # Obtener nombre: Juan
persona.set_nombre("Pedro")  # Modificar nombre
print(persona.get_nombre())  # Obtener nombre modificado: Pedro

# Esto generaría un error, ya que __nombre es privado
# print(persona.__nombre)
```

En este ejemplo, los atributos `__nombre` y `__edad` son privados y solo se pueden acceder o modificar a través de los métodos `get_nombre` y `set_nombre`, lo que ejemplifica la encapsulación.

**Abstracción:**

La abstracción es el proceso de identificar y enfocarse en las características esenciales de un objeto o sistema, mientras se ignoran los detalles innecesarios. En POO, la abstracción se logra al definir clases y objetos que representan conceptos y entidades del mundo real de manera simplificada y abstracta. Esto permite a los programadores trabajar con representaciones más simples y manejables de los objetos del mundo real, lo que simplifica el diseño y la implementación del software.

Por ejemplo, en un sistema de gestión de biblioteca, puedes crear una clase "Libro" que abstractamente representa las características más importantes de un libro, como título, autor y número de páginas, sin tener que preocuparte por los detalles internos de cómo se almacenan físicamente los libros en la biblioteca.

La abstracción también implica la creación de interfaces y métodos que ocultan los detalles de implementación, permitiendo a los usuarios de una clase centrarse en cómo usarla sin necesidad de conocer cómo se realiza el trabajo interno. Esto facilita la modularidad y el mantenimiento del código.

---
## Proyecto de sección 

---
## Resumen

