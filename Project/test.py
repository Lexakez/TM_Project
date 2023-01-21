import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, bg='white', width=200, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a frame inside the canvas
frame = tk.Frame(canvas, bg='white')
canvas.create_window((0,0), window=frame, anchor='nw')

# Add buttons to the frame
for i in range(1,101):
    button = tk.Button(frame, text=f"Button {i}")
    button.pack()
    button.bind("<Button-1>")

# Update the scrollregion of the canvas
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Configure the scrollbar
canvas.config(yscrollcommand=scrollbar.set)

root.mainloop()
