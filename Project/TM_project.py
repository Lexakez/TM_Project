from tkinter import *
from tkinter import ttk
from main_window import *
from tasks import *

window_size = "600x700"
Screen = Tk()

main_window(window_size, Screen)
trash_button()
delete_all_button()
add_task_button(Screen)


Screen.mainloop()