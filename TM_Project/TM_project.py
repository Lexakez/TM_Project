from tkinter import *
from tkinter import ttk
from main_window import *

window_size = "600x700"
Screen = Tk()

Main_window(window_size, Screen)
Trash_button()
Delete_all_button()
Add_task_button(Screen)

Screen.mainloop()