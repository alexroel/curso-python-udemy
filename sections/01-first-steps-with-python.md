# Primeros pasos con Python

1. [Introducción](#introducción)
2. [Instalación de Python](#instalación-de-python)
3. [Instalar Visual Studio Code](#instalación-de-visual-studio-code)
4. [Creación de la primera aplicación](#creación-de-la-primera-aplicación)
5. [Consola interactiva de Python](#consola-interactiva-de-python)
6. [Resumen](#resumen)

---
## Introducción
¡Bienvenido a la sección de "Primeros pasos con Python"! En este emocionante viaje, exploraremos los fundamentos esenciales para comenzar a programar en Python. En primer lugar, nos sumergiremos en la instalación de Python, la piedra angular de este lenguaje de programación versátil y poderoso.

A continuación, aprenderemos a configurar un entorno de desarrollo eficiente mediante la instalación de Visual Studio Code, una herramienta popular y amigable que potenciará nuestra experiencia de codificación.

Una vez que hayamos establecido nuestro entorno de trabajo, nos aventuraremos en la creación de nuestra primera aplicación en Python. Este paso inicial nos permitirá aplicar lo aprendido y comenzar a construir nuestro conocimiento práctico.

Además, exploraremos la consola interactiva de Python, una herramienta valiosa para probar y experimentar con código de manera rápida. ¡Prepárate para sumergirte en el fascinante mundo de Python y dar tus primeros pasos hacia el dominio de este lenguaje de programación!

---
## Instalación de Python

Antes de sumergirse en el emocionante mundo de la programación con Python, es fundamental asegurarse de tener correctamente instalada la versión adecuada del lenguaje. En esta guía paso a paso, exploraremos cómo validar la versión de Python existente en su sistema y cómo proceder con la instalación en caso de ser necesario.

**¿Cómo puedo saber si ya tengo instalado Python 3 en mi equipo?**

Es posible que Python 3 ya esté presente en su sistema, ya sea por instalación previa o como parte de alguna aplicación. Para verificarlo, siga las instrucciones según su sistema operativo.

### En Windows:

1. Abra la aplicación del símbolo del sistema seleccionando "Inicio" en la barra de tareas y buscando "cmd" en el cuadro de búsqueda. Seleccione la aplicación "Símbolo del sistema" en los resultados.

2. Escriba el siguiente comando y presione "Enter":

    ```bash
    python --version
    ```

    o

    ```bash
    py --version
    ```

    - Si obtiene la salida "Python X.X.X" (donde X.X.X es una serie de números), significa que ya tiene Python 3 instalado.

    - Si el primer número es 3, incluso si no tiene la versión más reciente, puede proceder con confianza. Si es 2 o recibe un mensaje de error, es necesario instalar Python 3.

### Instalar Python

Ahora, si determina que Python 3 no está instalado en su sistema o si necesita actualizarlo, siga estos pasos sencillos para instalar Python.

#### Paso 1: Descargar Python

Visite el [sitio oficial de Python](https://www.python.org/downloads/) y seleccione la versión más reciente de Python 3.x (donde x es la última subversión).

#### Paso 2: Iniciar el Instalador

Ejecute el archivo descargado para iniciar el instalador. Asegúrese de marcar la opción "Add Python X.X to PATH" durante el proceso de instalación, lo que facilitará la ejecución de Python desde la línea de comandos.

#### Paso 3: Configurar la Instalación

Seleccione las opciones de instalación según sus preferencias. Puede dejar las configuraciones predeterminadas en su mayoría, pero asegúrese de habilitar la opción "Add Python to PATH".

#### Paso 4: Completar la Instalación

Haga clic en "Install Now" y espere a que el instalador complete el proceso. Una vez finalizado, puede cerrar el instalador.

#### Paso 5: Verificar la Instalación

Abra una nueva ventana del símbolo del sistema y escriba:

```bash
python --version
```

o

```bash
py --version
```

Si ve la versión de Python, ¡felicidades! Ha instalado Python con éxito.

Con estos simples pasos, ahora está listo para sumergirse en el emocionante viaje de la programación con Python. ¡A programar!

---
## Instalar Visual Studio Code

### Herramientas para Escribir Código de Python

Antes de sumergirnos en el proceso de instalación de Visual Studio Code, es esencial comprender las herramientas necesarias para escribir código en Python. Un entorno de desarrollo integrado (IDE) como Visual Studio Code proporciona un conjunto de características que mejoran la productividad y hacen que la escritura de código sea más eficiente.

### Instalación de Visual Studio Code

Visual Studio Code es una herramienta gratuita y de código abierto que puede instalarse en diferentes sistemas operativos. A continuación, te guiamos a través del proceso de instalación paso a paso.

#### Paso 1: Descargar Visual Studio Code

Visita el [sitio oficial de Visual Studio Code](https://code.visualstudio.com/) y haz clic en el botón "Download" para obtener el instalador adecuado para tu sistema operativo.

#### Paso 2: Ejecutar el Instalador

Una vez completada la descarga, ejecuta el archivo descargado para iniciar el instalador. Sigue las instrucciones del asistente de instalación.

#### Paso 3: Configurar Opciones de Instalación

Durante la instalación, podrás personalizar algunas opciones según tus preferencias. Asegúrate de marcar la opción "Add to PATH" para facilitar el acceso desde la línea de comandos.

#### Paso 4: Instalación Completa

Haz clic en "Next" y luego en "Finish" para completar la instalación. Visual Studio Code estará listo para su uso.

### Extensiones: Python, Tokyo Night, Material Icon Theme

Una de las características poderosas de Visual Studio Code es su capacidad para admitir extensiones que personalizan y amplían sus funciones. Aquí te recomendamos algunas extensiones que mejorarán tu experiencia de desarrollo.

#### 1. Python

Para habilitar el soporte completo de Python en Visual Studio Code, instala la extensión oficial de Python. Abre Visual Studio Code, ve a la pestaña de Extensiones (puedes usar el atajo `Ctrl+Shift+X`), busca "Python" y selecciona la extensión proporcionada por Microsoft.

#### 2. Tokyo Night

Tokyo Night es un tema de color que agrega un toque estético a tu entorno de desarrollo. Instala esta extensión para cambiar la apariencia de Visual Studio Code. Ve a la pestaña de Extensiones, busca "Tokyo Night" y selecciona la extensión del tema.

#### 3. Material Icon Theme

Esta extensión agrega iconos a los archivos y carpetas en el explorador de Visual Studio Code, facilitando la identificación rápida de diferentes tipos de archivos. Instala la extensión "Material Icon Theme" para mejorar la visualización de tu proyecto.

### Resumen

Con Visual Studio Code instalado y configurado con estas extensiones, disfrutarás de un entorno de desarrollo personalizado y altamente funcional. El soporte total para Python y las mejoras visuales proporcionadas por los temas y los iconos mejorarán significativamente tu experiencia de codificación. ¡Ahora estás listo para escribir código de Python con estilo y eficiencia!

---
## Creación de la primera aplicación

**Creación de un espacio de trabajo ("workspace")**

Un espacio de trabajo es simplemente un directorio que contendrá tus proyectos. Puedes crear uno nuevo y navegar a él desde la terminal. Abre la terminal y ejecuta los siguientes comandos:

```bash
mkdir workspaces
cd workspaces
```

**Creación de un proyecto "hello-world"**

Dentro del espacio de trabajo, puedes crear un nuevo directorio para tu proyecto "hello-world". Ejecuta los siguientes comandos:

```bash
mkdir hello-world
cd hello-world
```

**Creación de un archivo con VSCode**

Abre Visual Studio Code en el directorio de tu proyecto con el comando:

```bash
code .
```

Esto abrirá VSCode en el directorio actual. Luego, crea un nuevo archivo llamado `hello.py` y añade el siguiente código simple de Python:

```python
print("¡Hola, mundo!")
```
- `print`: Es una función incorporada en Python que se utiliza para imprimir información en la consola.

- `("¡Hola, mundo!")`: Este es el argumento que se pasa a la función print. En este caso, es una cadena de texto (string) que contiene el mensaje que se imprimirá. La cadena de texto está delimitada por comillas dobles (") y contiene el mensaje "¡Hola, mundo!".

**Proyecto simple de Python**

Ahora, tienes una estructura básica de proyecto con un archivo Python simple.

```
workspaces/
|-- hello-world/
|   |-- hello.py
```

**Ejecución de la aplicación**

Vuelve a la terminal y asegúrate de estar en el directorio del proyecto "hello-world". Ejecuta el script Python con el siguiente comando:

```bash
python hello.py
```

Verás la salida en la consola:

```
¡Hola, mundo!
```

¡Listo! Has creado y ejecutado tu primera aplicación Python. Este es solo un ejemplo simple, pero puedes comenzar a construir proyectos más complejos a partir de aquí. ¡Diviértete programando en Python!

---
## Consola interactiva de Python
#### ¿Qué es?

La consola interactiva de Python, también conocida como el intérprete interactivo, es una interfaz de línea de comandos que permite a los usuarios interactuar directamente con el intérprete de Python. En lugar de escribir un programa completo en un archivo, puedes ingresar instrucciones una a una y obtener resultados inmediatos.

#### ¿Para qué se usa?

1. **Pruebas Rápidas:** Es útil para probar rápidamente fragmentos de código sin tener que escribir un programa completo.

2. **Aprendizaje y Experimentación:** Permite a los principiantes en Python experimentar y aprender de manera interactiva.

3. **Depuración:** Puede ser útil para depurar y entender el comportamiento de ciertos fragmentos de código.

4. **Exploración de Bibliotecas y Módulos:** Puedes probar funciones y métodos de bibliotecas directamente en la consola interactiva para entender cómo funcionan.

#### Ejemplos de uso básico:

**Operaciones Aritméticas:**
 
 Python incluye varios operadores aritméticos que te permiten realizar operaciones matemáticas básicas. Aquí están todos los operadores aritméticos en Python:

1. **Suma (+):**
   ```python
   resultado = 3 + 4
   ```

2. **Resta (-):**
   ```python
   resultado = 7 - 2
   ```

3. **Multiplicación (*):**
   ```python
   resultado = 5 * 6
   ```

4. **División (/):**
   ```python
   resultado = 8 / 2
   ```

5. **División Entera (//):**
   ```python
   resultado = 9 // 2
   ```

6. **Módulo (%):**
   ```python
   resultado = 11 % 3
   ```

7. **Potencia (**):**
   ```python
   resultado = 2 ** 3
   ```

Estos operadores aritméticos siguen las reglas matemáticas estándar. Algunas consideraciones adicionales:

- La división (`/`) siempre devuelve un número de punto flotante, incluso si ambos operandos son enteros. Si necesitas obtener un resultado entero, puedes usar la división entera (`//`).

- El operador de módulo (`%`) devuelve el resto de la división.

- El operador de potencia (`**`) eleva el primer operando a la potencia del segundo operando.

Recuerda que puedes salir de la consola interactiva escribiendo `exit()` o presionando `Ctrl + Z` seguido de `Enter` (en sistemas UNIX). La consola interactiva es una herramienta poderosa para aprender y experimentar con Python de manera rápida y sencilla.

---
## Resumen
En la sección de "Primeros pasos con Python", exploramos los fundamentos esenciales para iniciarse en la programación con este lenguaje. Comenzamos con la instalación de Python, la piedra angular de nuestro viaje. Luego, configuramos un entorno de desarrollo eficiente mediante la instalación de Visual Studio Code.

Con nuestro entorno listo, nos sumergimos en la creación de nuestra primera aplicación en Python, permitiéndonos aplicar de inmediato los conocimientos adquiridos. También exploramos la utilidad de la consola interactiva de Python, una herramienta valiosa para experimentar y probar código de manera rápida.

Así, dimos los primeros pasos en el fascinante mundo de Python, construyendo una base sólida para seguir explorando y dominando este poderoso lenguaje de programación.