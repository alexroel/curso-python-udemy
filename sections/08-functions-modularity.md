# Funciones y Modularidad

1. [Introducción](#introducción)
2. [Definición y uso de funciones](#definición-y-uso-de-funciones)
3. [Alcance de variables (scope)](#alcance-de-variables-scope)
4. [Argumentos indefinidos](#argumentos-indefinidos)
5. [Función recursiva](#función-recursiva)
6. [Anotaciones de tipos](#anotaciones-de-tipos)
7. [Módulos y paquetes](#módulos-y-paquetes)
8. [Proyecto de sección](#proyecto-de-sección)
9. [Resumen](#resumen)

---
## Introducción
¡Bienvenido a la sección de funciones y modularización de nuestro curso de Python! En esta sección, exploraremos conceptos fundamentales que te permitirán escribir código más organizado, eficiente y reutilizable. Aquí están los temas que abordaremos:

### 1. Definición y uso de funciones
Las funciones son bloques de código reutilizables que realizan una tarea específica. Aprenderemos cómo definir funciones, pasar argumentos y devolver valores.

### 2. Alcance de variables (scope)
Comprenderemos cómo las variables tienen diferentes ámbitos dentro y fuera de las funciones. Esto es esencial para evitar errores y entender dónde se puede acceder a una variable en un programa.

### 3. Argumentos indefinidos
Aprenderemos sobre formas flexibles de trabajar con argumentos, incluyendo argumentos posicionales, argumentos de palabras clave y cómo manejar argumentos variables.

### 4. Función recursiva
Exploraremos cómo definir y utilizar funciones que se llaman a sí mismas, un concepto clave en programación para resolver problemas de manera elegante y eficiente.

### 5. Módulos y paquetes
Entenderemos cómo organizar nuestro código en módulos y paquetes para facilitar la gestión y reutilización del código en proyectos más grandes.

### 6. Proyecto de sección
Al final de esta sección, te guiaremos en la creación de un proyecto que aplicará todos los conceptos aprendidos. Este proyecto te permitirá poner en práctica tus habilidades en la creación de funciones, manejo de variables, argumentos y modularización.

¡Vamos a sumergirnos en estos conceptos y desarrollar tus habilidades para que puedas construir aplicaciones más robustas y estructuradas en Python! Si tienes alguna pregunta a lo largo de esta sección, no dudes en plantearla. ¡A por ello!

---
## Definición y uso de funciones
En Python, una función es un bloque de código reutilizable que realiza una tarea específica. Estas funciones pueden tener parámetros (inputs) y devolver un resultado (output). La definición de una función se realiza con la palabra clave `def`, seguida del nombre de la función y la lista de parámetros entre paréntesis. A continuación, se incluye un bloque de código indentado que representa el cuerpo de la función.

Aquí está la sintaxis básica para definir una función en Python:

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # Cuerpo de la función
    # Puedes hacer operaciones y cálculos aquí
    return resultado  # Opcional: devolver un resultado
```

- `nombre_de_la_funcion`: Es el nombre de la función y debe seguir las reglas de nomenclatura de Python.
- `parametro1, parametro2, ...`: Son los parámetros que la función puede recibir. Pueden ser cualquier tipo de datos, como números, cadenas, listas, etc.
- `return resultado`: Es opcional y se usa para devolver un resultado al llamar a la función.

Aquí hay un ejemplo sencillo de una función que suma dos números y devuelve el resultado:

```python
def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función e impresión del resultado
print(suma(5, 3))  # Imprime: 8
```

Puedes usar funciones para organizar tu código, evitar duplicación y hacerlo más modular y fácil de mantener. También puedes importar funciones definidas en otros archivos o bibliotecas usando la palabra clave `import`.

Es común utilizar funciones en Python para encapsular piezas de código que realizan una tarea específica, lo que facilita la lectura y el mantenimiento del programa.

---
## Alcance de variables (scope)
El alcance de una variable, también conocido como "scope" en inglés, se refiere a la parte de un programa donde una variable es accesible y puede ser utilizada. En Python, el alcance de una variable puede ser local, global o de nivel de función. Veamos cada uno de estos alcances en detalle:

1. **Alcance local (Local Scope)**:
   Una variable tiene un alcance local cuando es declarada dentro de una función. Estas variables solo son accesibles dentro de la función en la que fueron definidas. No se pueden usar fuera de esa función.

    ```python
    def mi_funcion():
        x = 10  # x tiene alcance local dentro de mi_funcion
        print(x)

    mi_funcion()  # Se imprime: 10
    # print(x)  # Esto generaría un error, ya que x no es accesible aquí
    ```

2. **Alcance global (Global Scope)**:
   Una variable tiene un alcance global cuando se declara fuera de cualquier función o clase. Estas variables son accesibles desde cualquier parte del programa, incluyendo dentro de funciones.

    ```python
    y = 20  # y tiene alcance global

    def otra_funcion():
        print(y)  # y se puede acceder dentro de la función

    otra_funcion()  # Se imprime: 20
    print(y)  # Se imprime: 20
    ```

3. **Alcance de función anidada (Enclosing Function Scope)**:
   Si hay una función dentro de otra función, la función interna puede acceder a las variables de la función externa. Las variables en el alcance de la función externa se consideran en un alcance de función anidada.

    ```python
    def funcion_externa():
        z = 30  # z tiene alcance en funcion_externa

        def funcion_interna():
            print(z)  # z se puede acceder dentro de la función interna

        funcion_interna()

    funcion_externa()  # Se imprime: 30
    ```

Es importante tener en cuenta que las variables en Python siguen una regla de "LEGB" para determinar su alcance, que significa:
- **L**: Busca en el alcance local.
- **E**: Busca en el alcance de la función que engloba (función anidada).
- **G**: Busca en el alcance global.
- **B**: Busca en el alcance de las funciones predefinidas (built-in functions).

Si una variable no se encuentra en el alcance local, Python buscará en los ámbitos superiores siguiendo este orden hasta encontrar la variable o hasta llegar al alcance global.

---
## Argumentos indefinidos
En Python, puedes definir funciones que acepten un número indefinido de argumentos usando tres formas principales: argumentos posicionales arbitrarios, argumentos de palabra clave arbitrarios y una combinación de ambos. Esto es útil cuando no sabes cuántos argumentos se pasarán a la función en tiempo de ejecución.

1. **Argumentos posicionales arbitrarios (`*args`)**:
   Puedes usar el asterisco (`*`) antes de un parámetro en la definición de la función para indicar que la función aceptará un número arbitrario de argumentos posicionales. Estos argumentos se empacarán en una tupla y podrás acceder a ellos mediante el nombre `args` (o cualquier otro nombre que elijas).

   ```python
   def funcion_con_args(*args):
       for arg in args:
           print(arg)

   funcion_con_args(1, 2, 3, 'a', 'b', 'c')
   ```

2. **Argumentos de palabra clave arbitrarios (`**kwargs`)**:
   Puedes usar dos asteriscos (`**`) antes de un parámetro en la definición de la función para indicar que la función aceptará un número arbitrario de argumentos de palabra clave. Estos argumentos se empacarán en un diccionario y podrás acceder a ellos mediante el nombre `kwargs` (o cualquier otro nombre que elijas).

   ```python
   def funcion_con_kwargs(**kwargs):
       for clave, valor in kwargs.items():
           print(f'{clave}: {valor}')

   funcion_con_kwargs(nombre='Alice', edad=30, ciudad='Nueva York')
   ```

3. **Combinación de argumentos (`*args` y `**kwargs`)**:
   Puedes combinar argumentos posicionales arbitrarios y argumentos de palabra clave arbitrarios en una misma función.

   ```python
   def funcion_con_args_y_kwargs(*args, **kwargs):
       for arg in args:
           print(arg)
       
       for clave, valor in kwargs.items():
           print(f'{clave}: {valor}')

   funcion_con_args_y_kwargs(1, 2, 3, nombre='Alice', edad=30)
   ```

   En este ejemplo, puedes pasar tanto argumentos posicionales como argumentos de palabra clave.

Estas técnicas te permiten crear funciones más flexibles y versátiles que pueden adaptarse a diferentes situaciones donde no conoces de antemano la cantidad exacta de argumentos que se pasarán. Es importante recordar que los argumentos posicionales deben preceder a los argumentos de palabra clave al llamar a la función.

---
## Función recursiva
Una función recursiva es una función que se llama a sí misma dentro de su propio cuerpo para resolver un problema. La recursión es una técnica poderosa en programación y se utiliza para dividir un problema en subproblemas más pequeños y manejables.

Aquí hay un ejemplo sencillo de una función recursiva en Python que calcula el factorial de un número:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado = factorial(5)
print("El factorial de 5 es:", resultado)  # Imprime: El factorial de 5 es: 120
```

En este ejemplo, la función `factorial` se llama a sí misma con un argumento menor (`n - 1`) en cada llamada hasta que alcanza el caso base (cuando `n` es 0 o 1), en cuyo caso devuelve 1. Luego, la función se desenrolla y calcula el resultado multiplicando `n` por el resultado de la llamada recursiva.

Es importante tener un caso base que detenga la recursión para evitar un bucle infinito. Cada llamada recursiva debe acercarse al caso base en algún momento.

Algunas cosas a considerar al trabajar con funciones recursivas:
- Asegúrate de tener un caso base que detenga la recursión.
- Verifica que el problema se divida en subproblemas más pequeños en cada llamada recursiva.
- La recursión puede tener un costo en términos de uso de memoria y tiempo de ejecución, especialmente para problemas grandes. Puedes optimizar la recursión en algunos casos.

Espero que este ejemplo te ayude a entender cómo se utiliza la recursión en Python. Si tienes alguna pregunta adicional o necesitas más clarificaciones, no dudes en preguntar.

---
## Anotaciones de tipos
Las "anotaciones de tipos" en Python se refieren a la capacidad de especificar el tipo de datos que se espera que una función o variable contenga. Estas anotaciones no afectan el comportamiento del código en tiempo de ejecución, pero pueden ser útiles para proporcionar información a otros desarrolladores y herramientas que analizan el código.

Aquí tienes ejemplos de cómo se pueden utilizar las anotaciones de tipos en Python:

1. **Anotaciones de tipos para funciones:**

```python
def suma(a: int, b: int) -> int:
    return a + b

resultado = suma(3, 5)  # La función espera dos enteros y devuelve un entero
print(resultado)  # Imprime 8
```

En este ejemplo, la función `suma` tiene anotaciones de tipos que indican que espera dos argumentos de tipo entero (`int`) y devuelve un entero.

2. **Anotaciones de tipos para variables:**

```python
edad: int = 25
nombre: str = "Alice"
```

Aquí, las variables `edad` y `nombre` tienen anotaciones de tipo indicando que `edad` es de tipo entero (`int`) y `nombre` es de tipo cadena (`str`).

3. **Anotaciones de tipos para estructuras de datos:**

```python
from typing import List, Tuple

def obtener_lista_enteros() -> List[int]:
    return [1, 2, 3]

def obtener_tupla() -> Tuple[int, str]:
    return (42, "hola")
```

En este caso, se utilizan anotaciones de tipos para indicar que `obtener_lista_enteros` devuelve una lista de enteros y que `obtener_tupla` devuelve una tupla con un entero y una cadena.

4. **Anotaciones de tipos para funciones con argumentos opcionales:**

```python
def saludo(nombre: str, veces: int = 1) -> str:
    return f"Hola {nombre}! " * veces

print(saludo("Alice"))  # Hola Alice!
print(saludo("Bob", 3))  # Hola Bob! Hola Bob! Hola Bob!
```

Aquí, la función `saludo` tiene una anotación de tipo para el argumento `nombre` (cadena) y `veces` (entero con un valor predeterminado de 1).

Recuerda que las anotaciones de tipos en Python son opcionales y no afectan al comportamiento del programa durante la ejecución. Puedes utilizar herramientas externas como `mypy` para realizar comprobaciones de tipos en tu código si así lo deseas.

Para agregar anotaciones de tipos a la función `factorial`, debemos especificar los tipos de los parámetros y el tipo de retorno. Aquí te muestro cómo hacerlo:

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado: int = factorial(5)
print("El factorial de 5 es:", resultado)  # Imprime: El factorial de 5 es: 120

```

En este caso, se ha anotado `n` con el tipo `int` para indicar que es un entero y se ha anotado el tipo de retorno de la función con `-> int` para indicar que la función devuelve un entero. Estas anotaciones proporcionan información sobre los tipos esperados y ayudan a los desarrolladores a comprender mejor cómo se debe usar la función.

---
## Módulos y paquetes
En Python, los módulos y paquetes son formas de organizar y reutilizar código. Permiten dividir un programa en componentes más pequeños, lo que facilita la gestión, la reutilización y la colaboración en proyectos de gran escala.

### Módulos:

Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, como funciones, variables y clases. Puedes acceder a estas definiciones desde otro archivo utilizando la palabra clave `import`. Algunos módulos son parte de la biblioteca estándar de Python, mientras que otros pueden ser creados por los propios programadores.

Ejemplo de un módulo simple llamado `mimodulo.py`:

```python
# mimodulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

PI = 3.14159265359
```

Para utilizar este módulo en otro archivo, puedes hacer lo siguiente:

```python
import mimodulo

mimodulo.saludar("Alice")  # Imprime: Hola, Alice!
print(mimodulo.PI)  # Imprime: 3.14159265359
```

### Paquetes:

Un paquete en Python es un directorio que contiene uno o más módulos. Para crear un paquete, simplemente crea un directorio y coloca dentro los módulos que deseas incluir. Para que Python reconozca el directorio como un paquete, debe contener un archivo especial llamado `__init__.py`.

Ejemplo de una estructura de paquete:

```
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```

Donde `__init__.py` puede estar vacío o contener código de inicialización para el paquete.

Para importar módulos de un paquete, puedes hacer lo siguiente:

```python
from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()
```

---
## Proyecto de sección
**Desarrollo de un Módulo de Saludos Aleatorios**

Bienvenidos al proyecto "Desarrollo de un Módulo de Saludos Aleatorios". El objetivo de este proyecto es crear un módulo llamado `greetings.py` que contendrá tres funciones proporcionadas: `random_format`, `hello` y `hellos`.

1. **random_format:** Una función que generará un saludo aleatorio a partir de una lista de saludos y nombres proporcionada como argumento.

2. **hello:** Una función que tomará un nombre como argumento y generará un saludo personalizado utilizando el nombre proporcionado.

3. **hellos:** Una función que tomará una lista de nombres y generará saludos personalizados para cada nombre en la lista.

El proyecto permitirá practicar varios conceptos, incluyendo la importación de módulos, el uso de funciones, manipulación de listas y diccionarios, así como el manejo de errores.

¿Listos para comenzar con el desarrollo del módulo de saludos aleatorios? ¡Adelante y demuestren sus habilidades!

### Código del modulo `greetings.py`

~~~python
import random 
from typing import List, Dict

# La función 'random_format' devuelve uno de varios mensajes de saludo seleccionado al azar.
def random_format() -> str:
    # Una lista de formatos de mensaje.
    formats = [
        "¡Hola, {}! ¡Bienvenido!",
        "¡Es genial verte, {}!",
        "¡Saludos, {}! ¡Encantado de conocerte!",
    ]

    # Seleccionar aleatoriamente un formato de mensaje especificando un índice aleatorio
    # para la lista de formatos.
    return random.choice(formats)

# La función 'hello' devuelve un saludo para la persona con el nombre dado.
def hello(name: str) -> str:
     # Si no se proporcionó un nombre, se lanza un error con un mensaje.
    if name == "":
        return f"Error: nombre vacío."
    
    # Si se recibió un nombre, se devuelve un mensaje que incluye el nombre
    # en un mensaje de bienvenida.
    message = random_format().format(name)
    #message = f"Hola, {name}. !Bienvenido!"
    return message

# Hola devuelve un mapa que asocia a cada una de las personas nombradas
# con un mensaje de saludo.
def hellos(names: List[str]) -> Dict[str, str]:
    # Un diccionario para asociar nombres con mensajes.
    messages = {}

    # Itera sobre la lista recibida de nombres, llamando
    # a la función hello para obtener un mensaje para cada nombre.
    for name in names:
        message = hello(name)
        messages[name] = message

    return messages    
~~~
Este código en Python define varias funciones para generar mensajes de saludo de manera aleatoria. Aquí está la explicación de cada parte del código:

1. `import random`: Importa el módulo `random`, que se utiliza para generar números aleatorios.

2. `from typing import List, Dict`: Importa las clases List y Dict del módulo typing, que se utilizan para proporcionar tipos de datos explícitos en la firma de las funciones.

3. `def random_format() -> str`: Define una función llamada `random_format` que devuelve un mensaje de saludo seleccionado al azar de una lista de formatos.

   - Se crea una lista llamada `formats` que contiene varios formatos de mensaje.
   - Se utiliza `random.choice` para seleccionar aleatoriamente un formato de mensaje de la lista y se devuelve.

4. `def hello(name: str) -> str`: Define una función llamada `hello` que recibe un nombre como argumento y devuelve un mensaje de saludo.

   - Si no se proporciona un nombre (nombre vacío), se devuelve un mensaje de error.
   - Si se proporciona un nombre, se llama a `random_format()` para obtener un formato de mensaje aleatorio y se inserta el nombre en el mensaje de bienvenida.

5. `def hellos(names: List[str]) -> Dict[str, str]`: Define una función llamada `hellos` que recibe una lista de nombres y devuelve un diccionario que asocia cada nombre con un mensaje de saludo.

   - Itera sobre la lista de nombres, llamando a la función `hello` para obtener un mensaje de saludo para cada nombre.
   - Asocia cada nombre con su respectivo mensaje en un diccionario y lo devuelve al final.

En resumen, el código genera mensajes de saludo aleatorios utilizando diferentes formatos y devuelve estos mensajes asociados a nombres proporcionados como entrada.

### Probanco código 

~~~python
import greetings 

print(greetings.hello("Alex"))

nombres = ["Alex", "Juan", "Perdro", "Suny"]

saludos = greetings.Hellos(nombres)
for saludo in saludos.values():
    print(saludo)
~~~


---
## Resumen
En la sección dedicada a funciones y modularización de nuestro curso de Python, exploramos conceptos fundamentales que permiten escribir código más organizado, eficiente y reutilizable. Aquí tienes un resumen de lo que abordamos:

### 1. Definición y uso de funciones
Aprendimos a definir funciones, pasar argumentos y devolver valores. Las funciones son bloques de código reutilizables diseñados para ejecutar tareas específicas.

### 2. Alcance de variables (scope)
Comprendimos cómo las variables tienen diferentes ámbitos dentro y fuera de las funciones, lo que es esencial para evitar errores y entender dónde se puede acceder a una variable en un programa.

### 3. Argumentos indefinidos
Exploramos las formas flexibles de trabajar con argumentos, incluyendo argumentos posicionales, argumentos de palabras clave y cómo manejar argumentos variables.

### 4. Función recursiva
Aprendimos a definir y utilizar funciones recursivas, un concepto clave en programación para resolver problemas de manera elegante y eficiente, al permitir que una función se llame a sí misma.

### 5. Módulos y paquetes
Entendimos cómo organizar nuestro código en módulos y paquetes para facilitar la gestión y reutilización del código en proyectos más grandes.

### 6. Proyecto de sección
Al final de esta sección, te guié en la creación de un proyecto que aplicó todos los conceptos aprendidos. Este proyecto te permitió poner en práctica tus habilidades en la creación de funciones, manejo de variables, argumentos y modularización.

En esta etapa, adquiriste conocimientos valiosos que te permitirán desarrollar aplicaciones más sólidas y estructuradas en Python. ¡Espero que hayas disfrutado esta sección y estés listo para aplicar estos conceptos en tus proyectos futuros! Si tienes alguna pregunta, no dudes en plantearla. ¡Sigue avanzando en tu aprendizaje!
