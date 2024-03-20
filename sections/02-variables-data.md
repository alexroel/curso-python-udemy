# Variables y datos

1. [Introducción](#introducción)
2. [Variables](#variables)
3. [Números en Python](#números-en-python)
4. [Entrada de datos](#entrada-de-datos)
5. [Conversión de tipos](#conversión-de-tipos)
6. [Proyecto de sección](#proyectos-de-sección)
7. [Comentarios](#comentarios)
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
## Números en Python

Los números son una parte fundamental en la programación, y Python ofrece una amplia variedad de tipos numéricos para trabajar. Desde enteros simples hasta números complejos, Python proporciona una flexibilidad excepcional para manejar diferentes tipos de datos numéricos. En esta guía, exploraremos los distintos tipos de números en Python, cómo se definen y algunas operaciones básicas que se pueden realizar con ellos.

**¿Qué es un número en Python?**

En Python, un número es un tipo de dato que representa un valor numérico. Hay varios tipos de números en Python, incluyendo enteros, números de punto flotante y números complejos. Cada tipo de número tiene sus propias características y se puede manipular de diversas formas.

**Números enteros**

Los números enteros son aquellos que no tienen parte fraccionaria y pueden ser positivos o negativos. En Python, los números enteros se representan con el tipo de dato `int`.

```python
>>> num = 10
>>> num
10
>>> num * 2
20
>>> num2 = "20"
>>> num2
'20'
>>> num * 2
20
>>> num2 * 2
'2020'
>>>
>>> type(num)
<class 'int'>
>>> type(num2)
<class 'str'>
```

Es importante tener en cuenta que los números enteros pueden ser representados como cadenas de caracteres, pero las operaciones con ellas no se comportan como números.

**Declaración de números grandes**

Python permite la declaración de números grandes. Se pueden separar los dígitos usando guiones bajos (`_`) para mejorar la legibilidad, como se muestra a continuación:

```python
>>> n = 1000000
>>> n
1000000
>>> n = 1_000_000
>>> n
1000000
```

Esta sintaxis con guiones bajos hace que sea más fácil leer números grandes sin afectar su valor.

**Números de punto flotante**

Los números de punto flotante son aquellos que tienen una parte fraccionaria. En Python, se representan con el tipo de dato `float`.

```python
>>> num = 10.5
>>> type(num)
<class 'float'>
>>> num = 1000000.5
>>> num
1000000.5
>>> num2 = 1_000_000.5
>>> num2
1000000.5
>>> num3 = 1e6
>>> num3
1000000.0
>>> num = 2e400
>>> num
inf
>>> num = -2e400
>>> num
-inf
```

Los números de punto flotante también pueden representarse en notación científica, como `1e6`, que equivale a 1,000,000.

**Números complejos**

Los números complejos son aquellos que tienen una parte real e imaginaria. En Python, se representan con el tipo de dato `complex`.

```python
>>> num = 1 + 2j
>>> num
(1+2j)
>>> type(num)
<class 'complex'>
>>> num.real
1.0
>>> num.imag
2.0
```

En un número complejo, la parte real se refiere al componente real del número, mientras que la parte imaginaria se refiere al componente imaginario del número.

En conclusión, Python ofrece una amplia gama de tipos numéricos que pueden ser utilizados para realizar diversas operaciones matemáticas. Desde enteros simples hasta números complejos, la capacidad de manipular números es fundamental en la programación y Python proporciona las herramientas necesarias para hacerlo de manera efectiva y eficiente.

---
## Entrada de datos

1. **Función `input()`**: La función `input()` permite al usuario introducir datos desde la consola. Ten en cuenta que los datos introducidos se almacenan como cadenas.

```python
mensaje = input("Ingrese el mensaje: ")
print(mensaje)
```


2. **Pasando argumentos al script**:

   Puedes pasar argumentos directamente al script cuando lo ejecutas desde la línea de comandos:

  ```python
  # hola.py
  import sys

   
  mensaje = sys.argv[1]
  print(mensaje)
  ```

   Puedes ejecutar el script así:

   ```bash
   python hola.py "Hola Mundo"
   ```

   Y obtendrás la salida: "Hola Mundo".

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

**Ejemplo de suma de dos números**

```python
n1 = input("Ingrese primer número: ")
n2 = input("Ingrese segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2

print(f"La suma de {n1} + {n2} = {suma}")
```

---
## Comentarios

Los comentarios en Python son porciones de texto que se utilizan para explicar el código o hacer anotaciones dentro del mismo. Los comentarios no se ejecutan como parte del programa y son ignorados por el intérprete de Python. Sirven para mejorar la legibilidad del código y para documentar su funcionamiento.

**Comentarios básicos**

En Python, los comentarios básicos se crean precediendo el texto con el símbolo `#`. Todo lo que esté después del `#` en la misma línea se considera un comentario y no será ejecutado.

Ejemplo:

```python
# Este es un comentario básico en Python
numero = 10  # Esta línea asigna el valor 10 a la variable "numero"
```

En el ejemplo anterior, el comentario después del símbolo `#` explica la acción que realiza la línea de código siguiente.

**Comentarios de varias líneas**

Los comentarios de varias líneas son útiles cuando se necesita explicar un bloque más extenso de código. En Python, se pueden crear comentarios de varias líneas utilizando comillas triples (`'''` o `"""`).

Ejemplo:

```python
'''
Este es un comentario
de varias líneas en Python.
Puede abarcar múltiples líneas
y es útil para documentar
bloques extensos de código.
'''
numero = 10
```

En este caso, todo el texto entre las comillas triples es considerado un comentario y no será ejecutado por el intérprete de Python.

Los comentarios son una herramienta invaluable para mejorar la claridad y la comprensión del código, tanto para el programador que lo escribe como para otros que puedan leerlo en el futuro. Es importante usarlos de manera efectiva para explicar la lógica detrás del código y hacer que sea más fácil de entender.

---
## Proyectos de sección 

**Calcular el Precio de Venta**

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