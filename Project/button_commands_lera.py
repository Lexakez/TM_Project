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
            print(time_now, alarmtime)
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







