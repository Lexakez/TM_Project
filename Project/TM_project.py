from tkinter import *
from tkinter import ttk
from main_window import *
from tasks import *
from tkinter import messagebox
from PIL import ImageTk, Image
from csv import *

window_size = "600x700"
Screen = Tk()

main_window(window_size, Screen)

csv_task_list = []
csv_note_list = []


def cheking():
    '''Перерисовка кнопок и удаление их из списка'''
    check = True
    if check:
        for task in csv_task_list:
            if not task.exist:
                check = False
                csv_task_list.remove(task)
                for task2 in csv_task_list:
                    task2.task_button.destroy()
                for note2 in csv_note_list:
                    note2.note_button.destroy()
                for i, task in enumerate(csv_task_list):
                    task.draw(i, 0)
                for i, note in enumerate(csv_note_list):
                    note.draw(i, len(csv_task_list))
                break
    if check:
        for note in csv_note_list:
            if not note.exist:
                check = False
                csv_note_list.remove(note)
                for task2 in csv_task_list:
                    task2.task_button.destroy()
                for note2 in csv_note_list:
                    note2.note_button.destroy()
                for i, task in enumerate(csv_task_list):
                    task.draw(i, 0)
                for i, note in enumerate(csv_note_list):
                    note.draw(i, len(csv_task_list))
                break
    Screen.after(100, cheking)


try:
    with open("tasks.csv", "r") as csv_file:
        csv_reader = reader(csv_file, delimiter = ",")
        next(csv_reader)
        for line in csv_reader:
            csv_task_list.append(New_task(line[0], line[1], line[2].split("|"), line[3]))
except FileNotFoundError:
    print("No such file")   

for i, task in enumerate(csv_task_list):
    task.draw(i, len(csv_note_list))
    
try:
    with open("notes.csv", "r") as csv_file:
        csv_reader = reader(csv_file, delimiter = ",")
        next(csv_reader)
        for line in csv_reader:
            csv_note_list.append(Note(line[0], line[1]))
except FileNotFoundError:
    print("No such file")

for i, note in enumerate(csv_note_list):
    note.draw(i, len(csv_task_list))

def click_delete_all_button():
    '''Нажатие на кнопку удалить все, удаляет все из цсв файла'''
    for task in csv_task_list:
        task.task_button.destroy()
    with open('tasks.csv', 'w', newline = '') as csv_file:
        fieldnames = ['Task Name', 'Task Description', 'Goals', 'Time']
        writer = DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
    csv_task_list.clear()
    csv_note_list.clear()

def click_add_task_button(window, add_task_button):
    '''Нажатие на кнопку добавить новую задачу'''
    if len(csv_task_list) == 9:
        messagebox.showinfo("Error", "You can't create more than 9 tasks/reminders")
        
    else:
        task_button = Button(
            window,
            font = ("Consolas", "15"), 
            text = "Task",
            command = lambda: click_task_button(window, task_button, notes_button)
        )

        notes_button = Button(
            window,
            font = ("Consolas", "15"), 
            text = "Notes",
            command = lambda: click_notes_button(window, task_button, notes_button)
        )

        '''отрисовка кнопок выбора задач'''
        task_button.place(
            x = 200, y = 100,
            width = 200,
            height = 50
        )
        notes_button.place(
            x = 400, y = 100,
            width = 200,
            height = 50
        )
        '''Удаление кнопки "добавить новую задачу"'''
        add_task_button.place_forget()

def click_task_button(window, task_button, notes_button):
    '''Кнопка выбора задачи'''
    task_button.place_forget()
    notes_button.place_forget()
    task_header_label = Label(
        font = ("Consolas", "20"),
        text = "Task setting:",
        borderwidth = 4,
        relief = GROOVE
    )
    task_header_label.place(
        x = 200, y = 100,
        width = 400,
        height = 50
    )
    task_name_label = Label(
        text = "Task name:",
        font = ("Consolas", "14"),
        relief = GROOVE
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
        x = 360, y = 155,
        width = 210,
        height = 30
    )
    task_description_label = Label(
        text = "Description",
        font = ("Consolas", "14"),
        relief = GROOVE
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
        x = 360, y = 190,
        width = 210,
        height = 30
    )
    goal_label = Label(
        text = "Goals:",
        font = ("Consolas", "14"),
        relief = GROOVE
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
        x = 360, y = 225,
        width = 180,
        height = 30
    )

    def add():
        new_goal = entry_goal.get()
        goal_list_box.insert(0, new_goal)
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
        relief = GROOVE
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

    minute = StringVar()
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
        command = lambda: click_save_task_button(window, task_name, task_description, task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box, setalarm_text, hour_text, minute_text, hours_option, minutes_option, minute, hour), 
    )
    save_button.place(
        x = 300, y = 600,
        width = 200,
        height = 50
    )

def click_notes_button(window, task_button, notes_button):
    '''Кнопка выбора заметки'''
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
    
    entry_note_description = Text(
        font = ("Consolas", "14"),
        bg = "light cyan",
        
    )
    entry_note_description.place(
        x = 360, y = 190,
        width = 220,
        height = 300
    )
    save_button = Button(
        text = "Save",
        font = ("Consolas", "20"),
        command = lambda:click_save_note_button(note_name, notes_name_label, entry_note_name, notes_header_label, note_description_label, entry_note_description, save_button)
    )
    save_button.place(
        x = 300, y = 600,
        width = 200,
        height = 50
    )

task_list = []

def click_save_task_button(window, task_name, task_description, task_name_label, entry_task_name, task_header_label, save_button, add_button, task_description_label, entry_task_description, goal_label, entry_goal, goal_list_box, setalarm_text, hour_text, minute_text, hours_option, minutes_option, minutes, hours):
    '''Кнопка сохранить задачу'''
    if task_name.get() == "":
        messagebox.showinfo("Error", "You can't create a task without a name")
    else:
        goals_copy = list(goal_list_box.get(0, END)).copy()
        result = []
        for st_idx in range(0, len(goals_copy), 1):
            result.extend(goals_copy[st_idx:st_idx+1])
            result.append("0")
        task = (New_task(task_name.get(), task_description.get(), result, str(hours.get() + ':' + minutes.get())))
        csv_task_list.append(task)
        task.draw(len(csv_task_list) - 1, len(csv_note_list))
        goals = goal_list_box.get(0, END)
        task.save_task_to_csv(task_name.get(), task_description.get(), goals, hours.get(), minutes.get())
        '''Убирает с экрана настройки задачи и возвращает кнопку "добавить новую задачу"'''
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
        addtask_button.place(
            x = 0,
            y = 100,
            width=200,
            height=50
        )

def click_save_note_button(note_name, notes_name_label, entry_note_name, note_header_label, note_description_label, entry_note_description, save_button):
    if note_name.get() == "":
        messagebox.showinfo("Error", "You can't create a task without a name")
    else:
        note_description = (entry_note_description.get(1.0, END))
        note_description = note_description.replace('\n',' ')
        note = Note(note_name.get(), note_description)
        csv_note_list.append(note)
        note.draw(len(csv_task_list), len(csv_note_list) - 1)
        note.save_note_to_csv(note_name.get(), note_description)
        notes_name_label.destroy()
        entry_note_name.destroy()
        note_header_label.destroy()
        note_description_label.destroy()
        entry_note_description.destroy()
        save_button.destroy()
        
        
        addtask_button.place(
                x = 0,
                y = 100,
                width=200,
                height=50
            )


'''Кнопка добавить задачу'''
addtask_button = Button(
    background = "green",
    foreground = "white",
    font = ("Consolas", "15"), 
    text = "Add Task",
    command = lambda: click_add_task_button(Screen, addtask_button)
)
addtask_button.place(
    x = 0,
    y = 100,
    width=200,
    height=50
)

'''Кнопка удалить все задачи'''
deleteall_button = Button(
    font = ("Consolas", "15"), 
    background = "red",
    foreground = "white",
    text = "Delete All",
    command = click_delete_all_button
)
deleteall_button.place(
    x = 0, y =650, 
    width = 200, 
    height = 50
)

cheking()

image = Image.open("logo.png")
image = image.resize((80, 90), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(image)
logo = Label(image = logo_image)
logo.place(
    x = 210, y = 0,
)

Screen.mainloop()