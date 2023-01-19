from tkinter import *

class TaskSettings:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x200")
        self.master.minsize(600,200)
        self.master.maxsize(600,200)
        self.master.title("Task Settings")
        self.task_button = Button(
            self.master,
            font = ("Consolas", "15"), 
            text = "Task",
)

        self.reminder_button = Button(
            self.master,
            font = ("Consolas", "15"), 
            text = "Reminder",
)

        self.draw()

    def draw(self):
        self.task_button.place(
            x = 50, y = 50,
            width = 100,
            height = 50
)
        self.reminder_button.place(
            x = 200, y = 50,
            width = 100,
            height = 50
)

