# Uso de cadenas en Python

1. [Introducción](#introducción)
2. [Aspectos básicos de las cadenas](#aspectos-básicos-de-las-cadenas)
3. [Estructura de una cadena](#estructura-de-una-cadena)
4. [Métodos de cadenas](#métodos-de-cadenas)
5. [Formato de cadena](#formato-de-cadena)
6. [Proyecto de sección](#proyecto-de-sección)
7. [Resumen](#resumen)

---
## Introducción
En esta sección, exploraremos en profundidad el manejo de cadenas en Python, un aspecto fundamental de la programación que desempeña un papel crucial en el procesamiento y manipulación de datos. Abordaremos los aspectos básicos de las cadenas, examinaremos la estructura subyacente de una cadena en Python, exploraremos diversos métodos que facilitan la manipulación de texto, y aprenderemos sobre el poderoso formato de cadena. Al final de la sección, aplicaremos los conocimientos adquiridos en un proyecto práctico que consolidará nuestra comprensión y habilidades en el uso efectivo de cadenas en Python. ¡Comencemos nuestro viaje hacia el dominio de las herramientas esenciales para trabajar con texto en este versátil lenguaje de programación!

---
## Aspectos básicos de las cadenas

### Declaración de cadenas:
En Python, puedes declarar cadenas utilizando comillas simples (`'`) o comillas dobles (`"`). También es posible utilizar triples comillas simples (`'''`) o triples comillas dobles (`"""`) para cadenas multilinea.

Ejemplos:

```python
simple_string = 'Hola, mundo!'
double_string = "¡Python es genial!"

# Cadenas grandes
single_multiline_string = '''Párrafo de texto'''

double_multiline_string = """Párrafo de texto"""
```

### Operaciones básicas con cadenas:

Las operaciones básicas con cadenas incluyen la concatenación y la repetición.

**Concatenación:**

```python
string1 = 'Hola, '
string2 = 'mundo!'
new_string = string1 + string2
print(new_string)  # Resultado: Hola, mundo!
```

**Repetición:**

```python
repeated_string = 'Hola' * 3
print(repeated_string)  # Resultado: HolaHolaHola
```

### Acerca del uso de comillas:

Puedes utilizar tanto comillas simples como comillas dobles para declarar cadenas. Esto puede ser útil cuando necesitas incluir comillas dentro de la cadena:

```python
text = '¡"Python" es genial!'
text = "La luna en ingles es Moon's."

message = """¡"Python" es genial! y La luna en ingles es Moon's."""

print(message)

```

### Texto multilínea:

Hay diferentes maneras de definir varias líneas de texto como una sola variable. Las más comunes son las siguientes:

- Usar un carácter de nueva línea (\n).
- Usar comillas triples (""").


```python

message = "¡Hola mundo! \n¡Python es genial!"
multiline_text = '''¡Hola mundo!
¡Python es genial!'''
```


Estos son aspectos básicos que te permitirán trabajar eficientemente con cadenas en Python. Recuerda que Python ofrece una variedad de métodos y funciones para el manejo avanzado de cadenas que puedes explorar según tus necesidades.

---
## Estructura de una cadena
La estructura de una cadena en Python es una secuencia ordenada de caracteres. Cada carácter en la cadena tiene un índice asociado, comenzando desde 0. Puedes acceder a un carácter específico utilizando su índice.

**Estructura básica de una cadena:**

```python
text = "Python"
```

En esta cadena, cada carácter tiene un índice asociado:

```
Índices:  0  1  2  3  4  5 
Cadena:   P  y  t  h  o  n
```

La longitud de una cadena (número total de caracteres) se puede obtener con la función len():

```python
length = len(text) # 6
```

### Índices y Segmentación:

- **Índices:** Los caracteres en una cadena están indexados, comenzando desde 0 para el primer carácter. Puedes acceder a un carácter específico utilizando su índice.

  ```python
  text = "Python"
  first_character = text[0]  # Obtiene el primer carácter ("P")
  first_character = text[2]  # Obtiene el tercer carácter ("t")
  ```

- **Segmentación (Slicing):** Puedes obtener subcadenas (segmentos) de una cadena utilizando la segmentación. El formato general es `cadena[inicio:fin]`, donde `inicio` es inclusivo y `fin` es exclusivo.

  ```python
  text = "Python"
  substring = text[1:4]  # Obtiene los caracteres desde el índice 1 hasta el índice 3 ("yth")
  ```

### Stride

### Inmutabilidad:

La inmutabilidad de las cadenas significa que no puedes cambiar directamente un carácter en una posición específica de la cadena después de que se ha creado. Sin embargo, puedes crear nuevas cadenas basadas en la cadena original.

```python
text = "Python"
# Esto generará un error, ya que las cadenas son inmutables
# cadena[0] = "J"

# Pero puedes crear una nueva cadena con modificaciones
new_string = "S" + text[1:]
print(new_string)  # Resultado: "Sython"
```

### Ejemplo con Segmentación:

```python
text = "Python es un lenguaje de programación poderoso"
# Obtener las primeras 6 letras
first_letters = text[:6]  # "Python"

# Obtener las palabras "es un"
word_segment = text[7:13]  # "es un"

# Obtener las últimas 10 letras
last_letters = text[-10:]  # "poderoso"
```

En este ejemplo, se utilizan índices y segmentación para obtener diferentes partes de la cadena original. Es importante recordar que los índices negativos se cuentan desde el final de la cadena.

---
## Métodos de cadenas
Los métodos de cadenas en Python son funciones incorporadas que actúan sobre objetos de tipo cadena (str). Estos métodos permiten realizar diversas operaciones y manipulaciones en las cadenas. Aquí te explico algunos de los métodos más comunes y su funcionamiento:

### ¿Qué son los métodos y cómo funcionan?

En Python, los métodos son funciones que están asociadas a un objeto particular y son invocadas sobre ese objeto. Los métodos de cadena son específicos para las cadenas y se aplican a un objeto de tipo cadena. Se invocan usando la notación de punto (`cadena.metodo()`).

Por ejemplo:

```python
text = "hola, mundo"
capital_letters = text.Title()  # El método title() convierte la cadena a título
print(capital_letters)  # Resultado: Hola, Mundo
```

### Métodos más usados:

1. **`upper()` y `lower()`:** Convierten la cadena a mayúsculas o minúsculas, respectivamente.

    ```python
    text = "Hola, mundo!"
    uppercase = text.upper()
    lowercase = text.lower()
    ```

2. **`capitalize()`:** Convierte la primera letra de la cadena a mayúscula.

    ```python
    text = "hola, mundo!"
    capitalize = text.capitalize()
    ```

3. **`count(subcadena)`:** Cuenta cuántas veces aparece la subcadena en la cadena.

    ```python
    text = "Hola, hola, hola, mundo!"
    count = text.count("hola")
    ```

4. **`find(subcadena)` y `index(subcadena)`:** Encuentran la posición de la primera aparición de la subcadena. La diferencia principal es que `find()` devuelve -1 si no encuentra la subcadena, mientras que `index()` lanza una excepción ValueError.

    ```python
    text = "Hola, mundo!"
    position = text.find("mundo")
    ```

5. **`replace(old, new)`:** Reemplaza todas las ocurrencias de una subcadena con otra.

    ```python
    text = "Hola, mundo!"
    new_string = text.replace("mundo", "Python")
    ```

6. **`split(separador)`:** Divide la cadena en una lista de subcadenas utilizando el separador proporcionado.

    ```python
    text = "Hola, mundo!"
    list_words = text.split(",")  # Resultado: ['Hola', ' mundo!']
    ```

7. **`join(iterable)`:** Une las cadenas de un iterable con la cadena llamadora como separador.

    ```python
    words = ["Hola", "mundo", "Python"]
    united_string = " ".join(words)  # Resultado: 'Hola mundo Python'
    ```

### Uso del operador de pertenencia (`in`):

El operador de pertenencia (`in`) se utiliza para verificar si una subcadena está presente dentro de otra cadena. Este operador devuelve `True` si la subcadena está presente y `False` en caso contrario.

Ejemplo del uso del operador de pertenencia:

```python
text = "Hola, mundo!"

# Verifica si "mundo" está presente en la cadena
presente = "mundo" in text  # Resultado: True
```

Este operador es útil cuando necesitas verificar la existencia de ciertos caracteres o subcadenas dentro de una cadena más grande.

---
## Formato de cadena
### Formato de signo de porcentaje (`%`):

El formato de signo de porcentaje utiliza marcadores específicos para diferentes tipos de datos. Aquí hay una lista de marcadores comunes:

- `%s`: Cadena de caracteres.
- `%d`: Número entero.
- `%f`: Número de punto flotante.
- `%x`: Número entero en formato hexadecimal.
- `%o`: Número entero en formato octal.
- `%c`: Carácter.

Ejemplo:

```python
name = "Juan"
age = 25
size = 1.75

message = "Hola, me llamo %s, tengo %d años y mido %.2f metros." % (name, age, size)
print(message)
```

### El método `format()`:

El método `format()` utiliza llaves `{}` como marcadores de posición y es más flexible que el formato de signo de porcentaje. Puedes especificar el orden de los valores o incluso usar nombres para los marcadores de posición.

Ejemplo:

```python
name = "Juan"
age = 25
size = 1.75

message = "Hola, me llamo {}, tengo {} años y mido {:.2f} metros.".format(name, age, size)
print(message)
```

### Acerca de las cadenas f-strings:

Las f-strings son cadenas literales que permiten la interpolación de variables directamente dentro de la cadena. Utilizan la sintaxis `f"..."` y son introducidas a partir de Python 3.6.

Ejemplo:

```python
name = "Juan"
age = 25
size = 1.75

message = f"Hola, me llamo {name}, tengo {age} años y mido {size:.2f} metros."
print(message)
```

En resumen, cada enfoque de formato de cadena tiene sus propias características y ventajas. Los f-strings son más concisos y legibles, el método `format()` es más versátil, y el formato de signo de porcentaje es menos recomendado en Python moderno pero sigue siendo válido.

---
## Proyecto de sección 
**Ejercicio: Verificación de Palíndromos**
El ejercicio consiste en desarrollar un programa para verificar si una palabra ingresada es un palíndromo. Aquí están los pasos resumidos:

- Usar `input` para obtener la palabra del usuario.
- Convertir la palabra a minúsculas
- Eliminar espacios en blanco
- Invertir la palabra con `[::-1]`
- Usar `if-else` para imprimir si la palabra es un palíndromo o no.

**Código del proyecto**
```Python
# Solicitar al usuario que ingrese una palabra
word = input("Ingrese una palabra: ")

# convertirla a minúsculas)
word = word.lower()

#eliminar espacios
word = word.replace(" ", "")

# Invertir palabra
inverted_word = word[::-1]

# Mostrar el resultado al usuario
if word == inverted_word:
    print(f"{word} es un palíndromo.")
else:
    print(f"{word} no es un palíndromo.")

```
***Optimizando el código**

```Python
# Solicita al usuario que ingrese una palabra
word = input("Ingrese una palabra: ")

# Convierte la palabra a minúsculas y elimina espacios en blanco
word = word.lower().replace(" ", "")

# Muestra el resultado
print("Es un palíndromo." if word == word[::-1] else "No es un palíndromo.")
```

Lo que ves en Python como `if word == word[::-1] else` es una expresión condicional o operador ternario. Es una forma compacta de escribir una estructura de control `if-else` en una sola línea.

---
## Resumen
En esta sección, exploramos en detalle el manejo de cadenas en Python, destacando los aspectos básicos de las cadenas, analizando la estructura fundamental de una cadena en Python, examinando los métodos clave para la manipulación eficiente del texto, y aprendiendo sobre el formato de cadena. Al finalizar la sección, aplicamos los conocimientos adquiridos en un proyecto práctico que consolidó nuestra comprensión y habilidades en el uso efectivo de cadenas en Python. Este viaje nos permitió adquirir destrezas esenciales para trabajar con texto en este versátil lenguaje de programación.