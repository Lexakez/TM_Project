from tkinter import *

Window = Tk()

Window.title("New Reminder")

Window.geometry("600x200")
Window.minsize(600,200)
Window.maxsize(600,200)

task_button = Button(
    font = ("Consolas", "15"), 
    text = "Task",
)

reminder_button = Button(
    font = ("Consolas", "15"), 
    text = "Reminder",
)

task_button.place(
    x = 50, y = 50,
    width = 100,
    height = 50
)

reminder_button.place(
    x = 200, y = 50,
    width = 100,
    height = 50
)



Window.mainloop()
