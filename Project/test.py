from tkinter import Listbox
from tkinter import *

root = Tk()
# Create a Listbox
my_listbox = Listbox(root)
my_listbox.pack()

# Insert some items into the Listbox
for i in range(5):
    my_listbox.insert(END, "Item " + str(i))

# Get the selected items from the Listbox
selected_items = my_listbox.get(ACTIVE)
print(selected_items)
print(list(my_listbox.get(0, END)))
root.mainloop()