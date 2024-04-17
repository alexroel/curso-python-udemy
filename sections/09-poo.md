# Programación Orientada a Objetos en Python

1. [Introducción](#introducción)
2. [Python y POO](#python-y-poo)
2. [Clases y objetos](#clases-y-objetos)
3. [Métodos y atributos de instancia](#métodos-y-atributos-de-instancia)
4. [Herencia y polimorfismo](#herencia-y-polimorfismo)
5. [Encapsulación](#encapsulación)
6. [Proyecto de sección: Registro de mascotas](#proyecto-de-sección-registro-de-mascotas)
7. [Resumen](#resumen)

---
## Introducción

---
## Python y POO

La Programación Orientada a Objetos (POO) es un paradigma de programación ampliamente utilizado en Python y en muchos otros lenguajes de programación modernos. En este artículo, exploraremos los conceptos básicos de la POO en Python, incluyendo qué es un objeto, qué es una clase, y cómo se utilizan en la práctica.

**¿Qué es la Programación Orientada a Objetos?**

La Programación Orientada a Objetos es un enfoque de desarrollo de software que se basa en el concepto de "objetos". Estos objetos son entidades que combinan datos (también conocidos como atributos) y funcionalidades (métodos o acciones que el objeto puede realizar). La POO organiza el código de una manera que refleja el mundo real, lo que facilita la modelización y resolución de problemas complejos.

**¿Qué es un Objeto?**

Un objeto es una instancia particular de una clase. Una clase es como un plano o una plantilla que define las propiedades y comportamientos comunes a un conjunto de objetos relacionados. Por ejemplo, si tienes una clase llamada `Tarea`, cada tarea individual (como "Tomar curso de Python" o "Crear proyecto personal") sería un objeto de esa clase.

**¿Qué es una Clase?**

Una clase es un tipo de dato definido por el programador que especifica tanto los datos como las operaciones que se pueden realizar en esos datos. Las clases son la base de la POO en Python. Definen la estructura y el comportamiento de los objetos. Por ejemplo, en nuestro caso, podríamos tener una clase `Tarea` que tenga atributos como "Descripción" y "Estado", y métodos como "Marcar como completado" y "Actualizar".

**Ejemplo Práctico**

Veamos un ejemplo práctico de cómo se vería esto en código Python:

```python
class Tarea:
    def __init__(self, descripcion, estado):
        self.descripcion = descripcion
        self.estado = estado

    def marcar_como_completado(self):
        self.estado = "Completado"

    def actualizar(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

# Creación de objetos Tarea
tarea1 = Tarea("Tomar curso de Python", "Pendiente")
tarea2 = Tarea("Crear proyecto personal", "Pendiente")
tarea3 = Tarea("Aprender HTML", "Completado")

# Uso de métodos en los objetos
tarea1.marcar_como_completado()
tarea2.actualizar("Crear un nuevo proyecto")

# Imprimir información de las tareas
print("Tarea 1:", tarea1.descripcion, "-", tarea1.estado)
print("Tarea 2:", tarea2.descripcion, "-", tarea2.estado)
print("Tarea 3:", tarea3.descripcion, "-", tarea3.estado)
```

En este ejemplo, creamos una clase `Tarea` con atributos `descripcion` y `estado`, y métodos `marcar_como_completado` y `actualizar`. Luego creamos tres objetos `tarea1`, `tarea2` y `tarea3`, y los manipulamos utilizando los métodos de la clase.


**En python todo esta basado en objetos y clases**
Absolutamente. En Python, todo es un objeto. Esto significa que todo, desde números y cadenas de texto hasta funciones y módulos, se representan internamente como objetos. Además, Python es un lenguaje de programación orientado a objetos, lo que significa que está diseñado para facilitar la creación y manipulación de objetos y clases.

Por ejemplo, incluso los tipos de datos básicos como enteros y listas son en realidad objetos en Python. Cuando defines una variable que contiene un número entero, estás creando un objeto de la clase `int`. Lo mismo ocurre con las cadenas de texto, listas, tuplas y diccionarios. Cada uno de estos tipos de datos tiene métodos y atributos asociados que puedes utilizar para manipularlos.

La orientación a objetos en Python te permite organizar tu código de manera más estructurada y reutilizable. Puedes crear tus propias clases para representar conceptos específicos en tu programa, lo que te permite encapsular datos y funcionalidades relacionadas en un solo lugar. Esto promueve la modularidad y el mantenimiento del código, lo que facilita la colaboración y la escalabilidad de tus proyectos.

---
## Clases y objetos

En la programación orientada a objetos (POO), las clases y los objetos son elementos fundamentales que nos permiten modelar el mundo real de manera eficiente en nuestros programas. En este artículo, aprenderás cómo crear clases y objetos en Python, junto con ejemplos prácticos.

**¿Qué son las Clases y los Objetos?**

En POO, una clase es un plano para crear objetos. Define los atributos (variables) y métodos (funciones) que los objetos de esa clase pueden tener. Por otro lado, un objeto es una instancia de una clase, es decir, una realización concreta de esa clase.

**Creación de Clases**

Para definir una clase en Python, utilizamos la palabra clave `class`, seguida del nombre de la clase y dos puntos. Dentro de la clase, podemos definir atributos y métodos.

```python
class Animal:
    especie = ""
    edad = 0
```

En este ejemplo, hemos creado una clase llamada `Animal` con dos atributos: `especie` y `edad`.

**Creación de Objetos**

Una vez que hemos definido una clase, podemos crear objetos (instancias de esa clase) utilizando el nombre de la clase seguido de paréntesis. Si la clase tiene un constructor definido (`__init__`), podemos pasar argumentos al crear el objeto.

```python
animal1 = Animal()
animal1.especie = "Perro"
animal1.edad = "1 Año"

animal2 = Animal()
animal2.especie = "Gato"
animal2.edad = "6 Meses"
```

En este código, hemos creado dos objetos `animal1` y `animal2`, ambos pertenecientes a la clase `Animal`. Luego, hemos asignado valores a los atributos `especie` y `edad` de cada objeto.

**Accediendo a los Atributos y Métodos de los Objetos**

Una vez que hemos creado objetos, podemos acceder a sus atributos y métodos utilizando la notación de punto (`.`). Por ejemplo, para acceder al atributo `especie` del `animal1`, podemos escribir `animal1.especie`.

```python
print(animal1.especie)  # Salida: Perro
print(animal2.edad)      # Salida: 6 Meses
```

También podemos definir métodos dentro de una clase y luego llamar a esos métodos en los objetos.

---
## Atributos y métodos de instancia
En la programación orientada a objetos (POO), los atributos y métodos de instancia son características y acciones específicas de cada objeto. En este artículo, exploraremos cómo trabajar con ellos en Python, incluyendo el constructor, los atributos de instancia y los métodos de instancia.

**Constructor**

El constructor es un método especial en Python que se llama automáticamente cuando creamos un objeto de una clase. Es utilizado para inicializar los atributos de la instancia. En Python, el constructor se define utilizando el método `__init__`.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
```

En este ejemplo, el constructor `__init__` toma dos parámetros (`especie` y `edad`) y los asigna a los atributos de instancia `self.especie` y `self.edad`.

**Atributos de Instancia**

Los atributos de instancia son variables que pertenecen a cada objeto individualmente. Se definen dentro del constructor o en cualquier otro método de la clase utilizando la notación `self.nombre_atributo`.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
```

En este caso, `especie` y `edad` son atributos de instancia de la clase `Animal`.

**Métodos de Instancia**

Los métodos de instancia son funciones definidas dentro de una clase que pueden acceder y modificar los atributos de esa clase. Se definen de la misma manera que las funciones normales, pero toman un parámetro adicional `self`, que hace referencia al objeto actual.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def info(self):
        print(f"Especie: {self.especie}, Edad: {self.edad}")
```

En este ejemplo, `info()` es un método de instancia que imprime la especie y la edad del animal.

**Ejemplo Práctico**

```python
animal1 = Animal("Perro", "1 Año")
animal1.info()
```

Este código crea un objeto `animal1` de la clase `Animal` con la especie "Perro" y la edad "1 Año", y luego llama al método `info()` para imprimir la información del animal.

---
## Herencia y polimorfismo
En la programación orientada a objetos (POO), la herencia y el polimorfismo son conceptos poderosos que nos permiten construir programas más flexibles y reutilizables al aprovechar la relación entre clases. En este artículo, exploraremos cómo utilizar la herencia y el polimorfismo en Python, con ejemplos prácticos.

**Herencia**

La herencia es un concepto fundamental en POO que permite a una clase (llamada subclase o clase derivada) heredar atributos y métodos de otra clase (llamada superclase o clase base). Esto permite la reutilización de código y la creación de una jerarquía de clases.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"


class Perro(Animal):
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"
```

En este ejemplo, `Perro` y `Gato` son subclases de la clase `Animal`. Esto significa que heredan los atributos y métodos de la clase `Animal`. Sin embargo, pueden tener sus propios métodos y atributos adicionales.

**Polimorfismo**

El polimorfismo es otro concepto importante en POO que se refiere a la capacidad de objetos de diferentes clases de responder al mismo mensaje de manera distinta. En otras palabras, objetos de diferentes clases pueden compartir el mismo nombre de método, pero cada clase puede implementar ese método de manera diferente.

```python
perro = Perro("Fido", 3)
gato = Gato("Pelusa", 2)

print(perro.hablar())  # Salida: Woof!
print(gato.hablar())   # Salida: Miau!
```

En este ejemplo, tanto `Perro` como `Gato` tienen un método `hablar()`, pero cada uno lo implementa de manera diferente. Esto es polimorfismo en acción: objetos diferentes respondiendo al mismo mensaje de manera diferente.

**Beneficios de Herencia y Polimorfismo**

- **Reutilización de código**: Al heredar de una clase base, las subclases pueden aprovechar los atributos y métodos de la clase base, evitando la duplicación de código.
- **Flexibilidad y extensibilidad**: Las subclases pueden agregar nuevos métodos y atributos, lo que permite extender el comportamiento de la clase base.
- **Polimorfismo**: Permite escribir código más genérico y flexible, ya que los objetos de diferentes clases pueden comportarse de manera diferente en función del contexto.


---
## Encapsulación
La encapsulación es un concepto en programación orientada a objetos (POO) que nos permite ocultar los detalles de implementación de una clase y restringir el acceso a ciertos atributos y métodos. En Python, podemos lograr la encapsulación utilizando modificadores de acceso y métodos de acceso.

**Modificadores de Acceso en Python**

En Python, los modificadores de acceso son convenciones que indican el nivel de visibilidad de los atributos y métodos de una clase. Hay tres tipos principales de modificadores de acceso:

- **Público (`public`)**: Los atributos y métodos públicos son accesibles desde cualquier parte del programa. En Python, todos los atributos y métodos son públicos por defecto, a menos que se indique lo contrario.
- **Protegido (`protected`)**: Los atributos y métodos protegidos son accesibles solo desde la misma clase y sus subclases. En Python, se indica un atributo o método protegido precediendo su nombre con un guion bajo y una letra minúscula (`_atributo`, `_metodo()`).
- **Privado (`private`)**: Los atributos y métodos privados son accesibles solo desde la misma clase. En Python, se indica un atributo o método privado precediendo su nombre con dos guiones bajos (`__atributo`, `__metodo()`).

**Ejemplo de Encapsulación en Python**

```python
class Animal:
    def __init__(self, especie, edad):
        self.__especie = especie
        self.__edad = edad

    def get_especie(self):
        return self.__especie
   
    def set_especie(self, especie):
        self.__especie = especie

    def __str__(self) -> str:
        return f"Animal[Especie: {self.__especie}, Edad: {self.__edad}]"
```

En este ejemplo, los atributos `__especie` y `__edad` son privados, lo que significa que solo pueden ser accedidos dentro de la misma clase. Se proporcionan métodos `get_especie()` y `set_especie()` para permitir el acceso controlado al atributo `__especie`.

**Acceso a Atributos Encapsulados**

```python
animal1 = Animal("Fido", "1 Año")
print(animal1.get_especie())  # Salida: Fido
```

Aquí, `get_especie()` es utilizado para obtener el valor del atributo `__especie`. El acceso directo al atributo `__especie` desde fuera de la clase resultaría en un error debido a su encapsulación privada.

**Beneficios de la Encapsulación**

- **Seguridad**: Ocultar los detalles de implementación ayuda a prevenir modificaciones no deseadas y errores.
- **Control de Acceso**: Los métodos de acceso permiten controlar cómo se accede y modifica el estado de un objeto.
- **Modularidad**: Permite cambios en la implementación interna de una clase sin afectar el código externo que utiliza la clase.

---
## Proyecto de sección: Registro de mascotas

**Objetivo:**
Desarrollar un sistema de gestión de mascotas básico en Python que permita a los usuarios agregar mascotas, mostrar la lista de mascotas, editar y eliminar.



**`mascotas.py`**
```python
class Animal:
    """Clase para representar un animal."""
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"


class Mascota(Animal):
    """Clase para representar una mascota, hereda de la clase Animal."""
    def __init__(self, nombre, especie, edad) -> None:
        super().__init__(especie, edad)
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Mascota: [Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"


class RegistroMascotas:
    """Clase para representar un registro de mascotas."""
    def __init__(self) -> None:
        self.mascotas = []

    def agregar_mascotas(self, mascota):
        """
        Agrega una mascota al registro.

        Parameters:
            mascota (Mascota): La mascota a agregar al registro.
        """
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        """
        Lista todas las mascotas registradas.
        """
        if self.mascotas:
            print("  Lista de mascotas \n", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas.")

    def editar_mascota(self, indice, nuevo_mascota):
        """
        Edita una mascota en el registro.

        Parameters:
            indice (int): El índice de la mascota a editar.
            nuevo_mascota (Mascota): La nueva información de la mascota.
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            self.mascotas[indice] = nuevo_mascota
            print("Mascota editada correctamente.")

    def eliminar_mascota(self, indice):
        """
        Elimina una mascota del registro.

        Parameters:
            indice (int): El índice de la mascota a eliminar.
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente.")

```


**`main.py`**
```python
from mascotas import Mascota, RegistroMascotas

registro = RegistroMascotas()



while True:
   menu = """--- Menú ---
1. Agregar mascota
2. Listar mascotas
3. Editar mascota
4. Eliminar mascota
5. Salir
Ingrese una opción: """

   opcion = input(menu)
   if opcion == "1":
      nombre = input("Nombre de la mascota: ")
      especie = input("Especie de la mascota: ")
      edad = input("Edad de la mascota: ")

      mascota = Mascota(nombre, especie, edad)
      registro.agregar_mascotas(mascota)

   elif opcion == "2":
      registro.listar_mascotas()
   
   elif opcion == "3":
      indice = int(input("Ingrese indice del registro: "))
      nombre = input("Nombre de la mascota: ")
      especie = input("Especie de la mascota: ")
      edad = input("Edad de la mascota: ")

      nueva_mascota = Mascota(nombre, especie, edad)
      registro.editar_mascota(indice-1, nueva_mascota)
   
   elif opcion == "4":
      indice = int(input("Ingrese el índice de la mascota a eliminar: "))
      registro.eliminar_mascota(indice - 1)

   elif opcion == "5":
      print("¡Hasta luego!")
      break
   else:
      print("Opción inválida. Por favor, elija una opción válida.")

```

---
## Resumen
