import json

class ControladorTareas:
    def __init__(self, archivo_tareas):
        self.archivo_tareas = archivo_tareas
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open(self.archivo_tareas, "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    def guardar_tareas(self):
        with open(self.archivo_tareas, "w") as archivo:
            json.dump(self.tareas, archivo, indent=4)

    def agregar_tarea(self, nombre):
        self.tareas.append({"nombre": nombre, "completada": False})
        self.guardar_tareas()

    def obtener_tareas(self):
        return self.tareas

    def marcar_como_completada(self, idx):
        self.tareas[idx]["completada"] = True
        self.guardar_tareas()

    def editar_tarea(self, idx, nuevo_nombre):
        self.tareas[idx]["nombre"] = nuevo_nombre
        self.guardar_tareas()

    def eliminar_tarea(self, idx):
        del self.tareas[idx]
        self.guardar_tareas()
