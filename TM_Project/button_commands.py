from tkinter import *
import time

def click_add_task_button(window):
    '''Нажатие на кнопку добавить новую задачу/ создание окна с выбором задачи'''
    task_setting = Toplevel(window)
    task_setting.geometry("600x200")
    task_setting.title("Task settings")
    task_setting.minsize(600,200)
    task_setting.maxsize(600,200)
    task_setting.title("Task Settings")
    task_button = Button(
        task_setting,
        font = ("Consolas", "15"), 
        text = "Task",
    )
    reminder_button = Button(
        task_setting,
        font = ("Consolas", "15"), 
        text = "Reminder",
        command = lambda: Click_reminder_button(window, task_setting)
    )
    '''отрисовка кнопок выбора задач'''
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

def Click_reminder_button(window, task_setting):
    '''Кнопка выбора напоминания'''
    task_setting.destroy()
    reminder_window = Toplevel(window)
    reminder_window.title("New Reminder")
    reminder_window.geometry("600x300")
    reminder_window.minsize(600,300)
    reminder_window.maxsize(600,300)
    reminder_header_label = Label(
        reminder_window,
        font = ("Consolas", "20"), 
        text = "Reminder setting",
        borderwidth = 4,
        relief = SOLID
    )
    def clock():
        '''Часы'''
        clock_time = time.strftime('%H:%M:%S')
        current_time.config(text = clock_time)
        current_time.after(1000, clock)
    current_time = Label(
        reminder_window,
        font = ("Consolas", "15"), 
        text = "",
    )
    clock()
    timetext_label = Label(
        reminder_window,
        font = ("Consolas", "15"),
        text = "Current time:",
    )
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


