from task_manager import Task, TaskManager

def main():
    task_list = TaskManager()

    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Marcar como Realizada")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            description = input("Ingrese la descripción de la tarea: ")
            new_task = Task(description)
            task_list.agregar_tarea(new_task)
            print("Tarea agregada correctamente.")

        elif option == "2":
            task_list.mostrar_tareas()

        elif option == "3":
            task_list.mostrar_tareas()
            index = int(input("Ingrese el número de la tarea a marcar como realizada: "))
            task_list.marcar_como_realizada(index)

        elif option == "4":
            print("¡Adiós!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()


