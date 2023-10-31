import tkinter as tk
from tkinter import PhotoImage
import os

def on_hover(event):
    if 900 <= event.x <= 1077 and 269 <= event.y <= 322:
        canvas.itemconfig(image_item, image=img2)
    elif 900 <= event.x <= 1077 and 469 <= event.y <= 522:
        canvas.itemconfig(image_item, image=img3)
    else:
        canvas.itemconfig(image_item, image=img1)

def on_click(event):
    if 900 <= event.x <= 1077 and 269 <= event.y <= 322:
        os.system('python EmailScreen.py')
    if 900 <= event.x <= 1077 and 469 <= event.y <= 522:
        os.system('python Story.py')
    root.destroy()


root = tk.Tk()
root.title("Phishing Awareness Game")

img1 = PhotoImage(file="Main Screen/Title1.png")
img2 = PhotoImage(file="Main Screen/Title2.png")
img3 = PhotoImage(file="Main Screen/Title3.png")
img4 = PhotoImage(file="Main Screen/Story.png")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set canvas dimensions
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()

image_item = canvas.create_image(screen_width // 2, screen_height // 2, image=img1)

canvas.bind("<Motion>", on_hover)
canvas.bind("<Button-1>", on_click)

# Fullscreen toggle
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.mainloop()
