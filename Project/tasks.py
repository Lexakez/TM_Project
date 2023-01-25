from tkinter import *
from csv import *

class New_task:
    def __init__(self, title, description, goal, time):
        self.title = title
        self.description = description
        self.goal = goal
        self.time = time

    def open_task_info(self):
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
        task_name_info = Label(
            font = ("Consolas", "14"),
            text = self.title,
        )
        task_name_info.place(
            x = 350, y = 155
        )
        task_description_label = Label(
            text = "Description:",
            font = ("Consolas", "14"),
            relief = SOLID
        )
        task_description_info = Label(
            text = self.description,
            font = ("Consolas", "14")
        )
        task_description_info.place(
            x = 350, y = 190,
            height = 30,
        )
        task_description_label.place(
            x = 200, y = 190,
            width = 150,
            height = 30
        )
        goal_label = Label(
            text = "Goals:",
            font = ("Consolas", "14"),
            relief = SOLID
        )
        goal_label.place(
            x = 330, y = 225,
            width = 150,
            height = 30
        )
        self.goal_btn_list = []
        self.check_list = [] 
        for i in range(len(self.goal) // 2):
            check_button_var = IntVar()
            self.check_list.append(check_button_var)
            goal_check = Checkbutton(
                text = self.goal[i * 2],
                justify = LEFT,
                bg = "light grey",
                font = ("Consolas", "15"),
                variable = check_button_var
            )
            self.goal_btn_list.append(goal_check)
            goal_check.place(
                x = 250, y = 280 + 30 * i,
                height = 30
            )
        def confirm():
            for i, check_btn in enumerate(self.check_list):
                self.goal[i * 2 + 1] = str(check_btn.get())
            with open('tasks.csv') as inf:
                csv_reader = reader(inf.readlines())

            with open('tasks.csv', 'w', newline = '') as outf:
                csv_writer = writer(outf)
                for line in csv_reader:
                    if line[1] == self.description and line[0] == self.title:
                        csv_writer.writerow("|".join(self.goal))
                        break
                    else:
                        csv_writer.writerow(line)
                csv_writer.writerows(csv_reader)
            task_name_label.destroy()
            task_name_info.destroy()
            task_description_label.destroy()
            task_description_info.destroy()
            goal_label.destroy()
            for goal in self.goal_btn_list:
                goal.place_forget()

        confirm_button = Button(
            text = "Confirm",
            command = confirm,
            font = ("Consolas", "15")
        )
        confirm_button.place(
            x = 330, y = 620,
            width = 150, height = 50
        )

    def draw(self, i, x):
        '''Создание кнопки для задачи'''
        self.task_button = Button(
        text = self.title,
        command = self.open_task_info
    )
        y_position = (((i + 1) + x) * 50 + 100)
        self.task_button.place(
            y = y_position, x = 0,
            width = 200,
            height = 50,
    )

    def __repr__(self) -> str:
        return self.title

    def save_task_to_csv(self, task_name, task_description, goals, hour, minute):
        '''Сохраняет задачу в цсв файл'''
        with open('tasks.csv', mode = 'a', newline = '') as csv_file:
            fieldnames = ['Task Name', 'Task Description', 'Goals', 'Time']
            writer = DictWriter(csv_file, fieldnames = fieldnames)
            time_str = hour + ':' + minute
            if goals:
                goals_str = '|0|'.join(goals) + "|0"
            else:
                goals_str = '|0|'.join(goals)
            writer.writerow({
                'Task Name': task_name,
                'Task Description': task_description,
                'Goals': goals_str,
                'Time': time_str
            })

class Note:
    def __init__(self,note_name, note_description):
        self.note_name = note_name
        self.note_description = note_description
        
    def open_note_info(self):

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

    def draw(self, i, x):
        self.note_button = Button(
            text = self.note_name,
            command = "",
            
        )
        
        y_position = (i + 1 + x)*50 + 100
        
        self.note_button.place(
            x = 0,
            y = y_position,
            width = 200,
            height = 50
            
        )

    def save_note_to_csv(self, note_name, note_description):
        with open('notes.csv', mode = 'a', newline = '') as csv_file:
            fieldnames = ['Note Name', 'Note Description']
            writer = DictWriter(csv_file, fieldnames = fieldnames)
            writer.writerow({
                'Note Name' : note_name,
                'Note Description' : note_description
            })  
              