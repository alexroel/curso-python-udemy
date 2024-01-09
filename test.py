# Lista para almacenar los diccionarios de estudiantes
registro_estudiantes = []

# Menú principal
while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        # Registrar estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        curso = input("Ingrese el curso del estudiante: ")

        # Crear un diccionario con la información del estudiante y agregarlo al registro
        estudiante = {'Nombre': nombre, 'Edad': edad, 'Curso': curso}
        registro_estudiantes.append(estudiante)

        print("Estudiante registrado exitosamente!\n")

    elif opcion == '2':
        # Mostrar registro
        if registro_estudiantes:
            print("\nRegistro de Estudiantes:")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante['Nombre']}, Edad: {estudiante['Edad']}, Curso: {estudiante['Curso']}")
            print()
        else:
            print("El registro está vacío. Registre estudiantes primero.\n")

    elif opcion == '3':
        # Salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.\n")
