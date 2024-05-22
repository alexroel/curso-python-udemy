from interfaz import InterfazTareas
from logica import ControladorTareas

def main():
    archivo_tareas = "tareas.json"
    controlador = ControladorTareas(archivo_tareas)
    interfaz = InterfazTareas(controlador)
    interfaz.mainloop()

if __name__ == "__main__":
    main()


