from tkinter import *
from tkinter import ttk
from add_task_btn import Add_task
from main_window import TaskManager

window_size = "600x700"
Window = Tk()

Main_window = TaskManager(Window)
Add_task_button = Add_task(Window)

Window.mainloop()