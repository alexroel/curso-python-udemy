# Control de errores de Python


---
## Introdución


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


---
## Proyecto de sección



---
## Resumen