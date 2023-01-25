from tkinter import *
from tasks import *
from tkinter import messagebox
import time


def click_notes_button(window, task_button, notes_button):

    task_button.place_forget()
    notes_button.place_forget()

    notes_header_label = Label(
        font = ("Consolas", "20"),
        text = "Notes setting",
        borderwidth = 2,
        relief = SOLID
    )

    notes_header_label.place(
        x = 200, y = 100,
        width = 400,
        height = 50
    )

    notes_name_label = Label(
        text = "Note name:",
        font = ("Consolas", "14"),
        relief = SOLID
    )
    
    notes_name_label.place(
        x = 200, y = 155,
        width = 150,
        height = 30
    )

    note_name = StringVar()
    entry_note_name = Entry(
        font = "14",
        textvariable = note_name,
    )
    
    entry_note_name.place(
        x = 360, y = 155,
        width = 220,
        height = 30
    )

    note_description_label = Label(
        text = "Description",
        font = ("Consolas", "14"),
        relief = SOLID
    )

    note_description_label.place(
        x = 200, y = 190,
        width = 150,
        height = 30
    )

    note_description = StringVar()
    entry_note_description = Text(
        font = ("Consolas", "14"),
        bg = "light cyan"
    )
    
    entry_note_description.place(
        x = 360, y = 190,
        width = 220,
        height = 300
    )

    def save_note_to_csv(note_name, note_description):
        with open('notes.csv', mode = 'a') as csv_file:
            fieldnames = ['Note Name', 'Note Description']
            writer = DictWriter(csv_file, fieldnames = fieldnames)
            writer.writerow({
                'Note Name' : note_name,
                'Note Description' : note_description,
            })

    save_button = Button(
        text = "Save",
        font = ("Consolas", "20"),
        command = lambda: save_note_to_scv(note_name,note_description)
         
    )
    
    save_button.place(
        x = 300, y = 600,
        width = 200,
        height = 50
    )

        






# def click_reminder_button(window, task_button, reminder_button):
#     '''Кнопка выбора напоминания'''
#     task_button.place_forget()
#     reminder_button.place_forget()
    
#     reminder_header_label = Label(
#         window,
#         font = ("Consolas", "20"),
#         text = "Reminder setting",
#         borderwidth = 2,
#         relief = SOLID
#     )
    
#     hrs = StringVar()
#     hours = ('00', '01', '02', '03', '04', '05', '06', '07',
#          '08', '09', '10', '11', '12', '13', '14', '15',
#          '16', '17', '18', '19', '20', '21', '22', '23', '24'
#         )
#     hrs.set(hours[0])

#     mins=StringVar()
#     minutes = ('00', '01', '05', '10', '15', '20', '25', '30',
#         '35', '40', '45', '50', '55', '60')
#     mins.set(minutes[0])

#     sec=StringVar()
#     seconds = ('00', '05', '10', '15', '20', '25', '30',
#         '35', '40', '45', '50', '55', '60')
#     sec.set(seconds[0])


#     '''Функция таймера - отсчет единиц времени'''
#     def countdown():
#         times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
#         while times > -1:
#             minute,second = (times // 60 , times % 60)
            
#             hour = 0
#             if minute > 60:
#                 hour , minute = (minute // 60 , minute % 60)
        
#             sec.set(second)
#             mins.set(minute)
#             hrs.set(hour)
    
#             window.update()
#             time.sleep(1)

#             if(times == 0):
                
#                 time_over = Label(window, font = ("Consolas", "15"), text = "Time is over!", foreground = "red")
#                 time_over.place(x = 335, y = 500)
#                 print("Wake up!")
                
#                 sec.set('00')
#                 mins.set('00')
#                 hrs.set('00')

#             times -= 1

#     reminder_header_label.place(
#         x = 200, y = 100,
#         width = 400,
#         height = 50
#     )
    
#     task_name_label = Label(
#         text = "Reminder name:",
#         font = ("Consolas", "14"),
#         relief = SOLID
#     )
    
#     task_name_label.place(
#         x = 200, y = 155,
#         width = 150,
#         height = 30
#     )

#     task_name = StringVar()
#     entry_task_name = Entry(
#         font = "14",
#         textvariable = task_name,
#     )
    
#     entry_task_name.place(
#         x = 360, y = 155,
#         width = 220,
#         height = 30
#     )
    
#     setalarm_text = Label(
#         window,
#         font = ("Consolas", 16, 'bold'),
#         text="Choose time for task!"
#     )
#     hour_text = Label(
#         window,
#         font = ('arial', 11, 'bold'),
#         text="Hour"
#     )
#     minute_text = Label(
#         window,
#         font = ('arial', 11, 'bold'),
#         text="Minute"
#     )
#     seconds_text = Label(
#         window,
#         font = ('arial', 11, 'bold'),
#         text = "Sec")

#     hours_option = OptionMenu(window, hrs, *hours)
#     minutes_option = OptionMenu(window, mins, *minutes)
#     seconds_option = OptionMenu(window, sec, *seconds)

#     settimer_button = Button(window, text="Set Timer!", command = countdown, bg="#D4AC0D", fg="Black",font = ("Consolas", 19, 'bold'))

#     setalarm_text.place(x = 270, y = 250)
#     hour_text.place(x = 270, y = 330)
#     minute_text.place(x = 370, y = 330)
#     seconds_text.place(x = 470, y = 330)

#     hours_option.place(x = 270, y = 350)
#     minutes_option.place(x = 370, y = 350)
#     seconds_option.place(x = 470, y = 350)
#     settimer_button.place(x = 330, y = 420)
    
#     save_button = Button(
#         text = "Save",
#         font = ("Consolas", "20") 
#     )
    
#     save_button.place(
#         x = 300, y = 600,
#         width = 200,
#         height = 50
#     )



