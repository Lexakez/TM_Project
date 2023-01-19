from tkinter import *

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager Project")
        self.master.geometry("600x700")
        self.master.minsize(600,700)
        self.master.maxsize(600,700)
        self.tasks = []

        self.header_label = Label(
            font = ("Consolas", "20"), 
            text = "To-do list",
            borderwidth = 4,
            relief = SOLID
        )

        self.task_label = Label(
            background = "grey",
        )

        self.main_label = Label(
            background = "lightgrey"
        )

        self.yourtasks_text_label = Label(
            foreground = "green",
            font = ("Consolas", "15"), 
            text = "Your Tasks:",
        )

        self.trash_button = Button(
            font = ("Consolas", "15"),
            foreground = "red",
            text = "Delete Task",
        )

        self.deleteall_button = Button(
            font = ("Consolas", "15"), 
            background = "red",
            foreground = "white",
            text = "Delete All",
        )
        
        self.draw()

    def draw(self):
        '''Отрисовка интерфейса'''
        self.header_label.place(
            x = 0, y = 0,
            width = 600, 
            height = 100
        )

        self.task_label.place(
            x = 0, y = 100,
            width = 200, 
            height = 600
        )

        self.yourtasks_text_label.place(
            x = 200, y = 100, 
            width = 400,
            height = 50
        )

        self.main_label.place(
            x = 200, y =100, 
            width = 400, 
            height = 600
        )

        self.trash_button.place(
            x = 0, y =600, 
            width = 200, 
            height = 50
        )

        self.deleteall_button.place(
            x = 0, y =650, 
            width = 200, 
            height = 50
        )
