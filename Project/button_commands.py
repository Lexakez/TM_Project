from tkinter import *
import time
from tasks import *

def click_add_task_button(window):
    '''Нажатие на кнопку добавить новую задачу'''
    task_button = Button(
        window,
        font = ("Consolas", "15"), 
        text = "Task",
        command = lambda: click_task_button(window, task_button, reminder_button)
    )
    reminder_button = Button(
        window,
        font = ("Consolas", "15"), 
        text = "Reminder",
        command = lambda: click_reminder_button(window, task_button, reminder_button)
    )
    '''отрисовка кнопок выбора задач'''
    task_button.place(
        x = 200, y = 100,
        width = 200,
        height = 50
    )
    reminder_button.place(
        x = 400, y = 100,
        width = 200,
        height = 50
    )

def click_reminder_button(window, task_button, reminder_button):
    '''Кнопка выбора напоминания'''
    task_button.place_forget()
    reminder_button.place_forget()
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

def click_task_button(window, task_button, reminder_button):
    '''Кнопка выбора задачи'''
    task_button.place_forget()
    reminder_button.place_forget()
    task_header_label = Label(
        font = ("Consolas", "20"),
        text = "Task setting:",
        borderwidth = 4,
        relief = SOLID
    )
    task_header_label.place(
        x = 200, y = 100,
        width = 400,
        height = 50
    )
    task_name_label = Label(
        text = "Task name:",
        font = ("Consolas", "14"),
        relief = SOLID
    )
    task_name_label.place(
        x = 200, y = 155,
        width = 150,
        height = 30
    )
    task_name = StringVar()
    entry_task_name = Entry(
        font = "14",
        textvariable = task_name,
    )
    entry_task_name.place(
        x = 350, y = 155,
        width = 250,
        height = 30
    )
    task_description_label = Label(
        text = "Description",
        font = ("Consolas", "14"),
        relief = SOLID
    )
    task_description_label.place(
        x = 200, y = 190,
        width = 150,
        height = 30
    )
    task_description = StringVar()
    entry_task_description = Entry(
        font = ("Consolas", "14"),
        textvariable = task_description
    )
    entry_task_description.place(
        x = 350, y = 190,
        width = 250,
        height = 30
    )
    goal_label = Label(
        text = "Goals:",
        font = ("Consolas", "14"),
        relief = SOLID
    )
    goal_label.place(
        x = 200, y = 225,
        width = 150,
        height = 30
    )
    entry_goal = Entry(
        font = "14",
    )
    entry_goal.place(
        x = 350, y = 225,
        width = 200,
        height = 30
    )
    def add():
        new_goal = entry_goal.get()
        goal_list_box.insert(-1, new_goal)
        entry_goal.delete(0, END)
    add_button = Button(
        text = "add",
        command = add,
        font = ("Consolas", "14")
    )
    add_button.place(
        x = 550, y = 225,
        width = 50,
        height = 30
    )
    goal_list_box = Listbox()
    goal_list_box.place(
        x = 350, y = 260,
        width = 200,
        height = 200,
    )
    save_button = Button(
        text = "Save",
        command = lambda: click_save_task_button(task_name, task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box)
    )
    save_button.place(
        x = 550, y = 660,
        width = 50,
        height = 40
    )

task_list = []

def click_save_task_button(task_name, task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box):
    '''Кнопка сохранить задачу'''
    task = (New_task(task_name.get()))
    task_list.append(task)
    task.draw(task_name, task_list)
    task_name_label.destroy()
    entry_task_name.destroy()
    task_header_label.destroy()
    add_button.destroy()
    task_description_label.destroy()
    entry_task_description.destroy()
    goal_label.destroy()
    entry_goal.destroy()
    goal_list_box.destroy()
    save_button.destroy()