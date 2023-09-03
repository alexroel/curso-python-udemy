# Variables y datos

## Variables
En programación, una variable es un espacio de memoria reservado para almacenar datos, como números, cadenas de texto, objetos u otro tipo de información. Las variables permiten que los programas almacenen y manipulen datos de manera dinámica en tiempo de ejecución.

En Python, las variables son identificadores que se utilizan para almacenar y acceder a datos. Cada variable tiene un nombre único que se utiliza para referirse a ella en el código. Aquí tienes cómo se ve una variable en Python y algunas reglas de nomenclatura:

```python
nombre_variable = valor
```

- `nombre_variable`: Es el nombre que eliges para tu variable. Debe seguir ciertas reglas de nomenclatura.
- `=`: Es el operador de asignación que se utiliza para asignar un valor a la variable.
- `valor`: Es el dato que deseas almacenar en la variable.

**Reglas de nomenclatura para variables en Python:**

1. Los nombres de las variables deben comenzar con una letra (a-z, A-Z) o un guión bajo (_).
2. Después del primer carácter, los nombres de las variables pueden contener letras, números y guiones bajos.
3. Los nombres de las variables distinguen entre mayúsculas y minúsculas. Esto significa que `mi_variable` y `Mi_Variable` son considerados nombres diferentes.
4. No se pueden utilizar palabras clave reservadas de Python como nombres de variables. Ejemplos de palabras clave son `if`, `else`, `while`, `for`, `def`, etc.
5. Es buena práctica utilizar nombres descriptivos para tus variables para que el código sea más legible.

Ejemplos de nombres de variables válidos:
```python
edad = 25
nombre_completo = "Juan Pérez"
saldo_cuenta = 1000.50
total_productos = 10
```

Recuerda que la elección de nombres de variables debe ser significativa y seguir convenciones de estilo para hacer tu código más legible y mantenible. Por ejemplo, PEP 8 es la guía de estilo de código recomendada para Python y ofrece pautas sobre cómo nombrar variables y otras convenciones de codificación.

---
## Tipos de datos
En Python, como en muchos lenguajes de programación, existen varios tipos de datos que se utilizan para representar diferentes tipos de información. Aquí están los tipos de datos básicos en Python:

1. **Enteros (`int`):** Representan números enteros, como 1, -5, 100, etc.

2. **Punto Flotante (`float`):** Representan números con decimales, como 3.14, -0.5, 2.0, etc.

3. **Cadenas de Texto (`str`):** Representan secuencias de caracteres. Se crean utilizando comillas simples ('...') o comillas dobles ("...").

4. **Booleanos (`bool`):** Representan los valores de verdad, que pueden ser `True` (verdadero) o `False` (falso). Son esenciales para la lógica y el control de flujo.

5. **Listas (`list`):** Son colecciones ordenadas y modificables de elementos. Los elementos pueden ser de diferentes tipos.

6. **Tuplas (`tuple`):** Son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de la creación.

7. **Diccionarios (`dict`):** Son colecciones de pares clave-valor. Las claves son únicas y se utilizan para acceder a los valores asociados.

8. **Conjuntos (`set`):** Son colecciones no ordenadas de elementos únicos. Se utilizan para realizar operaciones matemáticas de conjuntos.

9. **Ninguno (`NoneType`):** Representa la ausencia de valor. Se utiliza en situaciones en las que una variable no tiene un valor asignado.

10. **Bytes (`bytes`) y Bytesarray (`bytearray`):** Representan secuencias de bytes utilizados para manipular datos binarios.

11. **Rango (`range`):** Representa una secuencia inmutable de números enteros.

12. **Objetos (`object`):** Todos los tipos de datos en Python son objetos, incluyendo tipos internos y definidos por el usuario.

Estos son los tipos de datos más básicos en Python. Cada tipo de dato tiene sus propias características y métodos asociados. Python es un lenguaje de programación de tipado dinámico, lo que significa que no es necesario declarar explícitamente el tipo de dato de una variable; Python determinará el tipo en función del valor asignado.

---
## Operadores y expresiones
Los operadores y expresiones son componentes esenciales en la programación, ya que te permiten realizar cálculos, combinar valores y tomar decisiones. En Python, existen varios tipos de operadores y formas de construir expresiones. Aquí te proporciono una descripción general de los operadores y las expresiones en Python:

**Operadores Aritméticos:**
- `+` : Suma
- `-` : Resta
- `*` : Multiplicación
- `/` : División (siempre devuelve un valor de punto flotante)
- `//` : División entera (descarta la parte decimal)
- `%` : Módulo (devuelve el residuo de la división)
- `**` : Exponenciación

**Operadores de Comparación:**
- `==` : Igual a
- `!=` : No igual a
- `<` : Menor que
- `>` : Mayor que
- `<=` : Menor o igual que
- `>=` : Mayor o igual que

**Operadores Lógicos:**
- `and` : Operador lógico AND
- `or` : Operador lógico OR
- `not` : Operador lógico NOT

**Operadores de Asignación:**
- `=` : Asignación
- `+=` : Asignación con suma (puedes hacer lo mismo con otros operadores aritméticos)
- `-=` : Asignación con resta
- `*=` : Asignación con multiplicación
- `/=` : Asignación con división
- `//=`, `%=`, `**=` : Asignación con otros operadores

**Expresiones:**
Una expresión es una combinación de valores, variables y operadores que se evalúa y produce un resultado. Por ejemplo:
```python
a = 10
b = 5

a * b - 2**b >= 20 and not (a % b) != 0 # False
```

**Operadores de Concatenación y Repetición:**
- `+` : Concatenación de cadenas
- `*` : Repetición de cadenas

**Operadores de Pertenencia:**
- `in` : Verifica si un valor está en una secuencia
- `not in` : Verifica si un valor no está en una secuencia

**Operadores de Identidad:**
- `is` : Verifica si dos objetos son el mismo objeto en memoria
- `is not` : Verifica si dos objetos no son el mismo objeto en memoria

Estos son solo algunos de los operadores en Python. Las expresiones pueden combinarse de diversas maneras, y el uso de operadores y expresiones es fundamental para realizar cálculos y tomar decisiones en tus programas.

---
## Salida y entrada de datos
La entrada y salida de datos son componentes esenciales en la programación, ya que permiten que un programa interactúe con el usuario y con otros sistemas. En Python, hay varias formas de realizar entrada y salida de datos. A continuación, te mostraré algunas de las formas más comunes de hacerlo:

### Salida de datos:

1. **Función `print()`**: La función `print()` se utiliza para mostrar información en la consola.

```python
print("Hola, mundo!")
```

2. **Formateo de cadenas**: Puedes utilizar f-strings (format strings) o el método `format()` para insertar valores en cadenas de texto formateadas.

```python
nombre = "Juan"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")
```

```python
nombre = "María"
edad = 25
print("Mi nombre es {} y tengo {} años.".format(nombre, edad))
```

### Caracteres especiales
En Python y muchos otros lenguajes de programación, los caracteres especiales son secuencias de caracteres que representan caracteres no imprimibles o que tienen un significado especial en una cadena de texto. Aquí tienes una lista de algunos caracteres especiales comunes en Python:

1. **`\n`**: Representa un salto de línea. Se utiliza para crear una nueva línea en una cadena de texto o en la salida de datos.

```python
print("Línea 1\nLínea 2")
```

Esto producirá la siguiente salida:

```
Línea 1
Línea 2
```

2. **`\t`**: Representa un tabulador. Se utiliza para insertar un espacio en blanco equivalente a un tabulador en una cadena de texto.

```python
print("Columna1\tColumna2")
```

Esto producirá la siguiente salida:

```
Columna1    Columna2
```

3. **`\\`**: Representa una barra invertida literal. Si deseas incluir una barra invertida en una cadena sin que se interprete como un carácter de escape, debes usar `\\`.

```python
print("C:\\Directorio\\Archivo")
```

Esto producirá la siguiente salida:

```
C:\Directorio\Archivo
```

4. **`\"` y `\'`**: Representan comillas dobles y comillas simples dentro de una cadena del mismo tipo.

```python
print("Esto es una cadena con comillas \"dobles\"")
print('Esto es una cadena con comillas simples \'simples\'')
```

Esto producirá la siguiente salida:

```
Esto es una cadena con comillas "dobles"
Esto es una cadena con comillas simples 'simples'
```

5. **`\r`**: Representa un retorno de carro. A menudo se usa junto con `\n` para manejar saltos de línea en sistemas que utilizan retornos de carro y avance de línea (por ejemplo, en archivos de texto).

Estos son algunos ejemplos de caracteres especiales comunes en Python, pero hay otros caracteres de escape que puedes usar para diversos fines. Puedes combinar estos caracteres especiales según tus necesidades para formatear cadenas de texto o manipular la salida de datos de la manera deseada.

### Entrada de datos:

1. **Función `input()`**: La función `input()` permite al usuario introducir datos desde la consola. Ten en cuenta que los datos introducidos se almacenan como cadenas.

```python
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}!")
```

2. **Conversión de tipos**: Si necesitas trabajar con tipos de datos diferentes, como números enteros o flotantes, debes convertir los datos ingresados utilizando las funciones `int()` o `float()`.

```python
edad_str = input("Por favor, ingresa tu edad: ")
edad = int(edad_str)
print(f"Tienes {edad} años.")
```

Estas son algunas de las formas más comunes de realizar entrada y salida de datos en Python. Puedes adaptar estas técnicas según tus necesidades específicas en tus programas.