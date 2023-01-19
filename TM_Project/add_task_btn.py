from tkinter import *
from taskmenu import TaskSettings

class Add_task:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x700")
        self.addtask_button = Button(
        background = "green",
        foreground = "white",
        font = ("Consolas", "15"), 
        text = "Add Task:",
        command = self.add_task
)
        self.addtask_button.place(
            x = 0,
            y = 100,
            width=200,
            height=50
        )

    def add_task(self):
        self.new_window = Toplevel(self.master)
        task_settings = TaskSettings(self.new_window)

    def reminder(self):
        self.reminder_window = Toplevel(self.master)
        self.reminder_window.geometry("600x700")
        self.reminder_window.title("New Reminder")
        self.new_window.destroy()