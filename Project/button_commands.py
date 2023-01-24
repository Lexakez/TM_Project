from tkinter import *
import time
from tasks import *
from tkinter import messagebox
import time



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



