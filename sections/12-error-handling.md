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
En Python, los errores se dividen principalmente en dos categorías: errores de sintaxis y excepciones. Aquí te proporciono una descripción de ambas:

1. **Errores de Sintaxis:**
   - *Descripción:* Los errores de sintaxis ocurren cuando el intérprete de Python no puede interpretar el código porque no sigue las reglas gramaticales del lenguaje. Estos errores se detectan durante la fase de análisis y previenen que el programa se ejecute.
   - *Ejemplo:*
     ```python
     print("Hola Mundo"  # Falta cerrar paréntesis
     ```

2. **Excepciones:**
   - *Descripción:* Las excepciones son eventos inesperados que ocurren durante la ejecución de un programa. A diferencia de los errores de sintaxis, las excepciones no impiden que el programa se ejecute por completo, pero deben ser manejadas para evitar que el programa termine abruptamente.
   - *Ejemplo:*
     ```python
     divisor = 0
     resultado = 10 / divisor  # Generará un ZeroDivisionError
     ```

   Algunas excepciones comunes en Python incluyen:
   - `ZeroDivisionError`: Ocurre cuando intentas dividir por cero.
   - `TypeError`: Se produce cuando hay un error en el tipo de datos (por ejemplo, operaciones no válidas entre tipos).
   - `ValueError`: Sucede cuando una función recibe un argumento con un valor inapropiado.
   - `FileNotFoundError`: Se produce cuando intentas abrir un archivo que no existe.

Además de estas, Python tiene una amplia variedad de excepciones integradas, y los desarrolladores también pueden definir sus propias excepciones personalizadas.

```python
# Entrada de datos 
a = int(input('Ingrese un número entero: '))
b = int(input('Ingrese un número entero: '))

# Proceso

d = a / b

# Salida 
print(f"División entre {a}/{b} = {d}")
```

Es importante comprender la diferencia entre errores de sintaxis y excepciones, ya que el manejo adecuado de excepciones es esencial para crear programas robustos y prevenir la terminación inesperada debido a situaciones excepcionales durante la ejecución.

---
## Control de Excepciones
El control de excepciones en Python se refiere a la práctica de manejar situaciones excepcionales durante la ejecución de un programa para evitar que este se detenga de manera abrupta. Aquí hay algunas estrategias y elementos clave relacionados con el control de excepciones en Python:

1. **Bloque try-except:**
   - **Descripción:** El bloque `try` se utiliza para envolver un conjunto de instrucciones donde se espera que ocurran excepciones. Si se produce una excepción dentro del bloque `try`, el control se transfiere al bloque `except` correspondiente.
   - **Ejemplo:**
     ```python
        # Entrada de datos
        try:
            a = int(input('Ingrese un número entero: '))
            b = int(input('Ingrese un número entero diferente de cero: '))

            # Proceso
            resultado = a / b

            # Salida
            print(f"División entre {a}/{b} = {resultado}")

        except ValueError:
            print("Error: Ingrese un número entero válido.")
        except ZeroDivisionError:
            print("Error: El segundo número no puede ser cero.")
     ```

2. **Cláusula else en bloques try-except:**
   - **Descripción:** La cláusula `else` se utiliza para especificar un conjunto de instrucciones que se ejecutarán solo si no se produce ninguna excepción dentro del bloque `try`. Esto permite separar el código propenso a errores del código que debe ejecutarse en condiciones normales.
   - **Ejemplo:**
     ```python
     # Entrada de datos
    try:
        a = int(input('Ingrese un número entero: '))
        b = int(input('Ingrese un número entero: '))

        # Proceso
        resultado = a / b

    except ValueError:
        print("Error: Ingrese un número entero válido.")
    except ZeroDivisionError:
        print("Error: El segundo número no puede ser cero.")
    else:
        # Salida
        print(f"División entre {a}/{b} = {resultado}")


     ```

3. **Utilización de la cláusula `as` en la declaración `except`:**
   - **Descripción:** La cláusula `as` se utiliza para asignar la excepción capturada a una variable, permitiendo acceder a información más detallada sobre la excepción.
   - **Ejemplo:**
     ```python
     # Entrada de datos
    try:
        a = int(input('Ingrese un número entero: '))
        b = int(input('Ingrese un número entero: '))

        # Proceso
        resultado = a / b

        # Salida
        print(f"División entre {a}/{b} = {resultado}")

    except ValueError:
        print("Error: Ingrese un número entero válido.")
    except ZeroDivisionError:
        print("Error: El segundo número no puede ser cero.")
    except Exception as e:
        print(f"Error inesperado: {e}")
     ```

Al emplear estas técnicas, puedes escribir programas más robustos que manejen errores de manera controlada y, al mismo tiempo, faciliten la depuración y el mantenimiento del código.

---
## Generación de excepciones
Ahora que has adquirido una buena comprensión de los seguimientos y el control de excepciones, exploraremos la generación de excepciones en Python. En situaciones en las que ya identificas condiciones de error mientras escribes código, generar excepciones puede resultar útil para que otros fragmentos de código comprendan el problema.

La generación de excepciones no solo ayuda a señalar errores, sino que también facilita la toma de decisiones en otros fragmentos de código. Como vimos anteriormente, según el tipo de error, el código puede tomar decisiones inteligentes para resolver, solucionar o ignorar un problema.

Tomemos el ejemplo de astronautas que limitan su consumo de agua a unos 11 litros al día. Vamos a crear una función que, en función del número de astronautas, calcule la cantidad de agua que quedará después de un día o más:

```python
def agua_restante(astronautas, agua_restante, dias_restantes):
    consumo_diario = astronautas * 11
    consumo_total = consumo_diario * dias_restantes
    agua_total_restante = agua_restante - consumo_total
    return f"El total de agua restante después de {dias_restantes} días es: {agua_total_restante} litros"
```

Probemos la función con cinco astronautas, 100 litros de agua restante y dos días:

```python
agua_restante(5, 100, 2)
```

Obtenemos un resultado negativo: `'El total de agua restante después de 2 días es: -10 litros'`. Esto no es útil, ya que una cantidad negativa de litros sería un error. El sistema de navegación podría alertar a los astronautas de que no habrá suficiente agua para todos en dos días. Si eres un ingeniero que programa el sistema de navegación, podrías generar una excepción en la función `agua_restante()` para alertar sobre la condición de error:

```python
def agua_restante(astronautas, agua_restante, dias_restantes):
    consumo_diario = astronautas * 11
    consumo_total = consumo_diario * dias_restantes
    agua_total_restante = agua_restante - consumo_total
    if agua_total_restante < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} astronautas después de {dias_restantes} días.")
    return f"El total de agua restante después de {dias_restantes} días es: {agua_total_restante} litros"
```

Al ejecutar la función nuevamente:

```python
agua_restante(5, 100, 2)
```

Obtenemos un rastro de excepción:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in agua_restante
RuntimeError: No hay suficiente agua para 5 astronautas después de 2 días.
```

En el sistema de navegación, el código para señalar la alerta ahora puede usar `RuntimeError` para generar la alerta:

```python
try:
    agua_restante(5, 100, 2)
except RuntimeError as err:
    alertar_sistema_navegacion(err)
```

La función `agua_restante()` también se puede actualizar para evitar el paso de tipos no admitidos. Intentemos pasar argumentos que no sean enteros para comprobar la salida de error:

```python
agua_restante("3", "200", None)
```

Obtenemos un mensaje de error más descriptivo:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in agua_restante
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

El error de `TypeError` no es muy descriptivo en el contexto de lo que espera la función. Actualicemos la función para utilizar `TypeError`, pero con un mensaje mejor:

```python
def agua_restante(astronautas, agua_restante, dias_restantes):
    for argumento in [astronautas, agua_restante, dias_restantes]:
        try:
            argumento / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser del tipo int, pero se recibió: '{argumento}'")
    consumo_diario = astronautas * 11
    consumo_total = consumo_diario * dias_restantes
    agua_total_restante = agua_restante - consumo_total
    if agua_total_restante < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronautas} astronautas después de {dias_restantes} días.")
    return f"El total de agua restante después de {dias_restantes} días es: {agua_total_restante} litros"
```

Ahora, al intentar nuevamente obtener un error:

```python
agua_restante("3", "200", None)
```

Obtenemos un mensaje de error más claro:

```python
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
  File "<stdin>", line 9, in agua_restante
TypeError: Todos los argumentos deben ser del tipo int, pero se recibió: '3'
```

En resumen, la generación de excepciones es una herramienta poderosa en Python para mejorar la claridad y la robustez del código. Utilizar excepciones de manera estratégica no solo ayuda a identificar y manejar errores, sino que también facilita la comprensión y el mantenimiento del código.

---
## Manejo de archivos

El manejo de archivos en Python es una tarea fundamental en el desarrollo de aplicaciones. Python proporciona funciones y métodos integrados que facilitan la lectura, escritura y manipulación de archivos. A continuación, te proporcionaré una introducción básica al manejo de archivos en Python.

### Lectura de Archivos

Para leer un archivo en Python, puedes utilizar la función `open()` para abrir el archivo y luego usar el método `read()` para leer su contenido. Aquí hay un ejemplo:

```python
# Abrir un archivo en modo de lectura
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
```

En este ejemplo, se abre el archivo `archivo.txt` en modo de lectura (`'r'`). La instrucción `with` asegura que el archivo se cierre automáticamente después de su uso.

### Escritura en Archivos

Para escribir en un archivo, puedes utilizar la función `open()` con el modo de escritura (`'w'`). Aquí hay un ejemplo:

```python
# Abrir un archivo en modo de escritura
with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write('Hola, este es un nuevo archivo.\n')
    archivo.write('¡Aprender Python es divertido!')
```

En este caso, se crea un nuevo archivo llamado `nuevo_archivo.txt` y se escribe contenido en él.

### Operaciones Adicionales

Además de leer y escribir, Python proporciona otras operaciones útiles para el manejo de archivos. Algunas de ellas son:

- **Lectura de líneas**: Puedes utilizar el método `readline()` para leer una línea a la vez.
  ```python
  with open('archivo.txt', 'r') as archivo:
      linea = archivo.readline()
      while linea:
          print(linea)
          linea = archivo.readline()
  ```

- **Lectura de todas las líneas como lista**: Puedes utilizar el método `readlines()` para leer todas las líneas y almacenarlas en una lista.
  ```python
  with open('archivo.txt', 'r') as archivo:
      lineas = archivo.readlines()
      for linea in lineas:
          print(linea)
  ```

- **Iteración directa sobre el archivo**: Puedes iterar directamente sobre las líneas de un archivo utilizando un bucle `for`.
  ```python
  with open('archivo.txt', 'r') as archivo:
      for linea in archivo:
          print(linea)
  ```

### Manejo de Errores

Es importante manejar posibles errores al trabajar con archivos, como la posibilidad de que el archivo no exista o que no tengas permisos para leerlo o escribirlo. Puedes hacer esto utilizando bloques `try` y `except`. Por ejemplo:

```python
try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
except Exception as e:
    print(f"Se produjo un error: {e}")
```

Esto garantiza que tu programa maneje los posibles errores de manera elegante.

Recuerda que el manejo de archivos puede variar según los requisitos específicos de tu aplicación. A medida que te familiarices más con Python, podrás utilizar módulos adicionales y técnicas avanzadas para trabajar con archivos de manera más eficiente y flexible.


---
## Resumen
En la sección dedicada al Control de Errores en Python, exploramos diversos aspectos fundamentales para gestionar situaciones imprevistas y mejorar la robustez de nuestros programas. Se abordaron los siguientes temas:

**Tipos de Errores:**
Antes de abordar el manejo de errores, fue esencial comprender los diferentes tipos de errores que podían surgir en un programa. Python clasifica los errores en varias categorías, desde errores de sintaxis hasta errores de tiempo de ejecución.

**Control de Excepciones:**
Python utiliza bloques `try` y `except` para gestionar excepciones de manera eficiente. Aprendimos a utilizar esta estructura para capturar y manejar errores, permitiendo que el programa continuara ejecutándose incluso cuando se enfrentaba a condiciones excepcionales.

**Generación de Excepciones:**
En algunos casos, fue necesario generar excepciones de forma deliberada para señalar condiciones de error específicas. Exploramos cómo crear y lanzar excepciones personalizadas, proporcionando mensajes significativos para facilitar la identificación y resolución de problemas en el código.

**Manejo de Archivos:**
El manejo de archivos, una tarea común en la programación, fue abordado. Aprendimos a abrir archivos, leer su contenido y escribir en ellos utilizando las funciones y métodos integrados de Python. Además, exploramos las mejores prácticas para garantizar la correcta gestión de recursos al trabajar con archivos.

Al abordar estos aspectos, fortalecimos nuestras habilidades en el control de errores, mejorando la calidad y la confiabilidad de nuestros programas. Nos sumergimos en el fascinante mundo del control de errores en Python.