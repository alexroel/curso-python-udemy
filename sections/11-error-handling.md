# Control de errores de Python

1. [Introdución](#introdución)
2. [Tipos de errores](#tipos-de-errores)
3. [Control de Excepciones](#control-de-excepciones)
4. [Generación de excepciones](#generación-de-excepciones)
5. [Manejo de archivos](#manejo-de-archivos)
6. [Resumen](#resumen)

---
## Introdución
En la sección dedicada al Control de Errores en Python, exploraremos diversos aspectos fundamentales para gestionar situaciones imprevistas y mejorar la robustez de nuestros programas. Estos aspectos incluyen:

**Tipos de Errores:**
Antes de abordar el manejo de errores, es esencial comprender los diferentes tipos de errores que pueden surgir en un programa. Python clasifica los errores en varias categorías, desde errores de sintaxis hasta errores de tiempo de ejecución.

**Control de Excepciones:**
Python utiliza bloques `try` y `except` para gestionar excepciones de manera eficiente. Aprenderemos a utilizar esta estructura para capturar y manejar errores, permitiendo que el programa continúe ejecutándose incluso cuando se enfrenta a condiciones excepcionales.

**Generación de Excepciones:**
En algunos casos, es necesario generar excepciones de forma deliberada para señalar condiciones de error específicas. Exploraremos cómo crear y lanzar excepciones personalizadas, proporcionando mensajes significativos para facilitar la identificación y resolución de problemas en el código.

**Manejo de Archivos:**
El manejo de archivos es una tarea común en la programación. Aprenderemos a abrir archivos, leer su contenido y escribir en ellos utilizando las funciones y métodos integrados de Python. Además, exploraremos las mejores prácticas para garantizar la correcta gestión de recursos al trabajar con archivos.

Al abordar estos aspectos, fortaleceremos nuestras habilidades en el control de errores, mejorando la calidad y la confiabilidad de nuestros programas. ¡Sumergámonos en el fascinante mundo del control de errores en Python!

---
## Tipos de errores
Python es un lenguaje de programación muy poderoso y versátil, pero como cualquier otro lenguaje, los errores son una parte inevitable del proceso de desarrollo. Los errores en Python se pueden clasificar en dos categorías principales: errores de sintaxis y excepciones. En esta guía, exploraremos ambos tipos de errores y proporcionaremos ejemplos para ayudarte a entenderlos mejor.

**Errores de Sintaxis**

Los errores de sintaxis ocurren cuando el intérprete de Python no puede entender tu código debido a una violación de las reglas del lenguaje. Estos errores suelen ser detectados durante la etapa de análisis del código antes de que se ejecute. Aquí hay un ejemplo de un error de sintaxis común:

```python
print("Hola Mundo)
  File "<stdin>", line 1
    print("Hola Mundo)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

En este caso, el error ocurre porque falta una comilla de cierre en la cadena `"Hola Mundo"`. Python detecta este error durante la fase de análisis y muestra un mensaje de error indicando la ubicación del problema y el tipo de error (`SyntaxError` en este caso).


**Excepciones**

Las excepciones son errores que ocurren durante la ejecución de un programa. Estos errores pueden ser manejados y, en algunos casos, pueden permitir que el programa continúe ejecutándose incluso después de un problema. Aquí hay algunos ejemplos de excepciones comunes en Python:

1. **NameError**

```python
>>> print(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'var' is not defined. Did you mean: 'vars'?
```

Este error ocurre cuando intentas usar una variable que no ha sido definida previamente. En este caso, Python no puede encontrar la variable `var` y muestra un `NameError`.

2. **ZeroDivisionError**

```python
>>> 50/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Este error ocurre cuando intentas dividir un número por cero, lo cual es una operación indefinida en matemáticas. Python muestra un `ZeroDivisionError` para indicar que la operación no se puede realizar.

3. **TypeError**

```python
>>> "4" + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Este error ocurre cuando intentas realizar una operación entre dos tipos de datos incompatibles. En este caso, estás intentando concatenar una cadena (`"4"`) con un entero (`4`), lo cual no es válido en Python, y se genera un `TypeError`.

---
## Control de Excepciones
El control de excepciones en Python es una técnica fundamental para escribir programas robustos y que manejen adecuadamente situaciones inesperadas. En esta guía, aprenderás a utilizar los bloques `try-except` para manejar excepciones, manejar múltiples excepciones, emplear la cláusula `else` y la cláusula `as` en conjunto con `except`.

**Bloque Try-Except**

El bloque `try-except` es una estructura que te permite manejar excepciones de manera controlada. Aquí tienes un ejemplo básico:

```python
try:
    # Código que puede lanzar una excepción
    a = int(input('Ingrese un número entero: '))
    b = int(input('Ingrese un número entero diferente de cero: '))
    resultado = a / b

    print(f"División entre {a}/{b} = {resultado}")
except Exception as e:
    # Manejo de la excepción
    print(f"Ocurrió un error: {e}")
```

En este ejemplo, el código dentro del bloque `try` es susceptible de lanzar una excepción. Si se produce una excepción, el programa salta al bloque `except`, donde puedes manejar el error de manera adecuada. La cláusula `as` te permite asignar la excepción a una variable para su posterior uso.


**Múltiples Excepciones**

Puedes manejar diferentes tipos de excepciones de manera individual utilizando múltiples bloques `except`. Por ejemplo:

```python
try:
    # Código que puede lanzar una excepción
    a = int(input('Ingrese un número entero: '))
    b = int(input('Ingrese un número entero diferente de cero: '))
    resultado = a / b
    print(f"División entre {a}/{b} = {resultado}")
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")
except ValueError:
    print("¡Error! Debes ingresar números enteros.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

En este caso, se manejan tres tipos diferentes de excepciones: `ZeroDivisionError`, `ValueError` y cualquier otra excepción no especificada.

**Uso de Else**

La cláusula `else` en un bloque `try-except` se ejecuta si no se produce ninguna excepción. Puedes usarla para ejecutar código que depende del éxito del bloque `try`. Por ejemplo:

```python
try:
    # Código que puede lanzar una excepción
    a = int(input('Ingrese un número entero: '))
    b = int(input('Ingrese un número entero diferente de cero: '))
    resultado = a / b
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")
except ValueError:
    print("¡Error! Debes ingresar números enteros.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
else:
    print(f"División entre {a}/{b} = {resultado}")
```

En este caso, el bloque `else` se ejecuta solo si no se lanzó ninguna excepción dentro del bloque `try`.

---
## Generación de excepciones
En Python, la generación de excepciones es una técnica fundamental que te permite indicar que ha ocurrido un error o una situación excepcional dentro de tu código. Esto facilita el manejo adecuado de casos inesperados y mejora la robustez de tus programas. En esta guía, aprenderás cómo generar excepciones personalizadas utilizando el ejemplo proporcionado.

**Generación de Excepciones Personalizadas**

En Python, puedes generar excepciones personalizadas utilizando la palabra clave `raise`. Esto te permite lanzar una excepción en cualquier punto de tu código cuando detectas una situación que requiere atención especial. Aquí tienes un ejemplo:

```python
def colores(color):
    lista_colores = ["azul", "verde", "rojo"]

    if color not in lista_colores:
        raise Exception(f"El color {color} no se encuentra en la lista de colores permitidos.")

colores("amarillo")
```

En este ejemplo, la función `colores` verifica si el color pasado como argumento está presente en una lista de colores permitidos. Si el color no está en la lista, se genera una excepción utilizando `raise`. La excepción generada es de tipo `Exception`, pero puedes crear excepciones personalizadas creando tus propias clases de excepción.


**Clases de Excepción Personalizadas**

Puedes crear tus propias clases de excepción para representar situaciones específicas en tu código. Esto te permite capturar y manejar esos casos de manera más precisa. Aquí tienes un ejemplo de cómo crear una clase de excepción personalizada:

```python
class ColorNoValidoError(Exception):
    def __init__(self, color):
        super().__init__(f"El color {color} no se encuentra en la lista de colores permitidos.")

def colores(color):
    lista_colores = ["azul", "verde", "rojo"]

    if color not in lista_colores:
        raise ColorNoValidoError(color)

colores("amarillo")
```

En este ejemplo, hemos creado la clase `ColorNoValidoError`, que hereda de la clase base `Exception`. Esta clase tiene un método `__init__` que inicializa la excepción con un mensaje personalizado. Luego, en la función `colores`, lanzamos esta excepción personalizada si el color no está en la lista de colores permitidos.


**Manejo de Excepciones Generadas**

Cuando generas una excepción, es importante manejarla adecuadamente para que tu programa no se detenga abruptamente. Puedes hacerlo utilizando bloques `try-except` para capturar y manejar las excepciones generadas. Aquí tienes un ejemplo de cómo hacerlo:

```python
try:
    colores("amarillo")
except ColorNoValidoError as error:
    print(f"Se ha generado una excepción: {error}")
```

En este bloque `try-except`, intentamos llamar a la función `colores` con el color "amarillo". Si se genera la excepción `ColorNoValidoError`, la capturamos en el bloque `except` y mostramos un mensaje adecuado.

---
## Manejo de archivos
El manejo de archivos en Python es una tarea común en la programación, ya sea para leer datos de archivos existentes, escribir datos en archivos o crear nuevos archivos. En esta guía, exploraremos cómo abrir, leer, escribir y cerrar archivos en Python, además de discutir buenas prácticas como el uso de bloques `try-except` y `with`.

**Abrir y Leer un Archivo**

Para abrir y leer un archivo en Python, puedes usar la función `open()` con el modo de apertura `"r"` (lectura). Aquí tienes un ejemplo:

```python
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
finally:
    if archivo:
        archivo.close()
```

En este ejemplo, intentamos abrir el archivo `"archivo.txt"` en modo lectura. Si el archivo existe, leemos su contenido y lo imprimimos en la consola. Si el archivo no se encuentra, se maneja la excepción `FileNotFoundError`.

**Crear un Archivo si no Existe**

Puedes verificar si un archivo existe y, si no existe, crearlo. Aquí tienes un ejemplo que utiliza un bloque `try-except` para manejar esto:

```python
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
    print("Creando el archivo...")
    archivo = open("archivo.txt", "w")
    archivo.write("¡Hola mundo!")
else:
    print("Contenido del archivo:")
    print(contenido)
```

En este ejemplo, utilizamos la declaración `with` para abrir el archivo en modo lectura. Si el archivo no se encuentra, se maneja la excepción `FileNotFoundError` y se crea el archivo en modo escritura `"w"` con el contenido `"¡Hola mundo!"`.


**Uso de la Declaración `with`**

La declaración `with` en Python es una forma más limpia y segura de trabajar con archivos. Te asegura que el archivo se cierre automáticamente una vez que el bloque `with` haya terminado de ejecutarse, incluso si ocurren excepciones. Aquí tienes un ejemplo:

```python
try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
    print("Creando el archivo...")
    with open("archivo.txt", "w") as archivo:
        archivo.write("¡Hola mundo!")
```

En este ejemplo, abrimos el archivo en modo lectura dentro de un bloque `with`. Si el archivo no se encuentra, se maneja la excepción `FileNotFoundError` y se crea el archivo en modo escritura `"w"` dentro de otro bloque `with`. En ambos casos, el archivo se cierra automáticamente al salir del bloque `with`, lo que simplifica el código y lo hace más seguro.

---
## Resumen
