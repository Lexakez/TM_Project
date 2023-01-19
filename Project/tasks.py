from tkinter import *

class New_task:
    def __init__(self, title):
        self.title = title

    def draw(self, window):
        # Create the button for the task
        task_button = Button(text=self.title)
        task_button.place(
            window,
            y = 150, x = 0,
            width = 200,
            height = 50,
        )
