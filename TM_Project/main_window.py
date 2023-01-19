from tkinter import *
from button_commands import *


def Main_window(extension, window):
    '''параметры главного окна'''
    window.title("Task Manager Project")
    window.geometry(extension)
    window.minsize(600,700)
    window.maxsize(600,700)
    header_label = Label(
        font = ("Consolas", "20"), 
        text = "To-do list",
        borderwidth = 4,
        relief = SOLID
    )
    task_label = Label(
        background = "grey",
    )
    main_label = Label(
        background = "lightgrey"
    )
    yourtasks_text_label = Label(
        foreground = "green",
        font = ("Consolas", "15"), 
        text = "Your Tasks:",
    )
    header_label.place(
        x = 0, y = 0,
        width = 600, 
        height = 100
    )
    task_label.place(
        x = 0, y = 100,
        width = 200, 
        height = 600
    )
    yourtasks_text_label.place(
        x = 200, y = 100, 
        width = 400,
        height = 50
    )
    main_label.place(
        x = 200, y =100, 
        width = 400, 
        height = 600
    )

def Trash_button():
    '''Кнопка удалить задачу'''
    trash_button = Button(
        font = ("Consolas", "15"),
        foreground = "red",
        text = "Delete Task",
    )
    trash_button.place(
        x = 0, y =600, 
        width = 200, 
        height = 50
    )
def Delete_all_button():
    '''Кнопка удалить все задачи'''
    deleteall_button = Button(
        font = ("Consolas", "15"), 
        background = "red",
        foreground = "white",
        text = "Delete All",
    )
    deleteall_button.place(
        x = 0, y =650, 
        width = 200, 
        height = 50
    )
def Add_task_button(window):
    '''Кнопка добавить задачу'''
    addtask_button = Button(
        background = "green",
        foreground = "white",
        font = ("Consolas", "15"), 
        text = "Add Task:",
        command = lambda: click_add_task_button(window)
    )
    addtask_button.place(
        x = 0,
        y = 100,
        width=200,
        height=50
    )