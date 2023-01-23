from tkinter import *
from csv import *

class New_task:
    def __init__(self, title):
        self.title = title

    def draw(self, title, task_list):
        '''Создание кнопки для задачи'''
        task_button = Button(
        text = self.title,
        command = ""
    )
        y_position = (len(task_list) * 50 + 100)
        task_button.place(
            y = y_position, x = 0,
            width = 200,
            height = 50,
    )
    def save_task_to_csv(self, task_name, task_description):
        # Open the CSV file for writing
        with open('tasks.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Task Name', 'Task Description']
            writer = DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Convert the goals list to a string
            # goals_str = ','.join(goals)

            # Write the task information as a row
            writer.writerow({'Task Name': task_name, 'Task Description': task_description})