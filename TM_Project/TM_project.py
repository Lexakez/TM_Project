from tkinter import *
from tkinter import ttk

Window = Tk()
Window.title("Task Manager Project")
Window.geometry("500x665")

tasks = []

header_label = Label(
    background = "gray", 
    text = "To do list",
    borderwidth = 4,
)

task_label = ttk.Label(
    background = "grey"
)

header_label.place(x = 0, y = 0, width = 500, height = 100)
task_label.place(x = 0, y = 0, width = 100, height = 600)
Window.mainloop()
