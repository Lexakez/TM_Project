from tkinter import *
import time
from tasks import *
from tkinter import messagebox
import schedule
import time
import playsound

def add_task_button(window):
    '''Кнопка добавить задачу'''
    addtask_button = Button(
        background = "green",
        foreground = "white",
        font = ("Consolas", "15"), 
        text = "Add Task:",
        command = lambda: click_add_task_button(window, addtask_button)
    )
    addtask_button.place(
        x = 0,
        y = 100,
        width=200,
        height=50
    )

def click_add_task_button(window, add_task_button):
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
    '''Удаление кнопки "добавить новую задачу"'''
    add_task_button.destroy()

def click_reminder_button(window, task_button, reminder_button):
    '''Кнопка выбора напоминания'''
    task_button.place_forget()
    reminder_button.place_forget()
    
    reminder_header_label = Label(
        window,
        font = ("Consolas", "20"),
        text = "Reminder setting",
        borderwidth = 2,
        relief = SOLID
    )
    
    def setalarm():
        alarmtime = f"{hour.get()}:{minute.get()}:{second.get()}"
        print(alarmtime)
        if (alarmtime!="0:0:0"):
            alarmclock(alarmtime)

    def alarmclock(alarmtime):
        while True:
            # time.sleep(1)
            time_now = time.strftime("%H:%M:%S")
            # timeleft = int(time_now) - int(alarmtime)
            # print(timeleft)
            print(time_now, alarmtime)
            if time_now == alarmtime:
                time_over = Label(window, font = ("Consolas", "15"), text = "Time is over!", foreground = "red")
                time_over.place(x = 250, y = 500)
                print("Wake up!")
                
                break

    hour = StringVar()
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
    hour.set(hours[0])

    minute=StringVar()
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
    minute.set(minutes[0])

    second=StringVar()
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
    second.set(seconds[0])


    timetext_label = Label(
        window,
        font = ("Consolas", "15"),
        text = "Current time:",
    )
    setalarm_text = Label(
        window,
        font = ("Consolas", 16, 'bold'),
        text="Set Your Alarm Clock!"
    )
    hour_text = Label(
        window,
        font = ('arial', 11, 'bold'),
        text="Hour"
    )
    minute_text = Label(
        window,
        font = ('arial', 11, 'bold'),
        text="Minute"
    )
    seconds_text = Label(
        window,
        font = ('arial', 11, 'bold'),
        text = "Sec")

    hours_option = OptionMenu(window, hour, *hours)
    minutes_option = OptionMenu(window, minute, *minutes)
    seconds_option = OptionMenu(window, second, *seconds)

    settimer_button = Button(window, text="Set Timer!", command = setalarm, bg="#D4AC0D", fg="Black",font = ("Consolas", 19, 'bold'))

    setalarm_text.place(x = 270, y = 250)
    hour_text.place(x = 270, y = 330)
    minute_text.place(x = 370, y = 330)
    seconds_text.place(x = 470, y = 330)

    hours_option.place(x = 270, y = 350)
    minutes_option.place(x = 370, y = 350)
    seconds_option.place(x = 470, y = 350)
    settimer_button.place(x = 330, y = 420)
    
    reminder_header_label.place(
        x = 200, y = 150,
        width = 400,
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
    setalarm_text = Label(
        window,
        font = ("Consolas", 14),
        text="Alarm Clock:",
        relief = SOLID
    )
    hour_text = Label(
        window,
        font = ('arial', 14),
        text="Hour:"
    )
    minute_text = Label(
        window,
        font = ('arial', 14),
        text="Minute:"
    )

    minute=StringVar()
    hour = StringVar()

    hours = [
        '00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24'
    ]
    minutes = [
        '00', '05', '10', '15', '20', '25', '30',
        '35', '40', '45', '50', '55', '60'
    ]

    hours_option = OptionMenu(window, hour, *hours)
    minutes_option = OptionMenu(window, minute, *minutes)

    setalarm_text.place(x = 200, y = 465, width = 150)
    hour_text.place(x = 355, y = 465)
    minute_text.place(x = 460, y = 465)

    hours_option.place(x = 410, y = 465)
    minutes_option.place(x = 530, y = 465)
    # settimer_button.place(x = 330, y = 630)
    save_button = Button(
        text = "Save",
        font = ("Consolas", "20"),
        command = lambda: click_save_task_button(window, task_name, task_description, task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box, setalarm_text, hour_text, minute_text, hours_option, minutes_option), 
    )
    save_button.place(
        x = 300, y = 600,
        width = 200,
        height = 50
    )

task_list = []

def click_save_task_button(window, task_name, task_description,task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box, setalarm_text, hour_text, minute_text, hours_option, minutes_option):
    '''Кнопка сохранить задачу'''
    if task_name.get() == "":
        messagebox.showinfo("Error", "You can't create a task without a name")
    else:
        task = (New_task(task_name.get()))
        task_list.append(task)
        task.draw(task_name, task_list)
        task.save_task_to_csv(task_name.get(), task_description.get())
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
        setalarm_text.destroy()
        hour_text.destroy()
        minute_text.destroy()
        hours_option.destroy()
        minutes_option.destroy()
        add_task_button(window)
