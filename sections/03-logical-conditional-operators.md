# Operadores lógicos y condicionales

1. [Introducción](#introducción)
2. [Operadores relacionales](#operadores-relacionales)
3. [Condicionales (if, else))](#condicionales-if-else)
4. [Condiciones anidadas](#condiciones-anidadas)
5. [Operadores lógicos](#operadores-lógicos)
6. [Proyecto de sección](#proyecto-de-sección)
7. [Resumen](#resumen)

---
## Introducción 
**Introducción: Explorando el Mundo de la Lógica y las Condiciones en la Programación**

Bienvenidos a la sección dedicada a los fundamentos esenciales de la programación: los operadores lógicos y condicionales. En este viaje, nos sumergiremos en el fascinante universo de la toma de decisiones en el código, donde cada línea de instrucción puede desencadenar diferentes caminos de ejecución.

**Operadores Relacionales: Desentrañando las Relaciones entre Datos**

Comenzaremos nuestro viaje explorando los operadores relacionales, herramientas cruciales para comparar valores y establecer condiciones en nuestros programas. Descubriremos cómo utilizar estos operadores para evaluar si dos valores son iguales, diferentes, mayores o menores, abriendo así la puerta a un mundo de posibilidades lógicas.

**Condicionales (if, else): Tomando Decisiones en el Código**

La programación se trata de tomar decisiones, y los condicionales son nuestras herramientas clave. Profundizaremos en la estructura "if, else" que permite ejecutar bloques de código basados en condiciones específicas. Aprenderemos a dirigir el flujo de nuestro programa, permitiendo respuestas dinámicas a diferentes situaciones.

**Condiciones Anidadas: Elevando la Complejidad de Decisiones**

La complejidad aumenta cuando las decisiones no son simples bifurcaciones. Exploraremos las condiciones anidadas, donde múltiples evaluaciones lógicas pueden determinar el rumbo del programa. Este enfoque nos permitirá construir lógica más sofisticada y manejar casos más complejos.

**Operadores Lógicos: Construyendo Puentes entre Condiciones**

En el corazón de nuestras decisiones se encuentran los operadores lógicos, como AND, OR y NOT. Estas herramientas nos permiten combinar condiciones de manera inteligente, abriendo la puerta a una toma de decisiones más flexible y potente en nuestros programas.

**Proyecto de Sección: Aplicando el Conocimiento en un Escenario Práctico**

Finalmente, consolidaremos nuestro aprendizaje aplicándolo a un proyecto concreto. Diseñaremos un programa que utilice operadores relacionales, condicionales, condiciones anidadas y operadores lógicos para resolver un problema específico. Esta experiencia práctica nos permitirá internalizar los conceptos aprendidos y fortalecer nuestras habilidades de programación.

¡Prepárense para explorar el emocionante mundo de la lógica y las condiciones en la programación!

---
## Operadores relacionales
Los operadores relacionales son utilizados para comparar dos valores y devolver un resultado booleano que indica si la relación entre ellos es verdadera o falsa. Aquí hay algunos operadores relacionales comunes:


### Operadores Relacionales:
Los operadores relacionales comparan dos valores y devuelven un resultado booleano.

```python
# Ejemplo de operadores relacionales
x = 15
y = 20
print(x == y)  # Igual a
print(x != y)  # No igual a
print(x < y)   # Menor que
print(x > y)   # Mayor que
print(x <= y)  # Menor o igual que
print(x >= y)  # Mayor o igual que
```

Puedes combinar expresiones aritméticas con operadores relacionales para realizar comparaciones más complejas. Por ejemplo:

```python
x = 10
y = 5
z = 3

resultado = (x + y) * z > x**2  # True
```

En este ejemplo, se realiza una operación aritmética `(x + y) * z` y luego se compara con `x**2`. El resultado final es `True` porque `(15) * 3` es mayor que `10**2`.

---
## Condicionales (if, else)
Los condicionales en programación, como "if" y "else", son estructuras de control que permiten tomar decisiones basadas en la evaluación de una condición. Estas estructuras permiten que un programa ejecute diferentes bloques de código según si una condición es verdadera o falsa. Aquí tienes una descripción detallada:

1. **if (si):**
   - La instrucción "if" se utiliza para evaluar una condición.
   - Si la condición es verdadera, el bloque de código dentro del "if" se ejecuta.
   - Si la condición es falsa, el bloque de código dentro del "if" se omite y el programa continúa con la siguiente instrucción.

   ```python
   if condicion:
       # Bloque de código si la condición es verdadera
   ```

2. **else (si no):**
   - La instrucción "else" se utiliza junto con "if" para especificar un bloque de código que se ejecutará si la condición en el "if" es falsa.
   - Solo se ejecutará uno de los bloques de código, ya sea el del "if" o el del "else".

   ```python
   if condicion:
       # Bloque de código si la condición es verdadera
   else:
       # Bloque de código si la condición es falsa
   ```

### Ejemplo de Aplicación: Detectar si un número es par o impar en Python

A continuación, te presento un ejemplo simple de cómo podrías usar condicionales en Python para crear una aplicación que determine si un número es par o impar:

```python
# Solicitar al usuario que ingrese un número
number = int(input("Ingrese un número: "))

# Verificar si el número es par o impar
if number % 2 == 0:
    print(f"El número {number} es par.")
else:
    print(f"El número {number} es impar.")
```

En este caso, la entrada del usuario se almacena en la variable `user_input`, y la condición se verifica directamente en el bloque de código sin la necesidad de una función adicional. El programa luego imprime un mensaje indicando si el número es par o impar.

---
## Condiciones anidadas
Las condiciones anidadas en programación son estructuras que permiten evaluar múltiples condiciones de manera jerárquica. En el ejemplo que proporcionaste, se están utilizando condiciones anidadas para determinar las propiedades de un número ingresado por el usuario. Vamos a analizar el código paso a paso:

1. **Entrada de datos:**
   ```python
   number = float(input("Enter a number: "))
   ```
   Aquí, el programa solicita al usuario ingresar un número, lo convierte a tipo float y lo asigna a la variable `numero`.

2. **Evaluación de condiciones anidadas:**
   ```python
    

    if number > 0:
        if number % 2 == 0:
            print("El número es positivo y par.")
        else:
            print("El número es positivo e impar.")
    elif number < 0:
        if number % 2 == 0:
            print("El número es negativo y par.")
        else:
            print("El número es negativo e impar.")
    else:
        print("El número es cero.")

   ```

   - Si `numero` es mayor que 0, se evalúa una segunda condición dentro de este bloque. Si `numero` es divisible por 2 (resto igual a 0), imprime "El número es positivo y par.", de lo contrario, imprime "El número es positivo e impar."
   - Si `numero` no es mayor que 0, se pasa a la siguiente condición (`elif`). Si `numero` es menor que 0, se evalúa una segunda condición dentro de este bloque. Si `numero` es divisible por 2, imprime "El número es negativo y par.", de lo contrario, imprime "El número es negativo e impar."
   - Si `numero` no es ni mayor que 0 ni menor que 0, significa que es igual a 0, y se imprime "El número es cero."

Este código es un ejemplo de cómo las condiciones anidadas pueden utilizarse para realizar una evaluación más detallada de las propiedades de un número. En resumen, se verifica si el número es positivo o negativo y, dentro de cada caso, se verifica si es par o impar.

---
## Operadores lógicos
Los operadores lógicos permiten combinar o modificar resultados booleanos y son útiles cuando deseas evaluar múltiples condiciones al mismo tiempo. Aquí están los operadores lógicos comunes:

1. **AND (`and`):** Devuelve `True` si ambas condiciones son verdaderas.
   ```python
   a = 5
   b = 7
   c = 10
   resultado = (a < b) and (b < c)  # Verdadero
   ```

2. **OR (`or`):** Devuelve `True` si al menos una de las condiciones es verdadera.
   ```python
   a = 5
   b = 7
   c = 3
   resultado = (a > b) or (b < c)  # Verdadero
   ```

3. **NOT (`not`):** Invierte el resultado booleano, convirtiendo `True` a `False` y viceversa.
   ```python
   a = 5
   b = 7
   resultado = not (a < b)  # Falso
   ```

Ahora, puedes combinar expresiones aritméticas, relacionales y lógicas para crear condiciones más complejas. Por ejemplo:

```python
x = 10
y = 5
z = 3

condicion = ((x + y) * z > x**2) and (y < z)  # Verdadero
```

En este ejemplo, se realiza una operación aritmética y una comparación relacional, y luego se combina con una condición adicional usando el operador lógico `and`. La variable `condicion` será `True` porque ambas condiciones son verdaderas. Puedes ajustar y combinar estas expresiones según las necesidades de tu programa.

---
## Proyecto de sección 

**Ejercicio: Sistema de Descuentos en un Restaurante**

Crea un programa en Python que simule un sistema de descuentos en un restaurante según el monto de consumo. El programa debe seguir las siguientes instrucciones:

1. Solicita al usuario que ingrese el monto de consumo en el restaurante.
2. Aplica descuentos según las siguientes reglas:
    - Si el monto de consumo es mayor a $50 pero igual o menor a $100, aplica un descuento del 10%.
    - Si el monto de consumo es mayor a $100 pero igual o menor a $200, aplica un descuento del 20%.
    - Si el monto de consumo es mayor a $200, aplica un descuento del 30%.
    - Si el monto de consumo es igual o menor a $50, no aplica ningún descuento.
3. Muestra al usuario un resumen de la cuenta con el monto de consumo, el descuento aplicado y el monto final con descuento.

**Código del proyecto**

```python
# Solicitar al usuario que ingrese el monto de consumo
total_amount = float(input("Ingrese el monto de consumo: $"))

# Calcular el descuento
if total_amount > 50 and total_amount <= 100:
    discount_percentage = 0.1
elif total_amount > 100 and total_amount <= 200:
    discount_percentage = 0.2
elif total_amount > 200:
    discount_percentage = 0.3
else:
    discount_percentage = 0.0

# Calcular el monto final con descuento
discount_amount = total_amount * discount_percentage
final_amount = total_amount - discount_amount

# Mostrar el resumen de la cuenta en español
print("\nResumen de la cuenta:")
print(f"Monto de consumo: ${total_amount:.2f}")
print(f"Descuento aplicado: {discount_percentage * 100:.0f}%")
print(f"Monto final con descuento: ${final_amount:.2f}")

```
---
## Resumen
En la sección dedicada a operadores lógicos y condicionales, exploramos las herramientas fundamentales de programación que nos permiten tomar decisiones dinámicas en el código. Comenzamos desentrañando los operadores relacionales, clave para comparar valores y establecer condiciones. Luego, nos sumergimos en la estructura "if, else" para dirigir el flujo del programa basado en condiciones específicas.

Abordamos la complejidad con condiciones anidadas, permitiendo múltiples evaluaciones lógicas para determinar el curso del programa. Los operadores lógicos, como AND, OR y NOT, fueron presentados como herramientas esenciales para combinar condiciones de manera inteligente.

Finalmente, aplicamos estos conceptos a un proyecto práctico, consolidando nuestro aprendizaje al resolver un problema específico mediante la aplicación de operadores relacionales, condicionales, condiciones anidadas y operadores lógicos. En resumen, exploramos y aplicamos de manera efectiva los fundamentos de la lógica y las condiciones en la programación.