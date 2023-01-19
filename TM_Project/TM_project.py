from tkinter import *
from tkinter import ttk
window_size = "600x700"


Window = Tk()

Window.title("Task Manager Project")

Window.geometry(window_size)
Window.minsize(600,700)
Window.maxsize(600,700)

tasks = []

header_label = Label(
    font = ("Consolas", "20"), 
    text = "To-do list",
    borderwidth = 4,
    relief = SOLID
)

task_label = ttk.Label(
    background = "grey",
)

addtask_button = Button(
    background = "green",
    foreground = "white",
    font = ("Consolas", "15"), 
    text = "Add Task:",
)

main_label = Label(
    background = "lightgrey"
)

yourtasks_text_label = Label(
    foreground = "green",
    font = ("Consolas", "15"), 
    text = "Your Tasks:",
)

trash_button = Button(
    font = ("Consolas", "15"),
    foreground = "red",
    text = "Delete Task",
)

deleteall_button = Button(
    font = ("Consolas", "15"), 
    background = "red",
    foreground = "white",
    text = "Delete All",
)

def draw():

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

    addtask_button.place(
        x = 0, y = 100, 
        width = 200, 
        height = 50
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

    trash_button.place(
        x = 0, y =600, 
        width = 200, 
        height = 50
    )

    deleteall_button.place(
        x = 0, y =650, 
        width = 200, 
        height = 50
    )

draw()

Window.mainloop()
