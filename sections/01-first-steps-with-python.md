# Primeros pasos con Python

1. [Introducción](#introducción)
2. [¿Qué es Python?](#¿qué-es-python?)
3. [Instalación de Python](#instalación-de-python)
4. [Consola interactiva de Python](#consola-interactiva-de-python)
5. [Instalar Visual Studio Code](#instalación-de-visual-studio-code)
6. [Creación de la primera aplicación](#creación-de-la-primera-aplicación)
7. [Sintaxis y semántica de Python](#sintaxis-y-semántica-de-python)
8. [Resumen](#resumen)

---
## Introducción

Bienvenido a la sección "Primeros pasos con Python". En esta etapa, exploraremos los fundamentos esenciales para iniciarte en el fascinante mundo de la programación con Python. Este lenguaje se ha destacado como uno de los más populares y de mayor crecimiento en el ámbito mundial. Su versatilidad lo ha convertido en una herramienta fundamental para diversas tareas, desde el desarrollo web hasta el análisis de datos, e incluso en el campo del aprendizaje automático.

**Razones para Aprender Python**

La creciente demanda de desarrolladores de Python y las oportunidades lucrativas en trabajos de programación son solo algunas de las razones que hacen que aprender Python sea una elección inteligente. Este módulo te proporcionará una introducción práctica al uso de Python para la creación de aplicaciones, sirviendo como un sólido punto de partida para tu camino hacia la programación en Python.

**Objetivos de Aprendizaje**

En esta sección, nos enfocaremos en:

- **¿Qué es Python?** Explora las características clave que hacen a Python único y poderoso.
- **Instalación de Python:** Aprende a instalar Python en tu sistema para comenzar a programar rápidamente.
- **Consola interactiva de Python:** Explora un espacio interactivo para experimentar y probar tu código.
- **Instalar Visual Studio Code:** Descubre cómo configurar este entorno de desarrollo popular y versátil.
- **Creación de la primera aplicación:** Guía paso a paso para crear tu primera aplicación en Python, estableciendo una base sólida.
- **Sintaxis y semántica de Python:** La sintaxis y la semántica son dos aspectos clave en cualquier lenguaje de programación, incluido Python.

Estamos emocionados de acompañarte en este viaje de descubrimiento y aprendizaje. ¡Vamos a sumergirnos en el mundo de Python y comenzar a construir juntos!


---
## ¿Qué es Python?

Python es uno de los lenguajes de programación más populares del mundo, con su origen a principios de la década de los 90. Este lenguaje se destaca por su versatilidad, utilizado desde la automatización de tareas repetitivas hasta la implementación de complejos modelos de Machine Learning y redes neuronales. La comunidad de investigadores, matemáticos y, especialmente, científicos de datos, aprecian Python debido a su sintaxis completa y fácil de entender, así como a la extensa gama de paquetes de código abierto disponibles. Estos paquetes son bibliotecas compartidas que están disponibles de forma gratuita para todos los usuarios.

Python se caracteriza por una sintaxis sencilla y fácil de aprender, enfatizando la legibilidad del código. Las aplicaciones escritas en Python son compatibles con una amplia variedad de sistemas operativos, como Windows, macOS y diversas distribuciones de Linux. Además, el ecosistema de Python incluye un conjunto diverso de herramientas de desarrollo que facilitan la escritura, depuración y publicación de aplicaciones en este lenguaje.

Finalmente, Python cuenta con el respaldo de una comunidad activa de usuarios dispuestos a ayudar a los programadores nuevos, guiándolos no solo hacia la sintaxis correcta, sino también hacia el uso efectivo del lenguaje para alcanzar sus objetivos.

**Diferencia entre Compilado e Interpretado**

Antes de explorar la ejecución de código en Python, es crucial comprender la diferencia entre lenguajes compilados e interpretados:

- **Lenguajes Compilados:** En estos lenguajes, el código fuente se traduce completamente a un código ejecutable antes de la ejecución. Este proceso se llama compilación y produce un archivo binario independiente que se ejecuta directamente por la máquina. Ejemplos comunes de lenguajes compilados son C y C++.

- **Lenguajes Interpretados:** En cambio, los lenguajes interpretados no se traducen completamente antes de la ejecución. El intérprete procesa el código línea por línea durante la ejecución del programa. Esto significa que no hay un paso de compilación previo a la ejecución del código fuente. Python es un ejemplo de lenguaje interpretado.

**Ejecución de código en Python**

Python es un lenguaje interpretado, lo que reduce el ciclo de editar-probar-depurar ya que no requiere un paso de compilación. Para ejecutar aplicaciones de Python, solo se necesita un entorno o intérprete de runtime para ejecutar el código.

La ejecución de código Python se puede realizar de dos maneras principales:

- **Modo interactivo:** Cada comando se interpreta y ejecuta inmediatamente, mostrando los resultados en cada presión de la tecla "Enter". Este es el modo predeterminado si no se especifica un nombre de archivo al intérprete.

- **Modo de script:** Se coloca un conjunto de instrucciones de Python en un archivo de texto con extensión .py. Luego, el intérprete de Python se ejecuta apuntando al archivo, ejecutando el programa línea por línea y mostrando la salida.

**Ejemplo de ejecución:**
```python
# Código fuente en hola.py
print("¡Hola Mundo!")

# Intérprete de Python interpreta 

# Resultado de la salida 
¡Hola Mundo!
```

**Nota:**
La mayoría de las implementaciones de Python compilan scripts parcialmente, convirtiendo el código fuente en código byte que se puede ejecutar en cualquier plataforma compatible. Esta compilación parcial se realiza automáticamente para mejorar el rendimiento de ejecuciones posteriores del script. También es posible generar una versión "compilada" del script para distribuir una aplicación sin proporcionar el código fuente completo.

**Implementaciones de Python**

Python se distribuye bajo la licencia de código abierto OSI (Esta licencia garantiza que cualquier persona pueda utilizar, modificar y distribuir Python libremente), y existen varias implementaciones disponibles según las necesidades. Algunas opciones incluyen:

- **CPython, la implementación de referencia:** Esta es la implementación más popular, utilizada para desarrollo web, creación de aplicaciones y scripting. CPython está disponible para Windows y macOS, y en Linux se puede instalar a través de administradores de paquetes como apt, yum y Zypper. También se puede probar en línea mediante una área de juegos y se proporciona el código fuente completo para compilación personalizada.

- **Anaconda:** Una distribución especializada de Python para tareas científicas como ciencia de datos y aprendizaje automático.

- **IronPython:** Una implementación de código abierto de Python compilada en el runtime de .NET.

- **Jupyter Notebook:** Un entorno de programación interactivo basado en web compatible con varios lenguajes, incluido Python. Ampliamente utilizado en investigación, enseñanza y aprendizaje de programación.

---
## Instalación de Python

Antes de sumergirse en el emocionante mundo de la programación con Python, es fundamental asegurarse de tener correctamente instalada la versión adecuada del lenguaje. En esta guía paso a paso, exploraremos cómo validar la versión de Python existente en su sistema y cómo proceder con la instalación en caso de ser necesario.

**¿Cómo puedo saber si ya tengo instalado Python 3 en mi equipo?**

Es posible que Python 3 ya esté presente en su sistema, ya sea por instalación previa o como parte de alguna aplicación. Para verificarlo, siga las instrucciones según su sistema operativo.

**En Windows:**

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

**Instalar Python**

Ahora, si determina que Python 3 no está instalado en su sistema o si necesita actualizarlo, siga estos pasos sencillos para instalar Python.

**Paso 1: Descargar Python**

Visite el [sitio oficial de Python](https://www.python.org/downloads/) y seleccione la versión más reciente de Python 3.x (donde x es la última subversión).

**Paso 2: Iniciar el Instalador**

Ejecute el archivo descargado para iniciar el instalador. Asegúrese de marcar la opción "Add Python X.X to PATH" durante el proceso de instalación, lo que facilitará la ejecución de Python desde la línea de comandos.

**Paso 3: Configurar la Instalación**

Seleccione las opciones de instalación según sus preferencias. Puede dejar las configuraciones predeterminadas en su mayoría, pero asegúrese de habilitar la opción "Add Python to PATH".

**Paso 4: Completar la Instalación**

Haga clic en "Install Now" y espere a que el instalador complete el proceso. Una vez finalizado, puede cerrar el instalador.

**Paso 5: Verificar la Instalación**

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
## Consola interactiva de Python
**¿Qué es?**

La consola interactiva de Python, también conocida como el intérprete interactivo, es una interfaz de línea de comandos que permite a los usuarios interactuar directamente con el intérprete de Python. En lugar de escribir un programa completo en un archivo, puedes ingresar instrucciones una a una y obtener resultados inmediatos.

**¿Para qué se usa?**

1. **Pruebas Rápidas:** Es útil para probar rápidamente fragmentos de código sin tener que escribir un programa completo.

2. **Aprendizaje y Experimentación:** Permite a los principiantes en Python experimentar y aprender de manera interactiva.

3. **Depuración:** Puede ser útil para depurar y entender el comportamiento de ciertos fragmentos de código.

4. **Exploración de Bibliotecas y Módulos:** Puedes probar funciones y métodos de bibliotecas directamente en la consola interactiva para entender cómo funcionan.

**Ejemplos de uso básico:**

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
## Instalar Visual Studio Code

**Herramientas para Escribir Código de Python**

Antes de sumergirnos en el proceso de instalación de Visual Studio Code, es esencial comprender las herramientas necesarias para escribir código en Python. Un entorno de desarrollo integrado (IDE) como Visual Studio Code proporciona un conjunto de características que mejoran la productividad y hacen que la escritura de código sea más eficiente.

**Instalación de Visual Studio Code**

Visual Studio Code es una herramienta gratuita y de código abierto que puede instalarse en diferentes sistemas operativos. A continuación, te guiamos a través del proceso de instalación paso a paso.

**Paso 1: Descargar Visual Studio Code**

Visita el [sitio oficial de Visual Studio Code](https://code.visualstudio.com/) y haz clic en el botón "Download" para obtener el instalador adecuado para tu sistema operativo.

**Paso 2: Ejecutar el Instalador**

Una vez completada la descarga, ejecuta el archivo descargado para iniciar el instalador. Sigue las instrucciones del asistente de instalación.

**Paso 3: Configurar Opciones de Instalación**

Durante la instalación, podrás personalizar algunas opciones según tus preferencias. Asegúrate de marcar la opción "Add to PATH" para facilitar el acceso desde la línea de comandos.

**Paso 4: Instalación Completa**

Haz clic en "Next" y luego en "Finish" para completar la instalación. Visual Studio Code estará listo para su uso.

**Extensiones: Python, Tokyo Night, Symbols**

Una de las características poderosas de Visual Studio Code es su capacidad para admitir extensiones que personalizan y amplían sus funciones. Aquí te recomendamos algunas extensiones que mejorarán tu experiencia de desarrollo.

**1. Python:** Para habilitar el soporte completo de Python en Visual Studio Code
**2. One Dark Theme:** One Dark Theme es un tema de color que agrega un toque estético a tu entorno de desarrollo.
**3. Fluent Icons y Symbols:** Esta extensión agrega iconos a los archivos y carpetas en el explorador de Visual Studio Code

Con Visual Studio Code instalado y configurado con estas extensiones, disfrutarás de un entorno de desarrollo personalizado y altamente funcional. El soporte total para Python y las mejoras visuales proporcionadas por los temas y los iconos mejorarán significativamente tu experiencia de codificación. ¡Ahora estás listo para escribir código de Python con estilo y eficiencia!


---
## Creación de la primera aplicación

**Creación de un espacio de trabajo ("workspace")**

Un espacio de trabajo es simplemente un directorio que contendrá tus proyectos. Puedes crear uno nuevo y navegar a él desde la terminal. Abre la terminal y ejecuta los siguientes comandos:

```bash
mkdir curso-python
cd curso-python
```

**Creación de un proyecto "hola-mundo"**

Dentro del espacio de trabajo, puedes crear un nuevo directorio para tu proyecto "hola-mundo". Ejecuta los siguientes comandos:

```bash
mkdir hola-mundo
cd hola-mundo
```

**Creación de un archivo con VSCode**

Abre Visual Studio Code en el directorio de tu proyecto con el comando:

```bash
code .
```

Esto abrirá VSCode en el directorio actual. Luego, crea un nuevo archivo llamado `hola.py` y añade el siguiente código simple de Python:

```python
print("¡Hola, mundo!")
```
- `print`: Es una función incorporada en Python que se utiliza para imprimir información en la consola.

- `("¡Hola, mundo!")`: Este es el argumento que se pasa a la función print. En este caso, es una cadena de texto (string) que contiene el mensaje que se imprimirá. La cadena de texto está delimitada por comillas dobles (") y contiene el mensaje "¡Hola, mundo!".

**Proyecto simple de Python**

Ahora, tienes una estructura básica de proyecto con un archivo Python simple.

```
workspaces/
|-- hola-mundo/
|   |-- hola.py
```

**Ejecución de la aplicación**

Vuelve a la terminal y asegúrate de estar en el directorio del proyecto "hola-mundo". Ejecuta el script Python con el siguiente comando:

```bash
python hola.py
```

Verás la salida en la consola:

```
¡Hola, mundo!
```

¡Listo! Has creado y ejecutado tu primera aplicación Python. Este es solo un ejemplo simple, pero puedes comenzar a construir proyectos más complejos a partir de aquí. ¡Diviértete programando en Python!

---
## Sintaxis y semántica de Python
La sintaxis y la semántica son dos aspectos clave en cualquier lenguaje de programación, incluido Python. Aquí tienes una explicación con ejemplos específicos del código que proporcionaste:

**Sintaxis:**

La sintaxis se refiere a las reglas y estructuras que rigen la construcción de programas en un lenguaje de programación específico. En Python, la sintaxis es legible y utiliza la indentación para delimitar bloques de código.

**Ejemplo:**

```python
print("Hola Mundo")
print(45)
```

En este código:

- La función `print()` se utiliza para imprimir valores en la consola.
- Los paréntesis `()` son necesarios para indicar que `print` es una función.
- Las cadenas de texto están envueltas entre comillas dobles (`"`) y los números no necesitan comillas.

**Semántica:**

La semántica se refiere al significado de las construcciones en un lenguaje de programación. Es decir, cómo se interpretan y ejecutan las instrucciones. La semántica de Python es bastante sencilla y orientada a objetos.

**Ejemplo:**

```python
print("Hola Mundo")  # Imprime la cadena de texto "Hola Mundo"
print(45)            # Imprime el número 45
```

- La primera línea imprime la cadena de texto "Hola Mundo" en la consola.
- La segunda línea imprime el número 45 en la consola.

Ambas líneas son instrucciones independientes y se ejecutan secuencialmente. La semántica de Python asegura que la función `print` muestre el valor proporcionado como argumento en la consola.

En resumen, la sintaxis de Python te permite escribir código de manera estructurada, y la semántica garantiza que el código tenga un significado y un comportamiento específicos. En este caso, el código simplemente imprime un saludo y un número en la consola.

---
## Resumen

¡Felicitaciones! Has completado la configuración de tu entorno de desarrollo y has dado tus primeros pasos al crear y ejecutar tu primer programa en Python. Este logro marca el emocionante inicio de tu travesía para convertirte en un hábil programador de Python.

**Sigue aprendiendo y explorando con tutoriales en línea**

Continúa tu camino de aprendizaje con recursos adicionales:

- **Documentación de Python:** Accede a la documentación oficial de Python para obtener detalles y recursos avanzados: [https://docs.python.org/es/3/tutorial/](https://docs.python.org/es/3/tutorial/)
  
- **Python para principiantes:** Explora recursos específicos para principiantes en Microsoft Learn: [https://learn.microsoft.com/es-es/training/paths/beginner-python/](https://learn.microsoft.com/es-es/training/paths/beginner-python/)

**Nota:**
**Si te gustó esta sección, apoya el curso con una calificación de 5 estrellas**:
⭐⭐⭐⭐⭐
Tu opinión es valiosa. Deja un mensaje expresando tus impresiones y agradecimientos. Estamos emocionados de ser parte de tu viaje en el fascinante mundo de Python. ¡Sigamos construyendo conocimiento juntos!
