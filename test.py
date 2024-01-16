ruta_archivo = "texto.txt"


# Abrir un archivo en modo de escritura
with open(ruta_archivo, 'w') as archivo:
    archivo.write('Hola, este es un nuevo archivo.\n')
    archivo.write('¡Aprender Python es divertido!')

try:
    with open(ruta_archivo, 'r') as archivo:
        # contenido = archivo.read()
        # print(contenido)
        lineas = archivo.readlines()
        print(lineas)
        for linea in lineas:
            print(linea)

    

except FileNotFoundError:
    print("El archivo no existe")

except Exception as e:
    print(f"Se produjo un error: {e}")



