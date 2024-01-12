# Modelo de una tarea 
class Task:
    def __init__(self, description, status="Pendiente") -> None:
        self.description = description
        self.status = status

# lista de tarea 
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def show_tasks(self):
        if not self.tasks:
            print("No hay tareas en la lista")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. Descripción: {task.description}, Estado: {task.status}.")
    
    def mark_as_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index-1].status = "Realizada"
            print(f"Tarea {index} marcada como realizada.")
        else:
            print("Indece de tarea no valido.")