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

    def draw(self, i):
        '''Создание кнопки для задачи'''
        self.task_button = Button(
        text = self.title,
        command = self.open_task_info
    )
        y_position = ((i + 1) * 50 + 100)
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
    