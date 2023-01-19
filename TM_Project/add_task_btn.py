from tkinter import *

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
        self.new_window.geometry("600x700")
        self.new_window.title("Task Settings")
        label = Label(self.new_window, text="Task Settings")
        label.place()
        reminder_btn = Button(self.new_window, text="Reminder", command=self.reminder)
        reminder_btn.pack()

    def reminder(self):
        self.reminder_window = Toplevel(self.master)
        self.reminder_window.geometry("600x700")
        self.reminder_window.title("New Reminder")
        self.new_window.destroy()