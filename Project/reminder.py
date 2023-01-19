from tkinter import *
import time 

reminder_window = Tk()
reminder_window.title("New Reminder")
reminder_window.geometry("600x300")
reminder_window.minsize(600,300)
reminder_window.maxsize(600,300)

reminder_header_label = Label(
    font = ("Consolas", "20"), 
    text = "Reminder setting",
    borderwidth = 4,
    relief = SOLID
)

current_time = Label(
    font = ("Consolas", "15"), 
    text = "",
)

timetext_label = Label( font = ("Consolas", "15"), 
    text = "Current time:",)

def clock():
    clock_time = time.strftime('%H:%M:%S')
    current_time.config(text = clock_time)
    current_time.after(1000, clock)
    

reminder_header_label.place(
    x = 0, y = 0,
    width = 600,
    height = 50
)

timetext_label.place(
    x = 120, y = 50,
    width = 200,
    height = 50
)

current_time.place(
    x = 220, y = 50,
    width = 300,
    height = 50
)

clock()

reminder_window.mainloop()