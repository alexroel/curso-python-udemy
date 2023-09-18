# Estructuras de Control Básicas

1. [Introducción](#introducción)
2. [Condicionales (if, else, elif)](#condicionales-if-else-elif)
3. [Bucles (while, for)](#bucles-while-for)
4. [Uso de rangos y enumeración en bucles](#uso-de-rangos-y-enumeración-en-bucles)
5. [Control de flujo con break y continue](#control-de-flujo-con-break-y-continue)
6. [Ejercicio de sección](#ejercicio-de-sección)
7. [Resumen](#resumen)

---
## Introducción 
En esta sección del curso de Python, vamos a explorar algunas de las estructuras de control más fundamentales que Python ofrece. Estas estructuras son esenciales para controlar el flujo de un programa y tomar decisiones lógicas. En particular, nos centraremos en los siguientes temas:

**1. Condicionales (if, else, elif):** Los condicionales son herramientas clave para tomar decisiones en un programa. Aprenderemos a utilizar declaraciones condicionales para ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones. Esto nos permite crear programas flexibles y adaptativos.

**2. Bucles (while, for):** Los bucles son fundamentales para la repetición de tareas en un programa. Exploraremos cómo usar bucles `while` y `for` para ejecutar un bloque de código múltiples veces. Esto es útil para tareas como la iteración a través de listas o la ejecución de un conjunto de instrucciones hasta que se cumpla una condición.

**3. Uso de rangos y enumeración en bucles:** Python proporciona herramientas poderosas para trabajar con bucles. Veremos cómo usar rangos para generar secuencias de números y cómo utilizar la función `enumerate` para trabajar con índices y valores en bucles `for`.

**4. Control de flujo con break y continue:** Aprenderemos a usar las declaraciones `break` y `continue` para controlar el flujo de ejecución en bucles. Esto nos permite detener bucles prematuramente o saltar a la siguiente iteración según ciertas condiciones.

**5. Ejercicio de la sección:** Al final de esta sección, tendrás la oportunidad de poner en práctica lo que has aprendido a través de un ejercicio. Esto te ayudará a consolidar tus conocimientos y a aplicar estas estructuras de control en situaciones reales.

Estas estructuras de control son fundamentales para la programación en Python y en muchos otros lenguajes. Te proporcionarán las herramientas necesarias para escribir programas más complejos y funcionales. ¡Vamos a sumergirnos en cada uno de estos temas y comenzar a construir programas más sofisticados en Python!

---
## Condicionales (if, else, elif)
Los condicionales `if`, `else` y `elif` son estructuras de control en la mayoría de los lenguajes de programación que te permiten tomar decisiones basadas en ciertas condiciones. Aquí te explico cómo funcionan estos condicionales en Python, que es un lenguaje de programación popular:

1. **if**: El condicional `if` se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:

```python
if condicion:
    # Bloque de código que se ejecutará si la condición es verdadera
```

Ejemplo:

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
```

2. **else**: El condicional `else` se utiliza junto con `if` para especificar un bloque de código que se ejecutará si la condición del `if` es falsa. La sintaxis es:

```python
if condicion:
    # Bloque de código si la condición es verdadera
else:
    # Bloque de código si la condición es falsa
```

Ejemplo:

```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

3. **elif**: El condicional `elif` (abreviatura de "else if") se utiliza para manejar múltiples condiciones en una estructura de control. Puedes tener múltiples bloques `elif` después de un `if` y un bloque `else` opcional al final. La sintaxis es:

```python
if condicion1:
    # Bloque de código si condicion1 es verdadera
elif condicion2:
    # Bloque de código si condicion2 es verdadera
else:
    # Bloque de código si ninguna de las condiciones es verdadera
```

Ejemplo:

```python
nota = 75
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")
```

En este ejemplo, se evalúa la nota y se imprime la calificación correspondiente según la condición que se cumpla primero.

Estos condicionales son fundamentales en la programación, ya que te permiten tomar decisiones y ejecutar diferentes acciones en función de las condiciones que se cumplan en tu programa.

---
## Bucles (while, for)

Los bucles `while` y `for` son estructuras de control que se utilizan en la programación para repetir un bloque de código múltiples veces, pero difieren en cómo determinan cuándo detenerse y cuándo continuar. Aquí te explico cómo funcionan estos bucles en Python:

1. **Bucle `while`**: El bucle `while` se ejecuta mientras una condición específica sea verdadera. La sintaxis básica es la siguiente:

```python
while condicion:
    # Bloque de código que se ejecutará mientras la condición sea verdadera
```

Ejemplo:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Este bucle imprimirá los números del 0 al 4, ya que se ejecuta mientras `contador` sea menor que 5.

2. **Bucle `for`**: El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena de caracteres, etc.) y ejecutar un bloque de código para cada elemento de esa secuencia. La sintaxis básica es la siguiente:

```python
for elemento in secuencia:
    # Bloque de código que se ejecutará para cada elemento de la secuencia
```

Ejemplo:

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

Este bucle imprimirá cada elemento de la lista `frutas`.

Además de la estructura básica de `for`, puedes usar la función `range()` para generar una secuencia de números y recorrerla en un bucle `for`. Por ejemplo:

```python
for i in range(5):
    print(i)
```

Este bucle imprimirá los números del 0 al 4.

En resumen, los bucles `while` son útiles cuando no sabes cuántas veces necesitas repetir un bloque de código, pero necesitas que una condición se cumpla para detener la ejecución. Los bucles `for` son ideales para recorrer elementos en una secuencia de manera controlada. Ambos tipos de bucles son esenciales en la programación y se utilizan para diferentes situaciones según las necesidades de tu programa.

---
## Uso de rangos y enumeración en bucles
El uso de rangos y enumeración en bucles es una técnica común en la programación que te permite iterar sobre una secuencia de números o elementos con mayor control y facilidad. En Python, puedes hacer uso de la función `range()` para crear rangos numéricos y la función `enumerate()` para obtener tanto el valor como el índice de los elementos en una secuencia. Aquí te explico cómo utilizarlos:

**1. Uso de `range()` en bucles:**

La función `range()` genera una secuencia de números enteros desde un valor inicial hasta un valor final, con un paso opcional. La sintaxis básica es:

```python
range(valor_inicial, valor_final, paso)
```

- `valor_inicial`: El primer valor en el rango (incluido).
- `valor_final`: El valor final en el rango (excluido).
- `paso`: El incremento entre los números en el rango (opcional).

Puedes utilizar `range()` en bucles `for` para controlar el número de iteraciones:

```python
for i in range(1, 6):
    print(i)
```

Este bucle imprimirá los números del 1 al 5, ya que `range(1, 6)` genera una secuencia que incluye 1 pero excluye 6.

**2. Uso de `enumerate()` en bucles:**

La función `enumerate()` se utiliza para iterar sobre elementos de una secuencia (como una lista) y obtener tanto el valor como el índice de cada elemento. La sintaxis es la siguiente:

```python
for indice, valor in enumerate(secuencia):
    # Bloque de código que utiliza el índice y el valor
```

Ejemplo:

```python
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
```

Este bucle imprimirá:

```
Índice 0: manzana
Índice 1: banana
Índice 2: cereza
```

`enumerate()` es útil cuando necesitas realizar operaciones basadas en la posición o el índice de los elementos en una secuencia.

En resumen, el uso de `range()` te permite generar secuencias numéricas controladas para bucles `for`, mientras que `enumerate()` te ayuda a obtener tanto el valor como el índice de los elementos en una secuencia. Estas funciones son herramientas útiles para mejorar el control y la funcionalidad de tus bucles en Python.

---
## Control de flujo con break y continue
`break` y `continue` son dos palabras clave que se utilizan para controlar el flujo de ejecución en bucles en Python (y en otros lenguajes de programación). A continuación, te explico cómo funcionan:

1. **`break`**:

La palabra clave `break` se utiliza para salir inmediatamente de un bucle, ya sea un bucle `for` o un bucle `while`. Cuando se encuentra un `break`, el bucle se detiene y la ejecución continúa fuera del bucle. Esta es útil cuando deseas salir del bucle antes de que se complete su ejecución normal.

Ejemplo con un bucle `while`:

```python
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

Este bucle imprimirá los números del 0 al 2 y se detendrá cuando `i` sea igual a 3 debido al `break`.

Ejemplo con un bucle `for`:

```python
for letra in "Python":
    if letra == "h":
        break
    print(letra)
```

Este bucle imprimirá "P" y "y" y se detendrá cuando encuentre la letra "h" debido al `break`.

2. **`continue`**:

La palabra clave `continue` se utiliza para saltar la iteración actual en un bucle y continuar con la siguiente. Cuando se encuentra un `continue`, el resto del bloque de código dentro del bucle para la iteración actual y el bucle continúa con la siguiente iteración.

Ejemplo con un bucle `for`:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Este bucle imprimirá todos los números del 0 al 4, excepto el 2, porque se omite esa iteración debido al `continue`.

Ejemplo con un bucle `while`:

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

Este bucle imprimirá todos los números del 1 al 5, excepto el 3, debido al `continue`.

En resumen, `break` se usa para salir inmediatamente de un bucle, mientras que `continue` se utiliza para saltar una iteración y pasar a la siguiente. Ambos son útiles para controlar el flujo de ejecución en bucles y adaptar el comportamiento del programa según las condiciones que se cumplan.

---
## Ejercicio de sección
¡Por supuesto! Crearemos un proyecto de adivinar el número en el que utilizaremos las estructuras de control básicas que mencionaste: condicionales (if, else, elif), bucles (while, for), uso de rangos y enumeración en bucles, y control de flujo con break y continue.

## Proyecto: Juego de Adivina el Número

### Introducción
Este proyecto implica crear un juego simple llamado "Adivina el Número". El juego consiste en que el jugador intenta adivinar un número aleatorio generado por la computadora dentro de un rango específico. Se utilizan estructuras de control básicas para manejar las adivinanzas del jugador y proporcionar pistas hasta que adivine el número correcto.

### Objetivo del Juego
El objetivo del juego es que el jugador adivine el número aleatorio generado por la computadora dentro del rango dado.

### Estructuras de Control Utilizadas
1. **Condicionales (if, else, elif):** Se utilizan condicionales para verificar si la adivinanza del jugador es mayor, menor o igual al número aleatorio.

2. **Bucles (while):** Se utiliza un bucle while para permitir que el jugador haga múltiples adivinanzas hasta que adivine correctamente el número.

3. **Uso de Rangos y Enumeración en Bucles:** Se establece un rango de números dentro del cual el jugador puede hacer adivinanzas.

4. **Control de Flujo con Break y Continue:** Se usa `break` para salir del bucle cuando el jugador adivina correctamente. No se utiliza `continue` en este juego.

### Implementación
Para implementar este juego, necesitarás un entorno de programación y conocimientos básicos de Python. Puedes utilizar un entorno de desarrollo como Jupyter Notebook, PyCharm o cualquier editor de texto compatible con Python.

1. **Generación del Número Aleatorio:**
   Genera un número aleatorio dentro de un rango específico.

2. **Interacción con el Jugador:**
   Permite al jugador hacer adivinanzas y proporciona pistas sobre si la adivinanza es mayor, menor o igual al número generado.

3. **Bucle para Adivinanzas:**
   Utiliza un bucle while para permitir al jugador hacer adivinanzas repetidas hasta que adivine correctamente.

4. **Condiciones de Finalización:**
   Si el jugador adivina correctamente, muestra un mensaje de victoria. Si decide salir del juego, muestra un mensaje de despedida.

### Código del juego

~~~python
import random

# Genera un número aleatorio dentro del rango [1, 100]
numero_secreto = random.randint(1, 100)

intentos = 0
max_intentos = 10

print("¡Bienvenido a Adivina el Número!")
print(f"Adivina un número entre 1 y 100. Tienes un máximo de {max_intentos} intentos.")

while intentos < max_intentos:
    intento = int(input("Introduce tu adivinanza: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! ¡Adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
        break

if intentos >= max_intentos:
    print(f"¡Agotaste tus {max_intentos} intentos! El número secreto era {numero_secreto}.")
    
print("Gracias por jugar. ¡Hasta la próxima!")

~~~

---
## Resumen
En esta sección del curso de Python, exploramos algunas de las estructuras de control más fundamentales de Python. Hemos aprendido sobre condicionales, como `if`, `else` y `elif`, que nos permiten tomar decisiones lógicas en nuestro código. También hemos visto cómo utilizar bucles `while` y `for` para repetir tareas, y cómo trabajar con rangos y la función `enumerate` en bucles `for`. Además, hemos discutido cómo controlar el flujo de ejecución con las declaraciones `break` y `continue`.

Al final de esta sección, tuviste la oportunidad de aplicar estos conceptos a través de un ejercicio práctico. Estas estructuras de control son esenciales para escribir programas más complejos y versátiles en Python. Esperamos que hayas adquirido un sólido entendimiento de estos conceptos y que te sientas más seguro al utilizarlos en tus propios proyectos de programación.