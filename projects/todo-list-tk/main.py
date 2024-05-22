from ui import FrameTaskList
import tkinter as tk


def run():
   root = tk.Tk()
   root.title("My To Do")
   root.geometry("500x600")
   root.resizable(False, True)

   frame_task = FrameTaskList(root)
   frame_task.grid(row=0, column=0, sticky="nsew")
   
   root.mainloop()


if __name__ == "__main__":
   run()

