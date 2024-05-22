import json
import os

class TaskManager:
   def __init__(self, filename = "tasks.json") -> None:
      self.filename = filename
      self.tasks = []
      self.load_tasks()

   def load_tasks(self):
      if os.path.exists(self.filename):
         with open(self.filename, "r") as file:
            self.tasks = json.load(file)
      else:
         self.tasks = []
   
   def save_tasks(self):
      with open(self.filename, "w") as file:
         json.dump(self.tasks, file, indent=4)
      
   def get_tasks(self):
      return self.tasks
   
   def add_task(self, name):
      self.tasks.append({"name":name, "completed":False})
      self.save_tasks()

   def delete_task(self, index):
      del self.tasks[index]
      self.save_tasks()

   def complete_task(self, index):
      self.tasks[index]["completed"] = not self.tasks[index]["completed"]
      self.save_tasks()