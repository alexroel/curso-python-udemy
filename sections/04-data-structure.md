# Estructuras de Datos

1. [Introducción](#introducción)
2. [Lista y tuplas](#lista-y-tuplas)
3. [Métodos de listas](#métodos-de-listas)
4. [Diccionarios](#diccionarios)
5. [Métodos de diccionarios](#métodos-de-diccionarios)
6. [Conjuntos](#conjuntos)
7. [Métodos de conjuntos](#métodos-de-conjuntos)
8. [Colas y Pilas](#colas-y-pilas)
9. [Proyecto de sección](#proyecto-de-sección)
10. [Resumen](#resumen)

---
## Introducción 
Bienvenidos a la sección dedicada a las estructuras de datos en nuestro curso de Python. En esta etapa del aprendizaje, exploraremos elementos fundamentales que permiten organizar, almacenar y manipular datos de manera eficiente en nuestros programas. Las estructuras de datos son esenciales para resolver problemas complejos y construir aplicaciones robustas.

Durante esta sección, nos enfocaremos en seis tipos principales de estructuras de datos en Python: listas, tuplas, diccionarios, conjuntos, colas y pilas. Estas estructuras nos proporcionan distintas formas de organizar y acceder a la información, cada una con sus propias características y aplicaciones.

**Temas a Cubrir:**

1. **Listas y Tuplas:**
   Comenzaremos explorando las listas y las tuplas, dos estructuras que nos permiten almacenar colecciones ordenadas de elementos. Analizaremos sus propiedades y cómo acceder y manipular los datos que contienen.

2. **Métodos de Listas:**
   Profundizaremos en los métodos específicos de las listas en Python, herramientas poderosas que facilitan la modificación, búsqueda y gestión de datos en listas.

3. **Diccionarios:**
   Los diccionarios son estructuras de datos clave-valor, proporcionando una manera eficiente de almacenar información y recuperarla según una clave específica. Aprenderemos a trabajar con diccionarios y sus características únicas.

4. **Métodos de Diccionarios:**
   Exploraremos los métodos disponibles para manipular y gestionar diccionarios en Python, optimizando nuestro uso de esta estructura.

5. **Conjuntos:**
   Los conjuntos son colecciones no ordenadas y sin duplicados, ofreciendo utilidad en diversas aplicaciones. Abordaremos cómo trabajar con conjuntos y sus ventajas.

6. **Métodos de Conjuntos:**
   Conoceremos los métodos que nos permiten realizar operaciones y manipulaciones efectivas en conjuntos, maximizando su funcionalidad.

7. **Colas y Pilas:**
   Examinaremos las estructuras de datos fundamentales de colas y pilas, esenciales en muchos algoritmos y aplicaciones.

Estamos entusiasmados por acompañarte en esta travesía de aprendizaje y desarrollo de habilidades fundamentales en Python. ¡Comencemos a explorar las estructuras de datos y su aplicación en la resolución de problemas!

---
## Lista y tuplas
En Python, las listas y las tuplas son tipos de datos que permiten almacenar múltiples elementos en una sola variable. A continuación, te mostraré cómo crear y trabajar con listas y tuplas:

### Listas:
Una lista es una colección ordenada y modificable de elementos. Se define utilizando corchetes `[ ]` y los elementos están separados por comas.

#### Crear una lista:
```python
mi_lista = [1, 2, 3, "hola", True]
```

#### Acceder a elementos de la lista por índice:
```python
print(mi_lista[0])  # Accede al primer elemento (índice 0)
print(mi_lista[3])  # Accede al cuarto elemento (índice 3)
```

#### Modificar elementos de la lista:
```python
mi_lista[1] = 42  # Modifica el segundo elemento
```

#### Agregar elementos a la lista:
```python
mi_lista.append(6)  # Agrega un elemento al final de la lista
```

### Tuplas:
Una tupla es una colección ordenada e inmutable de elementos. Se define utilizando paréntesis `( )` y los elementos están separados por comas.

#### Crear una tupla:
```python
mi_tupla = (1, 2, 3, "adiós", False)
```

#### Acceder a elementos de la tupla por índice:
```python
print(mi_tupla[0])  # Accede al primer elemento (índice 0)
print(mi_tupla[3])  # Accede al cuarto elemento (índice 3)
```

#### No se pueden modificar elementos de una tupla:
```python
mi_tupla[1] = 42  # Esto generará un error, ya que las tuplas son inmutables
```

Es importante recordar que las listas son mutables, lo que significa que puedes cambiar, agregar o eliminar elementos después de crear la lista. En cambio, las tuplas son inmutables y no puedes modificar sus elementos después de crearlas.

### Métodos de Lista s
Aquí tienes algunos de los métodos más comunes utilizados con listas en Python:

1. **`append(elemento)`**:
   Este método agrega un elemento al final de la lista.
   ```python
   lista = [1, 2, 3]
   lista.append(4)
   print(lista)  # Salida: [1, 2, 3, 4]
   ```

2. **`remove(elemento)`**:
   Elimina la primera ocurrencia de un elemento en la lista.
   ```python
   lista = [1, 2, 3, 2]
   lista.remove(2)
   print(lista)  # Salida: [1, 3, 2]
   ```

3. **`pop([índice])`**:
   Elimina y devuelve el elemento en la posición dada (o el último si no se especifica un índice).
   ```python
   lista = [1, 2, 3]
   elemento = lista.pop(1)
   print(elemento)  # Salida: 2
   print(lista)  # Salida: [1, 3]
   ```

4. **`index(elemento)`**:
   Devuelve el índice de la primera ocurrencia de un elemento en la lista.
   ```python
   lista = [10, 20, 30, 20]
   indice = lista.index(20)
   print(indice)  # Salida: 1
   ```

5. **`sort()`**:
   Ordena los elementos de la lista en su lugar (ascendente por defecto, o especifica `reverse=True` para ordenar en orden descendente).
   ```python
   lista = [3, 1, 2]
   lista.sort()
   print(lista)  # Salida: [1, 2, 3]
   ```

6. **`reverse()`**:
   Invierte el orden de los elementos de la lista en su lugar.
   ```python
   lista = [1, 2, 3]
   lista.reverse()
   print(lista)  # Salida: [3, 2, 1]
   ```

Estos métodos son esenciales para manipular listas de manera efectiva en Python y son ampliamente utilizados en el desarrollo de aplicaciones.

---
## Métodos de listas
Aquí te presento una lista de métodos de listas en Python junto con ejemplos para cada uno:

1. **`append(elemento)`**:
   Agrega un elemento al final de la lista.
   ```python
   lista = [1, 2, 3]
   lista.append(4)
   print(lista)  # Salida: [1, 2, 3, 4]
   ```

2. **`extend(iterable)`**:
   Extiende la lista agregando elementos del iterable proporcionado.
   ```python
   lista1 = [1, 2, 3]
   lista2 = [4, 5, 6]
   lista1.extend(lista2)
   print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]
   ```

3. **`insert(indice, elemento)`**:
   Inserta un elemento en la posición indicada.
   ```python
   lista = [1, 2, 3]
   lista.insert(1, 5)
   print(lista)  # Salida: [1, 5, 2, 3]
   ```

4. **`remove(elemento)`**:
   Elimina la primera ocurrencia del elemento en la lista.
   ```python
   lista = [1, 2, 3, 2]
   lista.remove(2)
   print(lista)  # Salida: [1, 3, 2]
   ```

5. **`pop([indice])`**:
   Elimina y devuelve el elemento en la posición dada (o el último si no se especifica un índice).
   ```python
   lista = [1, 2, 3]
   elemento = lista.pop(1)
   print(elemento)  # Salida: 2
   print(lista)  # Salida: [1, 3]
   ```

6. **`index(elemento)`**:
   Devuelve el índice de la primera ocurrencia del elemento en la lista.
   ```python
   lista = [10, 20, 30, 20]
   indice = lista.index(20)
   print(indice)  # Salida: 1
   ```

7. **`count(elemento)`**:
   Devuelve la cantidad de veces que aparece el elemento en la lista.
   ```python
   lista = [1, 2, 2, 3, 2]
   veces = lista.count(2)
   print(veces)  # Salida: 3
   ```

8. **`sort(key=None, reverse=False)`**:
   Ordena los elementos de la lista (ascendente por defecto, o especifica `reverse=True` para ordenar en orden descendente).
   ```python
   lista = [3, 1, 2]
   lista.sort()
   print(lista)  # Salida: [1, 2, 3]
   ```

9. **`reverse()`**:
   Invierte el orden de los elementos de la lista.
   ```python
   lista = [1, 2, 3]
   lista.reverse()
   print(lista)  # Salida: [3, 2, 1]
   ```

10. **`clear()`**:
    Elimina todos los elementos de la lista.
    ```python
    lista = [1, 2, 3]
    lista.clear()
    print(lista)  # Salida: []
    ```

11. **`copy()`**:
    Crea una copia superficial de la lista.
    ```python
    lista1 = [1, 2, 3]
    lista2 = lista1.copy()
    print(lista2)  # Salida: [1, 2, 3]
    ```

12. **`len()`**:
    Devuelve la longitud (número de elementos) de la lista.
    ```python
    lista = [1, 2, 3]
    longitud = len(lista)
    print(longitud)  # Salida: 3
    ```

Estos métodos son esenciales para trabajar con listas en Python y son ampliamente utilizados en el desarrollo de aplicaciones.

---
## Diccionarios 
En Python, un diccionario es una estructura de datos que permite almacenar pares clave-valor, donde cada clave debe ser única y se utiliza para acceder a su respectivo valor. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación. Aquí te muestro cómo trabajar con diccionarios en Python:

### Crear un diccionario:
```python
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

### Acceder a un valor mediante su clave:
```python
print(mi_diccionario["nombre"])  # Salida: "Juan"
print(mi_diccionario["edad"])  # Salida: 30
```

### Modificar un valor en el diccionario:
```python
mi_diccionario["edad"] = 31
print(mi_diccionario)  # Salida: {"nombre": "Juan", "edad": 31, "ciudad": "Madrid"}
```

### Agregar un nuevo par clave-valor al diccionario:
```python
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)  # Salida: {"nombre": "Juan", "edad": 31, "ciudad": "Madrid", "profesion": "Ingeniero"}
```

### Eliminar una clave y su valor del diccionario:
```python
del mi_diccionario["ciudad"]
print(mi_diccionario)  # Salida: {"nombre": "Juan", "edad": 31, "profesion": "Ingeniero"}
```

### Verificar si una clave está en el diccionario:
```python
print("nombre" in mi_diccionario)  # Salida: True
print("ciudad" in mi_diccionario)  # Salida: False
```

### Obtener todas las claves y valores del diccionario:
```python
print(mi_diccionario.keys())  # Salida: dict_keys(["nombre", "edad", "profesion"])
print(mi_diccionario.values())  # Salida: dict_values(["Juan", 31, "Ingeniero"])
```

### Iterar sobre las claves y valores del diccionario:
```python
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

# Salida:
# nombre Juan
# edad 31
# profesion Ingeniero
```

Los diccionarios son muy útiles cuando necesitas almacenar y acceder a datos de forma eficiente mediante un identificador único (la clave).

---
## Métodos de diccionarios
Aquí te presento una lista de métodos de diccionarios en Python junto con ejemplos para cada uno:

1. **`clear()`**:
   Elimina todos los elementos del diccionario.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   diccionario.clear()
   print(diccionario)  # Salida: {}
   ```

2. **`copy()`**:
   Crea una copia superficial del diccionario.
   ```python
   diccionario1 = {"nombre": "Juan", "edad": 30}
   diccionario2 = diccionario1.copy()
   print(diccionario2)  # Salida: {"nombre": "Juan", "edad": 30}
   ```

3. **`get(clave[, valor_predeterminado])`**:
   Devuelve el valor asociado con la clave dada, o un valor predeterminado si la clave no existe.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   print(diccionario.get("nombre"))  # Salida: "Juan"
   print(diccionario.get("ciudad", "N/A"))  # Salida: "N/A" (clave no existente)
   ```

4. **`items()`**:
   Devuelve una vista de tuplas de pares clave-valor en el diccionario.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   print(diccionario.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30)])
   ```

5. **`keys()`**:
   Devuelve una vista de las claves en el diccionario.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   print(diccionario.keys())  # Salida: dict_keys(['nombre', 'edad'])
   ```

6. **`values()`**:
   Devuelve una vista de los valores en el diccionario.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   print(diccionario.values())  # Salida: dict_values(['Juan', 30])
   ```

7. **`pop(clave[, valor_predeterminado])`**:
   Elimina y devuelve el valor asociado con la clave dada, o un valor predeterminado si la clave no existe.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   valor = diccionario.pop("nombre")
   print(valor)  # Salida: "Juan"
   print(diccionario)  # Salida: {"edad": 30}
   ```

8. **`popitem()`**:
   Elimina y devuelve un par clave-valor aleatorio como una tupla.
   ```python
   diccionario = {"nombre": "Juan", "edad": 30}
   par = diccionario.popitem()
   print(par)  # Salida: ('edad', 30)
   print(diccionario)  # Salida: {"nombre": "Juan"}
   ```

9. **`update(diccionario2)`**:
   Actualiza el diccionario con elementos del diccionario proporcionado.
   ```python
   diccionario1 = {"nombre": "Juan", "edad": 30}
   diccionario2 = {"ciudad": "Madrid", "edad": 31}
   diccionario1.update(diccionario2)
   print(diccionario1)  # Salida: {"nombre": "Juan", "edad": 31, "ciudad": "Madrid"}
   ```

10. **`setdefault(clave[, valor_predeterminado])`**:
    Devuelve el valor asociado con la clave dada, o inserta la clave con un valor predeterminado si no existe.
    ```python
    diccionario = {"nombre": "Juan", "edad": 30}
    valor = diccionario.setdefault("ciudad", "Madrid")
    print(valor)  # Salida: "Madrid" (valor predeterminado)
    print(diccionario)  # Salida: {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
    ```

11. **`fromkeys(iterable[, valor])`**:
    Crea un nuevo diccionario con claves del iterable y un valor opcional para todas las claves.
    ```python
    claves = ["a", "b", "c"]
    diccionario = dict.fromkeys(claves, 0)
    print(diccionario)  # Salida: {'a': 0, 'b': 0, 'c': 0}
    ```

Estos son algunos de los métodos más comunes para trabajar con diccionarios en Python. Son herramientas valiosas para manipular y gestionar datos en forma de pares clave-valor.

---
## Conjuntos 
En Python, un conjunto es una colección no ordenada y mutable de elementos únicos e inmutables. Los conjuntos se utilizan para almacenar elementos únicos, lo que significa que no puede haber duplicados en un conjunto. Aquí te muestro cómo trabajar con conjuntos en Python, junto con algunos de los métodos más comunes:

### Crear un conjunto:
Puedes crear un conjunto utilizando llaves `{}` o utilizando la función `set()`.
```python
mi_conjunto = {1, 2, 3}
```

### Agregar elementos a un conjunto:
Utiliza el método `add()` para agregar un solo elemento al conjunto. Para agregar múltiples elementos, usa el método `update()`.
```python
mi_conjunto.add(4)
mi_conjunto.update({5, 6, 7})
```

### Eliminar elementos de un conjunto:
Utiliza los métodos `remove()`, `discard()` o `pop()` para eliminar elementos de un conjunto.
```python
mi_conjunto.remove(3)  # Elimina el elemento 3
mi_conjunto.discard(4)  # Elimina el elemento 4
elemento_eliminado = mi_conjunto.pop()  # Elimina y devuelve un elemento al azar
```

### Verificar si un elemento está en un conjunto:
Utiliza la palabra clave `in` para verificar la existencia de un elemento en un conjunto.
```python
print(2 in mi_conjunto)  # Salida: True
print(10 in mi_conjunto)  # Salida: False
```

### Operaciones con conjuntos:
Python también ofrece operaciones comunes de conjuntos, como unión (`union()`), intersección (`intersection()`), diferencia (`difference()`), diferencia simétrica (`symmetric_difference()`), entre otros.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union_set = conjunto1.union(conjunto2)  # Unión de conjuntos
interseccion_set = conjunto1.intersection(conjunto2)  # Intersección de conjuntos
diferencia_set = conjunto1.difference(conjunto2)  # Diferencia de conjuntos
dif_simetrica_set = conjunto1.symmetric_difference(conjunto2)  # Diferencia simétrica de conjuntos
```

### Limpiar un conjunto:
Utiliza el método `clear()` para eliminar todos los elementos del conjunto.
```python
mi_conjunto.clear()
```

### Obtener el tamaño de un conjunto:
Utiliza la función `len()` para obtener el número de elementos en un conjunto.
```python
print(len(mi_conjunto))  # Salida: Número de elementos en el conjunto
```

Estos son algunos de los métodos y operaciones comunes que puedes realizar en conjuntos en Python. Los conjuntos son útiles para operaciones relacionadas con la teoría de conjuntos y para garantizar elementos únicos en una colección.

---
## Métodos de conjuntos
Aquí te presento algunos métodos comunes que puedes utilizar con conjuntos en Python:

1. **`add(elemento)`**:
   Agrega un elemento al conjunto.
   ```python
   conjunto = {1, 2, 3}
   conjunto.add(4)
   print(conjunto)  # Salida: {1, 2, 3, 4}
   ```

2. **`remove(elemento)`**:
   Elimina un elemento del conjunto. Si el elemento no está en el conjunto, genera un error.
   ```python
   conjunto = {1, 2, 3}
   conjunto.remove(2)
   print(conjunto)  # Salida: {1, 3}
   ```

3. **`discard(elemento)`**:
   Elimina un elemento del conjunto si está presente. Si el elemento no está en el conjunto, no genera un error y no realiza ninguna acción.
   ```python
   conjunto = {1, 2, 3}
   conjunto.discard(2)
   print(conjunto)  # Salida: {1, 3}
   ```

4. **`pop()`**:
   Elimina y devuelve un elemento aleatorio del conjunto. Si el conjunto está vacío, genera un error.
   ```python
   conjunto = {1, 2, 3}
   elemento = conjunto.pop()
   print(elemento)  # Salida: Un elemento aleatorio (por ejemplo, 1)
   ```

5. **`clear()`**:
   Elimina todos los elementos del conjunto, dejándolo vacío.
   ```python
   conjunto = {1, 2, 3}
   conjunto.clear()
   print(conjunto)  # Salida: set()
   ```

6. **`union(otro_conjunto)`**:
   Devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos (unión).
   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   union_conjuntos = conjunto1.union(conjunto2)
   print(union_conjuntos)  # Salida: {1, 2, 3, 4, 5}
   ```

7. **`intersection(otro_conjunto)`**:
   Devuelve un nuevo conjunto que contiene elementos presentes en ambos conjuntos (intersección).
   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   interseccion_conjuntos = conjunto1.intersection(conjunto2)
   print(interseccion_conjuntos)  # Salida: {3}
   ```

8. **`difference(otro_conjunto)`**:
   Devuelve un nuevo conjunto que contiene elementos que están en el primer conjunto pero no en el segundo (diferencia).
   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   diferencia_conjuntos = conjunto1.difference(conjunto2)
   print(diferencia_conjuntos)  # Salida: {1, 2}
   ```

9. **`symmetric_difference(otro_conjunto)`**:
   Devuelve un nuevo conjunto que contiene elementos que están en uno de los conjuntos, pero no en ambos (diferencia simétrica).
   ```python
   conjunto1 = {1, 2, 3}
   conjunto2 = {3, 4, 5}
   dif_simetrica_conjuntos = conjunto1.symmetric_difference(conjunto2)
   print(dif_simetrica_conjuntos)  # Salida: {1, 2, 4, 5}
   ```

10. **`issubset(otro_conjunto)`**:
    Devuelve `True` si todos los elementos del conjunto están en otro conjunto (subconjunto).
    ```python
    conjunto1 = {1, 2}
    conjunto2 = {1, 2, 3, 4}
    es_subconjunto = conjunto1.issubset(conjunto2)
    print(es_subconjunto)  # Salida: True
    ```

11. **`issuperset(otro_conjunto)`**:
    Devuelve `True` si todos los elementos de otro conjunto están en el conjunto (superconjunto).
    ```python
    conjunto1 = {1, 2, 3, 4}
    conjunto2 = {1, 2}
    es_superconjunto = conjunto1.issuperset(conjunto2)
    print(es_superconjunto)  # Salida: True
    ```

Estos métodos son fundamentales para trabajar con conjuntos en Python y te permiten realizar varias operaciones y manipulaciones sobre ellos.

---
## Colas y Pilas
Las colas y las pilas son estructuras de datos comúnmente utilizadas en programación para organizar y acceder a elementos de una manera específica. A continuación, te explico qué son y cómo puedes implementarlas en Python:

### Colas (Queue):

Una cola es una estructura de datos que sigue el principio de "primero en entrar, primero en salir" (FIFO - First In, First Out). Es similar a una cola de personas en la vida real, donde la primera persona que llega es la primera en ser atendida.

#### Implementación de una cola en Python:

Puedes implementar una cola utilizando la clase `deque` del módulo `collections` en Python.

```python
from collections import deque

# Crear una cola vacía utilizando deque
cola = deque()

# Agregar elementos a la cola
cola.append(1)
cola.append(2)
cola.append(3)

# Quitar el primer elemento de la cola (FIFO)
primer_elemento = cola.popleft()
print(primer_elemento)  # Salida: 1

# Tamaño de la cola
print(len(cola))  # Salida: 2

```

### Pilas (Stack):

Una pila es una estructura de datos que sigue el principio de "último en entrar, primero en salir" (LIFO - Last In, First Out). Es similar a una pila de platos, donde el último plato que se coloca es el primero que se retira.

#### Implementación de una pila en Python:

Puedes implementar una pila utilizando una lista en Python.

```python
# Crear una pila vacía utilizando una lista
pila = []

# Agregar elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)

# Quitar el último elemento agregado (LIFO)
ultimo_elemento = pila.pop()
print(ultimo_elemento)  # Salida: 3

# Tamaño de la pila
print(len(pila))  # Salida: 2

```

Tanto las colas como las pilas son estructuras de datos importantes en programación y se utilizan en muchos algoritmos y aplicaciones. Es importante comprender cómo funcionan y cómo implementarlas para aprovechar al máximo su utilidad.

---
## Proyecto de sección


---
## Resumen
En esta sección dedicada a las estructuras de datos en nuestro curso de Python, exploramos elementos fundamentales que permiten organizar, almacenar y manipular datos de manera eficiente en nuestros programas. Las estructuras de datos resultan esenciales para resolver problemas complejos y construir aplicaciones robustas.

Durante esta sección, nos enfocamos en seis tipos principales de estructuras de datos en Python: listas, tuplas, diccionarios, conjuntos, colas y pilas. Estas estructuras nos proporcionaron distintas formas de organizar y acceder a la información, cada una con sus propias características y aplicaciones.

A lo largo de la sección, abordamos los siguientes temas:

1. **Listas y Tuplas:**
   Exploramos las listas y las tuplas, dos estructuras que nos permiten almacenar colecciones ordenadas de elementos, analizando sus propiedades y cómo acceder y manipular los datos que contienen.

2. **Métodos de Listas:**
   Profundizamos en los métodos específicos de las listas en Python, herramientas poderosas que facilitan la modificación, búsqueda y gestión de datos en listas.

3. **Diccionarios:**
   Estudiamos los diccionarios, estructuras de datos clave-valor que ofrecen una manera eficiente de almacenar información y recuperarla según una clave específica, aprendiendo a trabajar con diccionarios y sus características únicas.

4. **Métodos de Diccionarios:**
   Exploramos los métodos disponibles para manipular y gestionar diccionarios en Python, optimizando nuestro uso de esta estructura.

5. **Conjuntos:**
   Analizamos los conjuntos, colecciones no ordenadas y sin duplicados que ofrecen utilidad en diversas aplicaciones, abordando cómo trabajar con conjuntos y sus ventajas.

6. **Métodos de Conjuntos:**
   Conocimos los métodos que nos permiten realizar operaciones y manipulaciones efectivas en conjuntos, maximizando su funcionalidad.

7. **Colas y Pilas:**
   Examinamos las estructuras de datos fundamentales de colas y pilas, esenciales en muchos algoritmos y aplicaciones.

Además, como parte de la consolidación de los conocimientos adquiridos, llevaste a cabo un emocionante proyecto. Utilizaste las estructuras de datos aprendidas para desarrollar una aplicación que simulaba un sistema de gestión de inventario para una tienda en línea. Este proyecto te permitió aplicar los conceptos de listas, diccionarios, conjuntos, colas y pilas en un contexto práctico y desafiante. Fue una travesía de aprendizaje en la que exploraste y aplicaste estas estructuras de datos para resolver problemas de manera efectiva.