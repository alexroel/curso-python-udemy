# Uso de listas y tuplas
1. [Introducción](#introducción)
2. [Creación de una lista](#creación-de-una-lista)
3. [Manipulación de datos de la lista](#manipulación-de-datos-de-la-lista)
4. [Trabajo con números en listas](#trabajo-con-números-en-listas)
5. [Métodos de listas](#métodos-de-listas)
6. [Creación de una tupla](#creación-de-una-tupla)
7. [Pilas y colas en python](#pilas-y-colas-en-python)
8. [Resumen](#resumen)

---
## Introducción
¡Bienvenido a la sección dedicada al "Uso de listas y tuplas"! En este fascinante recorrido por el mundo de la programación en Python, exploraremos diversas facetas relacionadas con la manipulación de datos mediante listas y tuplas. Comenzaremos desentrañando los secretos de la creación de listas, descubriendo cómo almacenar y organizar información de manera eficiente.

A lo largo de este viaje, nos sumergiremos en la magia de la manipulación de datos en listas, aprendiendo a modificar, agregar y eliminar elementos según nuestras necesidades. Además, exploraremos cómo trabajar con números dentro de listas, abordando conceptos esenciales para operaciones matemáticas y estadísticas.

No podríamos dejar de lado los métodos de listas, herramientas poderosas que potencian la capacidad de manipulación de estos versátiles contenedores. Desglosaremos estos métodos y comprenderemos cómo utilizarlos para optimizar y simplificar nuestro código.

Pero eso no es todo. En nuestra travesía, también nos adentraremos en el intrigante mundo de las tuplas. Descubriremos cómo crear estas estructuras inmutables y entenderemos las situaciones en las que su uso es más apropiado que el de las listas.

Y como colofón, exploraremos las pilas y colas en Python, dos estructuras de datos fundamentales que nos permitirán gestionar y organizar información de manera eficaz, abriendo nuevas posibilidades en la resolución de problemas algorítmicos.

Prepárate para sumergirte en este apasionante viaje de aprendizaje. ¡Comencemos a explorar las maravillas del "Uso de listas y tuplas" en Python!

---
## Creación de una lista

Una lista es una estructura de datos fundamental en Python que te permite almacenar y organizar información. En este artículo, exploraremos los aspectos esenciales al trabajar con listas, cubriendo su estructura, el acceso a elementos mediante índices, la determinación de su longitud, la adición y eliminación de elementos, el uso de índices negativos y la búsqueda de un valor dentro de una lista. A lo largo de esta guía, utilizaremos nombres de variables en inglés y trabajaremos con un ejemplo de lista de colores.

### 1. Estructura de una Lista

Una lista en Python se define utilizando corchetes `[]`. Los elementos dentro de la lista están separados por comas. Creemos una lista de colores:

```python
colors = ['rojo', 'verde', 'azul', 'amarillo']
```

### 2. Acceso a Elementos de una Lista por Índice

Los índices de las listas comienzan desde 0. Para acceder a un elemento específico, utiliza su índice dentro de corchetes:

```python
first_color = colors[0]  # Accede al primer elemento (rojo)
second_color = colors[1]  # Accede al segundo elemento (verde)
```

### 3. Determinación de la Longitud de una Lista

La función `len()` te permite conocer la cantidad de elementos en una lista:

```python
num_colors = len(colors)  # Devuelve 4 para nuestra lista de ejemplo
```

### 4. Agregar y Eliminar un Elemento de una Lista

**Agregar:**

```python
colors.append('negro')  # Agrega 'negro' al final de la lista
```

**Eliminar**:

```python
colors.remove('verde')  # Elimina el elemento 'green' de la lista
```

### 5. Uso de Índices Negativos

Los índices negativos cuentan desde el final de la lista. Por ejemplo:

```python
last_color = colors[-1]  # Accede al último elemento (yellow)
penultimate_color = colors[-2]  # Accede al segundo-to-último elemento (blue)
```

### 6. Búsqueda de un Valor en una Lista

Puedes utilizar la palabra clave `in` para verificar si un valor está presente en la lista:

```python
is_blue_present = 'azul' in colors  # Devuelve True si 'blue' está en la lista
```

En conclusión, comprender la estructura de una lista, acceder a elementos por índice, determinar su longitud, agregar y eliminar elementos, usar índices negativos y buscar valores son habilidades esenciales al trabajar con listas en Python. Estas capacidades te permiten gestionar y manipular eficientemente datos en tus programas.

---
## Manipulación de datos de la lista
En Python, la manipulación de listas va más allá de las operaciones básicas. En este segmento, exploraremos operaciones más avanzadas, la segmentación de listas para extraer subconjuntos y cómo ordenar listas de manera ascendente y descendente.

### 1. Operaciones con Listas

Las listas en Python admiten diversas operaciones que facilitan la manipulación de datos.

**Concatenación de Listas:**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2  # Resultado: [1, 2, 3, 4, 5, 6]
```

**Repetición de Listas:**

```python
repeated_list = list1 * 3  # Resultado: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

**Modificación de Elementos:**

```python
list1[0] = 10  # Modifica el primer elemento a 10
```

### 2. Segmentación de Listas

La segmentación te permite extraer porciones específicas de una lista.

```python
sublist = list1[1:3]  # Extrae elementos desde el índice 1 hasta el 2
```

La sintaxis es `[inicio:fin]`, donde el elemento en `inicio` está incluido y el elemento en `fin` no lo está.

### 3. Ordenación de Listas

Python proporciona métodos para ordenar listas de manera ascendente (`sort()`) o descendente (`sort(reverse=True)`).

```python
colors.sort()  # Ordena la lista de colores en orden alfabético ascendente
```

Si deseas mantener la lista original inalterada, puedes usar la función `sorted()`:

```python
ordered_colors = sorted(colors)  # Crea una nueva lista ordenada
```

Para ordenar en orden descendente:

```python
colors.sort(reverse=True)  # Ordena la lista de colores en orden alfabético descendente
```

Estas operaciones de lista, segmentación y ordenamiento son esenciales para manipular datos de manera efectiva en Python. Ya sea combinando listas, extrayendo subconjuntos específicos o clasificando elementos, estas herramientas hacen que trabajar con listas sea poderoso y flexible.

---
## Trabajo con números en listas
Cuando trabajas con listas numéricas en Python, las funciones `min()`, `max()`, y `sum()` son herramientas esenciales para obtener información clave sobre tus datos. Aquí te mostramos cómo utilizarlas de manera efectiva.

### 1. Uso de `min()` y `max()` con Listas

**Encontrar el Valor Mínimo:**

```python
numbers = [5, 2, 8, 1, 9]
min_value = min(numbers)  # Resultado: 1
```

**Encontrar el Valor Máximo:**

```python
max_value = max(numbers)  # Resultado: 9
```

Estas funciones te permiten identificar rápidamente los valores mínimo y máximo en una lista numérica.

### 2. Sumar Todos los Valores de una Lista

**Utilizando la Función `sum()`:**

```python
total_amount = sum(numbers)  # Resultado: 25
```

La función `sum()` proporciona una forma concisa de calcular la suma total de todos los elementos en una lista numérica.


El uso de `min()` y `max()` es fundamental para identificar los valores extremos en tus datos. Por otro lado, `sum()` te permite calcular fácilmente la suma total de los elementos en una lista numérica. Estas funciones son esenciales al trabajar con números en listas, facilitando la obtención de información valiosa y permitiéndote realizar análisis y manipulación de datos de manera eficiente en Python.

---
## Métodos de listas
En Python, las listas son un tipo de datos muy versátil y tienen varios métodos integrados que facilitan la manipulación y manipulación de datos. Aquí hay algunos métodos comunes de listas en Python:

### 1. `append()`

Añade un elemento al final de la lista.

```python
fruit = ['manzana', 'naranja', 'plátano']
fruit.append('uva')  # Resultado: ['manzana', 'naranja', 'plátano', 'uva']
```

### 2. `extend()`

Extiende la lista agregando los elementos de otra lista al final.

```python
vegetables = ['zanahoria', 'brócoli']
fruit.extend(vegetables)  # Resultado: ['manzana', 'naranja', 'plátano', 'uva', 'zanahoria', 'brócoli']
```

### 3. `insert()`

Inserta un elemento en una posición específica de la lista.

```python
fruit.insert(1, 'pera')  # Inserta 'pera' en la posición 1
# Resultado: ['manzana', 'pera', 'naranja', 'plátano', 'uva', 'zanahoria', 'brócoli']
```

### 4. `remove()`

Elimina la primera aparición de un elemento de la lista.

```python
fruit.remove('naranja')  # Elimina 'naranja'
# Resultado: ['manzana', 'pera', 'plátano', 'uva', 'zanahoria', 'brócoli']
```

### 5. `pop()`

Elimina y devuelve el elemento en una posición específica de la lista.

```python
deleted_item = fruit.pop(2)  # Elimina el elemento en la posición 2 ('plátano')
# Resultado de frutas: ['manzana', 'pera', 'uva', 'zanahoria', 'brócoli']
# Valor de elemento_eliminado: 'plátano'
```

### 6. `index()`

Devuelve la primera posición de un elemento específico en la lista.

```python
position = fruit.index('uva')  # Devuelve la posición de 'uva' en la lista
# Resultado: 2
```

### 7. `count()`

Devuelve el número de veces que un elemento aparece en la lista.

```python
quantity_grapes = fruit.count('uva')  # Cuenta cuántas veces aparece 'uva'
# Resultado: 1
```

### 8. `sort()`

Ordena la lista en orden ascendente.

```python
fruit.sort()  # Ordena la lista alfabéticamente
# Resultado: ['brócoli', 'manzana', 'pera', 'uva', 'zanahoria']
```

### 9. `reverse()`

Invierte el orden de los elementos en la lista.

```python
fruit.reverse()  # Invierte el orden de la lista
# Resultado: ['zanahoria', 'uva', 'pera', 'manzana', 'brócoli']
```

Estos son solo algunos de los muchos métodos disponibles para trabajar con listas en Python. La familiaridad con estos métodos te ayudará a aprovechar al máximo las listas en tus programas.

---
## Creación de una tupla
En Python, una tupla es una colección ordenada e inmutable de elementos. Puedes crear una tupla de varias maneras. Aquí tienes algunos ejemplos:

**Creación de una Tupla con Paréntesis:**

```python
my_tuple = (1, 2, 3, 'cuatro', 5.0)
```

**Creación de una Tupla sin Paréntesis:**

```python
another_tuple = 1, 'dos', 3.0, (4, 5)
```

**Tupla Vacía:**

```python
empty_tuple = ()
```

**Tupla con un Solo Elemento (Importante agregar la coma al final):**

```python
tuple_an_element = (42,)
```

**Conversión de una Lista a una Tupla:**

```python
my_list = [1, 2, 3]
tuple_from_list = tuple(my_list)
```

**Creación de una Tupla con la Función `tuple()`:**

```python
new_tuple = tuple('Hola')
# Resultado: ('H', 'o', 'l', 'a')
```

Las tuplas son inmutables, lo que significa que no puedes cambiar sus elementos después de haber sido creadas. Puedes acceder a los elementos de una tupla mediante índices, al igual que con las listas. Por ejemplo:

```python
print(my_tuple[0])  # Imprime el primer elemento de la tupla (1)
```

Recuerda que las tuplas son útiles cuando necesitas colecciones de datos inmutables, y su sintaxis es muy parecida a la de las listas.

---
## Pilas y colas en python
En Python, puedes implementar pilas y colas utilizando listas. Aunque Python no tiene tipos de datos específicos para pilas y colas en su biblioteca estándar, las listas son lo suficientemente flexibles para funcionar como estructuras de datos para estos propósitos. Aquí hay ejemplos de cómo puedes implementar pilas y colas:

### Pilas

Una pila sigue el principio de LIFO (Last In, First Out). El último elemento que se agrega es el primero en ser eliminado.

**Implementación de una Pila:**

```python
stack = []

# Agregar elementos a la pila
stack.append(1)
stack.append(2)
stack.append(3)

# Retirar elementos de la pila
element = stack.pop()
print(element)  # Resultado: 3
```

### Colas

Una cola sigue el principio de FIFO (First In, First Out). El primer elemento que se agrega es el primero en ser eliminado.

**Implementación de una Cola:**

```python
from collections import deque

cola = deque()

# Agregar elementos a la cola
cola.append(1)
cola.append(2)
cola.append(3)

# Retirar elementos de la cola
element = cola.popleft()
print(element)  # Resultado: 1
```

### Utilizando `queue` para Colas

La biblioteca estándar de Python también proporciona un módulo llamado `queue` que contiene implementaciones más seguras y eficientes para colas. Aquí hay un ejemplo:

```python
from queue import Queue

cola = Queue()

# Agregar elementos a la cola
cola.put(1)
cola.put(2)
cola.put(3)

# Retirar elementos de la cola
element = cola.get()
print(element)  # Resultado: 1
```

Estos son ejemplos básicos para entender cómo funcionan las pilas y colas en Python utilizando listas o el módulo `queue`. Puedes ajustar estas implementaciones según tus necesidades específicas.

---
## Resumen
En la sección anterior, exploramos de manera exhaustiva el uso de listas y tuplas en Python. Comenzamos abordando la creación de listas, aprendiendo a organizar datos de manera eficiente. A lo largo del recorrido, nos sumergimos en la manipulación de datos en listas, adquiriendo habilidades para modificar, agregar y eliminar elementos según nuestras necesidades. También exploramos cómo trabajar con números en listas, abordando conceptos matemáticos y estadísticos esenciales.

No obstante, la exploración no se limitó solo a las listas. Profundizamos en los métodos de listas, herramientas poderosas que mejoran la capacidad de manipulación de estos versátiles contenedores, simplificando y optimizando nuestro código.

En la segunda parte de nuestra travesía, nos aventuramos en el intrigante mundo de las tuplas. Descubrimos cómo crear estas estructuras inmutables y comprendimos las situaciones en las que su uso es más apropiado que el de las listas, ampliando así nuestras opciones de diseño de programas.

Finalmente, concluimos explorando las pilas y colas en Python, dos estructuras de datos fundamentales que nos proporcionan herramientas poderosas para gestionar y organizar información de manera eficaz, ofreciendo nuevas perspectivas en la resolución de problemas algorítmicos.

Este resumen refleja la riqueza y diversidad de conocimientos adquiridos en nuestra inmersión en el "Uso de listas y tuplas" en Python, preparándonos para enfrentar desafíos más complejos y emocionantes en el vasto mundo de la programación.
