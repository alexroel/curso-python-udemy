import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from logic import TaskManager

class FrameTaskList(tk.Frame):
   def __init__(self, parent):
      super().__init__(parent)

      self.task_manager = TaskManager()
      self.root = parent

      # Crear un estilo para los encabezados del Treeview
      style = ttk.Style()
      style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
      style.configure("Treeview", font = ("Helvetica", 11), rowheight=30)

      
      # Crear y configurar Treeview
      self.tree = ttk.Treeview(self.root, columns=("Task"), selectmode="none")
      self.tree.heading("Task", text="Tareas")
      self.tree.grid(row=0, column=0, sticky="nsew")

      self.tree.column("#0", anchor="center", width=3)
      self.tree.column("Task", width=400)

      # Crear y configurar el frame para los botones
      button_frame = tk.Frame(self.root)
      button_frame.grid(row=1, column=0, sticky="ew", pady=(0,20), padx=5)

      # Añadir botones
      self.add_img = tk.PhotoImage(file="img/add.png").subsample(2,2)
      self.add_label = tk.Label(button_frame, image=self.add_img)
      self.add_label.grid(row=0, column=0)

      # Configurar grid para expandir el Entry
      button_frame.grid_columnconfigure(1, weight=1)

      # Añadir campo de entrada
      self.task_entry = ttk.Entry(button_frame, font=("Helveltica", 14))
      self.task_entry.grid(row=0, column=1, ipadx=30, sticky="ew")
      self.task_entry.bind("<Return>", self.add_task)

      # Configurar bindings y menús
      self.tree.bind("<Button-3>", self.show_context_menu)
      self.tree.bind("<Button-1>", self.on_item_click)

      self.context_menu = tk.Menu(self.root, tearoff=0)
      self.context_menu.add_command(label="Eliminar", command=self.delete_task)
      self.context_menu.add_command(label="Marcar como Completado", command=self.completed_task)

      # Cargar imágenes de checkbox
      self._img1 = tk.PhotoImage(file="img/blank_check.png").subsample(2,2)
      self._img2 = tk.PhotoImage(file="img/check_one.png").subsample(2,2)

      # Configurar el grid layout para expandirse
      self.root.grid_rowconfigure(0, weight=1)
      self.root.grid_columnconfigure(0, weight=1)

      self.load_tasks()
   def show_context_menu(self, event):
      try:
         self.tree.selection_clear()
         item = self.tree.identify_row(event.y)
         self.tree.selection_set(item)
         self.context_menu.tk_popup(event.x_root, event.y_root)
      finally:
         self.context_menu.grab_release()

   def on_item_click(self, event):
      region = self.tree.identify_region(event.x, event.y)
      if region == "tree":
         column = self.tree.identify_column(event.x)
         if column == "#0":
            item = self.tree.identify_row(event.y)
            if item:
               self.completed_task(item)

   def load_tasks(self):
      for item in self.tree.get_children():
         self.tree.delete(item)
      
      for idx, task in enumerate(self.task_manager.get_tasks()):
         task_name = task["name"]
         if task["completed"]:
            self.tree.insert("", "end", iid=idx, values=(task_name,""), image=self._img2, tags=("completed",))
         else:
            self.tree.insert("", "end", iid=idx, values=(task_name, ""), image=self._img1)
      self.tree.tag_configure("completed", foreground="gray", font=("Helvetica", 11, "overstrike"))

   def add_task(self, event):
      task_name = self.task_entry.get()
      if task_name:
         self.task_manager.add_task(task_name)
         self.load_tasks()
         self.task_entry.delete(0, tk.END)
   
   def delete_task(self):
      selected_item = self.tree.selection()
      if selected_item:
         task_id = selected_item[0]
         self.task_manager.delete_task(int(task_id))
         self.load_tasks()

   def completed_task(self, item=None):
      if item is None:
         selected_item = self.tree.selection()
         if not selected_item:
            return
         item = selected_item[0]
      task_id = int(item)
      self.task_manager.complete_task(task_id)
      self.load_tasks()


