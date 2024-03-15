# Variables y datos

1. [Introducción](#introducción)
2. [Variables](#variables)
3. [Tipos de datos](#tipos-de-datos)
4. [Entrada de datos](#entrada-de-datos)
5. [Conversión de tipos](#conversión-de-tipos)
6. [Proyecto de sección](#proyectos-de-sección)
8. [Resumen](#resumen)

---
## Introducción

¡Bienvenidos a la sección de Variables y Datos en nuestro curso de Python! En esta emocionante etapa del aprendizaje, exploraremos conceptos fundamentales que son la base de la programación en Python. Comenzaremos por entender qué son las variables y cómo se utilizan para almacenar información en nuestros programas. Luego, nos sumergiremos en los diferentes tipos de datos que Python ofrece, lo que nos permitirá trabajar con números, texto, y más de manera efectiva.

A lo largo de esta sección, también exploraremos cómo funcionan los operadores y expresiones en Python, lo que nos ayudará a realizar cálculos y manipulaciones de datos. Aprenderemos cómo mostrar información en pantalla y cómo obtener datos del usuario a través de la entrada de datos, lo que es esencial para la interacción con nuestros programas.

La conversión de tipos es otro tema fundamental que abordaremos, ya que nos permitirá cambiar el tipo de dato de una variable según nuestras necesidades. Finalmente, para poner en práctica todo lo que aprendamos, trabajaremos en un emocionante proyecto de sección que consolidará nuestros conocimientos y nos dará la oportunidad de aplicar lo aprendido en situaciones del mundo real.

Así que prepárense para sumergirse en el fascinante mundo de las variables y datos en Python. ¡Estamos emocionados de acompañarlos en este viaje de aprendizaje!

---
## Variables
En programación, una variable es un espacio de memoria reservado para almacenar datos, como números, cadenas de texto, objetos u otro tipo de información. Las variables permiten que los programas almacenen y manipulen datos de manera dinámica en tiempo de ejecución.

En Python, las variables son identificadores que se utilizan para almacenar y acceder a datos. Cada variable tiene un nombre único que se utiliza para referirse a ella en el código. Aquí tienes cómo se ve una variable en Python y algunas reglas de nomenclatura:

```python
nombre_variable = valor
```

- `nombre_variable`: Es el nombre que eliges para tu variable. Debe seguir ciertas reglas de nomenclatura.
- `=`: Es el operador de asignación que se utiliza para asignar un valor a la variable.
- `valor`: Es el dato que deseas almacenar en la variable.

**Ejemplos de definición de variables**
Definción y inicialización de variable:
```python
mensaje = "Hola Mundo"
print(mensaje)
```
El valor asignado a una variable puede cambiar a lo largo del programa.
```python
mensaje = "Adios Mundo"
print(mensaje)
```

**Sintaxis de las variables en Python**

1. Los nombres de las variables deben comenzar con una letra (a-z, A-Z) o un guión bajo (_).
2. Después del primer carácter, los nombres de las variables pueden contener letras, números y guiones bajos.
  ```python
  _mensaje = "Hola mundo"
  print(_mensaje)
  ```
  ```python
  menSaje = "Hola mundo"
  print(menSaje)
  ```
  ```python
  mensaje_2 = "Hola Python"
  print(mensaje_2)
  ``` 
  Si no cumple con estas reglas definidas en la sintaxis de Python, el interprete lanza un error a la hora de ejecutar.

  ```python
  mensaje& = "Hola Python"
  print(mensaje_2)
  ``` 
  ```python
    File "<stdin>", line 1
    mensaje& = "Hola Python"
             ^
    SyntaxError: invalid syntax
  ``` 

  ```python
  2mensaje = "Hola Python"
  print(mensaje_2)
  ``` 
  ```python
    File "<stdin>", line 1
    2mensaje = "Hola Python"
    ^
    SyntaxError: invalid decimal literal
  ```
3. Los nombres de las variables distinguen entre mayúsculas y minúsculas. Esto significa que `mi_variable` y `Mi_Variable` son considerados nombres diferentes.
  ```python
  Mensaje3 = "Hola Python"
  print(mensaje3)
  ``` 
  ```python
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  NameError: name 'mensaje3' is not defined. Did you mean: 'Mensaje3'?
  ```
4. No se pueden utilizar palabras clave reservadas de Python como nombres de variables. Ejemplos de palabras clave son `if`, `else`, `while`, `for`, `def`, etc.
5. Es buena práctica utilizar nombres descriptivos para tus variables para que el código sea más legible.

Recuerda que la elección de nombres de variables debe ser significativa y seguir convenciones de estilo para hacer tu código más legible y mantenible. Por ejemplo, PEP 8 es la guía de estilo de código recomendada para Python y ofrece pautas sobre cómo nombrar variables y otras convenciones de codificación.

---
## Tipos de datos
A continuación, se presenta una tabla con algunos tipos de datos en Python, cómo identificar su tipo y ejemplos de cada uno:

| Tipo de Dato | Descripción                                          | Ejemplo               | Cómo Saber el Tipo  |
|--------------|------------------------------------------------------|-----------------------|----------------------|
| `int`        | Números enteros sin decimales                        | `edad = 25`           | `type(edad)`         |
| `float`      | Números con decimales                                | `altura = 1.75`       | `type(altura)`       |
| `str`        | Cadenas de texto                                     | `nombre = "Juan"`     | `type(nombre)`       |
| `bool`       | Valores de verdad o falsedad (booleanos)             | `es_mayor = True`     | `type(es_mayor)`     |
| `list`       | Listas: colecciones ordenadas de elementos           | `numeros = [1, 2, 3]`  | `type(numeros)`      |
| `tuple`      | Tuplas: colecciones inmutables de elementos          | `coordenadas = (3, 7)`| `type(coordenadas)`  |
| `dict`       | Diccionarios: pares clave-valor                      | `persona = {'nombre': 'Ana', 'edad': 30}`| `type(persona)`  |
| `set`        | Conjuntos: colecciones no ordenadas de elementos únicos | `colores = {'rojo', 'verde', 'azul'}` | `type(colores)` |

Para saber el tipo de dato de una variable, puedes utilizar la función `type()`. Por ejemplo:

```python
dato = 42
print(type(dato))  # Salida: <class 'int'>
```

A continuación, algunos ejemplos adicionales:

- Listas de diferentes tipos de datos:

  ```python
  mix_lista = [1, "dos", 3.0, True]
  ```

- Operaciones con tipos de datos:

  ```python
  a = 5
  b = 2.0
  resultado = a + b  # El resultado será un float
  ```

Estos ejemplos ilustran cómo Python es dinámicamente tipado, lo que significa que el tipo de una variable puede cambiar durante la ejecución del programa. Sin embargo, es importante comprender y gestionar los tipos de datos para evitar errores y mejorar la legibilidad del código.

---
## Entrada de datos

1. **Función `input()`**: La función `input()` permite al usuario introducir datos desde la consola. Ten en cuenta que los datos introducidos se almacenan como cadenas.

```python
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola,", nombre)
```


2. **Pasando argumentos al script**:

   Puedes pasar argumentos directamente al script cuando lo ejecutas desde la línea de comandos:

  ```python
   # script.py
   import sys

   
    nombre = sys.argv[1]
    print("Hola, " + nombre + "!")
   ```

   Puedes ejecutar el script así:

   ```bash
   python script.py Juan
   ```

   Y obtendrás la salida: "Hola, Juan!".

---
## Conversión de tipos
En Python, la conversión de tipos se refiere a la capacidad de cambiar el tipo de datos de una variable de un tipo a otro. Python ofrece varias funciones para realizar conversiones de tipos. Aquí hay algunas de las conversiones de tipos más comunes:

1. Conversión de entero a cadena y viceversa:
   - Para convertir un entero a una cadena, puedes usar la función `str()`. Por ejemplo:
     ```python
     numero = 42
     cadena = str(numero)
     ```

   - Para convertir una cadena a un entero, puedes usar la función `int()`. Ten en cuenta que esto puede generar una excepción `ValueError` si la cadena no es un número válido.
     ```python
     cadena = "42"
     numero = int(cadena)
     ```

2. Conversión de flotante a cadena y viceversa:
   - Para convertir un flotante a una cadena, puedes usar la función `str()`. Por ejemplo:
     ```python
     numero = 3.14159
     cadena = str(numero)
     ```

   - Para convertir una cadena a un flotante, puedes usar la función `float()`. Al igual que con `int()`, esto puede generar una excepción `ValueError` si la cadena no es un número válido.
     ```python
     cadena = "3.14159"
     numero = float(cadena)
     ```

3. Conversión de cadena a lista y viceversa:
   - Para convertir una cadena en una lista de caracteres, puedes usar la función `list()`. Esto creará una lista donde cada carácter de la cadena se convierte en un elemento de la lista.
     ```python
     cadena = "Hola"
     lista = list(cadena)
     ```

   - Para convertir una lista de caracteres en una cadena, puedes usar el método `join()`. Por ejemplo:
     ```python
     lista = ['H', 'o', 'l', 'a']
     cadena = ''.join(lista)
     ```

4. Conversión de otros tipos:
   - Puedes usar las funciones de conversión correspondientes, como `bool()`, `str()`, `int()`, `float()`, etc., para convertir entre otros tipos de datos, como booleanos, listas, tuplas, diccionarios, conjuntos, etc.

Recuerda que las conversiones de tipos deben realizarse con precaución y teniendo en cuenta posibles excepciones, especialmente cuando se convierten datos que pueden no ser compatibles.

---
## Proyectos de sección 

### Calcular el Precio de Venta

**Enunciado:**
Dado el valor de venta de un producto, se debe calcular el Impuesto General a las Ventas (IGV) que es del 18%, y a partir de eso, determinar el precio de venta final.

**Mejora:**
En esta práctica, vamos a crear un programa en Python que permita al usuario ingresar el valor de venta del producto. Luego, el sistema realizará los cálculos necesarios para hallar el IGV y el precio de venta final. Esta mejora incluirá un código Python que automatiza todo el proceso.

**Solución en Python:**
```python
# Solicitar al usuario ingresar el valor de venta
valor_venta = float(input("Ingrese el valor de venta del producto: "))

# Calcular el IGV (18% del valor de venta)
igv = valor_venta * 0.18

# Calcular el precio de venta final
precio_venta = valor_venta + igv

# Mostrar los resultados
print(f"El IGV es: {igv:.2f}")
print(f"El precio de venta final es: {precio_venta:.2f}")
```
El formato `:.2f` es una especificación de formato utilizada en Python para formatear números de punto flotante (números decimales). Vamos a desglosar cada parte:

- `:`: Este es el delimitador que indica que se va a especificar un formato.

- `.2`: El número después del punto (`.`) indica la cantidad de dígitos que se mostrarán después del punto decimal. En este caso, `.2` significa que se mostrarán exactamente 2 dígitos después del punto.

- `f`: Indica que el tipo de dato que se formateará es un número de punto flotante (float).

Entonces, cuando utilizas `:.2f` en una cadena de formato, estás diciendo que deseas formatear un número de punto flotante y que se deben mostrar exactamente dos dígitos después del punto decimal.


Con este código, el programa solicita al usuario ingresar el valor de venta del producto, luego calcula el IGV como el 18% del valor de venta y finalmente calcula el precio de venta final sumando el valor de venta y el IGV. Los resultados se muestran con dos decimales para mayor claridad.

Espero que esta mejora y solución en Python sean útiles para tu práctica.

---
## Resumen
En la sección anterior de nuestro curso de Python, exploramos conceptos esenciales relacionados con variables y datos. Comenzamos por comprender qué eran las variables y cómo se utilizaban para almacenar información en nuestros programas. Además, exploramos los diversos tipos de datos disponibles en Python, lo que nos permitió trabajar con números, texto y otros tipos de información.

Durante esa etapa, también profundizamos en cómo funcionaban los operadores y expresiones en Python, lo que nos permitió realizar cálculos y manipular datos de manera efectiva. Aprendimos a mostrar información en pantalla y a obtener datos del usuario a través de la entrada de datos, habilidades esenciales para la interacción con nuestros programas.

La conversión de tipos fue otro tema importante que abordamos, ya que nos permitió cambiar el tipo de dato de una variable según nuestras necesidades. Finalmente, concluimos esa sección con un emocionante proyecto que nos dio la oportunidad de aplicar nuestros conocimientos en situaciones del mundo real.

En resumen, la sección pasada fue un paso fundamental en nuestro viaje de aprendizaje en Python, proporcionándonos las bases necesarias para desarrollar habilidades más avanzadas en el futuro.