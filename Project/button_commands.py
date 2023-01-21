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
        command = lambda: click_reminder_button(window, task_button)
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

def click_reminder_button(window, task_setting):
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
        relief = SOLID)


    def clock():
        '''Часы'''
        clock_time = time.strftime("%H:%M:%S")
        current_time.config(text = clock_time)
        current_time.after(1000, clock)
    current_time = Label(
        reminder_window,
        font = ("Consolas", "15"), 
        text = "",
    )

    clock()

    def setalarm():
        alarmtime = f"{hour.get()}:{minute.get()}:{second.get()}"
        print(alarmtime)
        if (alarmtime!="0:0:0"):
            alarmclock(alarmtime)

    def alarmclock(alarmtime):
        while True:
            time.sleep(1)
            time_now = time.strftime("%H:%M:%S")
            # timeleft = int(time_now) - int(alarmtime)
            # print(timeleft)
            # print(time_now, alarmtime)
            if time_now == alarmtime:
                time_over = Label(reminder_window, font = ("Consolas", "15"), text = "Time is over!", foreground = "red")
                time_over.place(x = 230, y = 250)
                print("Wake up!")
                
                break

    hour=StringVar()
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

    setalarm_text = Label(reminder_window, font = ("Consolas", 16, 'bold'), text="Set Your Alarm Clock!")
    hour_text = Label(reminder_window, font = ('arial', 11, 'bold'), text="Hour")
    minute_text = Label(reminder_window, font = ('arial', 11, 'bold'), text="Minute")
    seconds_text = Label(reminder_window, font = ('arial', 11, 'bold'), text = "Sec")

    timeleft_text = Label(reminder_window, font = ("Consolas", 16, 'bold'))
    timeleft_text.place()


    hours_option = OptionMenu(reminder_window, hour, *hours)
    minutes_option = OptionMenu(reminder_window, minute, *minutes)
    seconds_option = OptionMenu(reminder_window, second, *seconds)

    settimer_button = Button(reminder_window, text="Set Timer!", command = setalarm, bg="#D4AC0D", fg="Black",font = ("Consolas", 19, 'bold'))

    

    setalarm_text.place(x = 180, y = 100)
    hour_text.place(x = 100, y = 160)
    minute_text.place(x = 200, y = 160)
    seconds_text.place(x = 300, y = 160)

    hours_option.place(x = 100, y = 190)
    minutes_option.place(x = 200, y = 190)
    seconds_option.place(x = 300, y = 190)
    settimer_button.place(x = 400, y = 180)

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
        x = 150, y = 50,
        width = 200,
        height = 50
    )
    current_time.place(
        x = 250, y = 50,
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