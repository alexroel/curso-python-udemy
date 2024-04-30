try:
   # Abrir el archivo en modo lectura
   archivo = open("archivo.txt", "r")

   # Leer el contenido del archivo
   contenido = archivo.read()

except FileNotFoundError:
   print("El archivo no se ha encontrado.")
   print("Creando el archivo")
   archivo = open("archivo.txt","w")
else:
   # Realizar operaciones con el contenido del archivo (opcional)
   print("Contenido del archivo:")
   print(contenido)
finally:
   # Cerrar el archivo para liberar recursos
   if archivo:
      archivo.close()


try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
    print("Creando el archivo")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola mundo")
else:
    # Realizar operaciones con el contenido del archivo (opcional)
    print("Contenido del archivo:")
    print(contenido)


