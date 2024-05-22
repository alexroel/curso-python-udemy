import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Constantes 
FONT = "Arial"
SIZE = 14
COLOR1 = ""
COLOR2 = ""

class InterfazTareas(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Lista de Tareas")

        self.lista_tareas = tk.Listbox(self, width=50, height=10, font=(FONT, SIZE))
        self.lista_tareas.grid(row=0, column=1, padx=10, pady=10, rowspan=4)

        self.actualizar_tareas()

        self.btn_agregar = tk.Button(self, text="Agregar Tarea", 
                                     command=self.agregar_tarea, 
                                     font=(FONT, SIZE),
                                     bg="red")
        self.btn_agregar.grid(row=0, column=0, pady=2)

        self.btn_completar = tk.Button(self, text="Marcar como Completada", 
                                       command=self.completar_tarea, 
                                       font=(FONT, SIZE))
        self.btn_completar.grid(row=1, column=0, pady=2)

        self.btn_editar = tk.Button(self, text="Editar Tarea", command=self.editar_tarea, 
                                    font=(FONT, SIZE))
        self.btn_editar.grid(row=2,column=0, pady=2)

        self.btn_eliminar = tk.Button(self, text="Eliminar Tarea", 
                                      command=self.eliminar_tarea, 
                                      font=(FONT, SIZE))
        self.btn_eliminar.grid(row=3, column=0, pady=2)

    def actualizar_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.controlador.obtener_tareas():
            estado = "Completada" if tarea["completada"] else "Pendiente"
            self.lista_tareas.insert(tk.END, f"{tarea['nombre']} - {estado}")

    def agregar_tarea(self):
        nombre = simpledialog.askstring("Agregar Tarea", "Ingrese el nombre de la tarea:")
        if nombre:
            self.controlador.agregar_tarea(nombre)
            self.actualizar_tareas()

    def completar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_idx = seleccion[0]
            self.controlador.marcar_como_completada(tarea_idx)
            self.actualizar_tareas()

    def editar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_idx = seleccion[0]
            nuevo_nombre = simpledialog.askstring("Editar Tarea", "Ingrese el nuevo nombre de la tarea:")
            if nuevo_nombre:
                self.controlador.editar_tarea(tarea_idx, nuevo_nombre)
                self.actualizar_tareas()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_idx = seleccion[0]
            confirmacion = messagebox.askokcancel("Eliminar Tarea", "¿Está seguro de que desea eliminar esta tarea?")
            if confirmacion:
                self.controlador.eliminar_tarea(tarea_idx)
                self.actualizar_tareas()
