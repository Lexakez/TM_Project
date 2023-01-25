from tkinter import *
# from button_commands import *
import time


def main_window(extension, window):
    '''параметры главного окна'''
    window.title("Task Manager Project")
    window.geometry(extension)
    window.minsize(600,700)
    window.maxsize(600,700)
    
    header_label = Label(
        font = ("Consolas", "20"), 
        text = "TO-DO LIST",
        borderwidth = 4,
        relief = SOLID
    )

    def clock():
            '''Часы'''
            clock_time = time.strftime("%H:%M:%S")
            current_time.config(text = clock_time)
            current_time.after(1000, clock)
            
    timetext_label = Label(
        window,
        font = ("Consolas", "15"),
        text = "Current time:",
        relief = GROOVE
    )
    
    current_time = Label(
        window,
        font = ("Consolas", "15"), 
        text = "",
    )
    
    timetext_label.place(
        x = 400, y = 10,
        width = 150,
        height = 30
    )
    
    current_time.place(
        x = 420, y = 50,
        width = 100,
        height = 30
    )

    clock()
    
    task_label = Label(
        background = "grey",
    )
    
    main_label = Label(
        background = "lightgrey",
    )
    
    yourtasks_text_label = Label(
        foreground = "green",
        font = ("Consolas", "15"), 
        text = "Your Tasks:",
        relief = SOLID
    )
    
    header_label.place(
        x = 0, y = 0,
        width = 200, 
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

