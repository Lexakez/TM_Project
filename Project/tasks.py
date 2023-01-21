from tkinter import *

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
