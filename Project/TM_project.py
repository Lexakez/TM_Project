from tkinter import *
from tkinter import ttk
from main_window import *
from tasks import *
from PIL import ImageTk, Image

window_size = "600x700"
Screen = Tk()

main_window(window_size, Screen)
trash_button()
delete_all_button()
add_task_button(Screen)

image = Image.open("logo.png")
image = image.resize((120, 100), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(image)
logo = Label(image = logo_image)
logo.place(
    x = 210, y = 0,
)

Screen.mainloop()