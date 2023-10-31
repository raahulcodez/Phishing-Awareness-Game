import tkinter as tk
from tkinter import PhotoImage
import os

def on_hover(event):
    if 195 <= event.x <= 345 and 469 <= event.y <= 522:
        canvas.itemconfig(image_item, image = img2)
    elif 900 <= event.x <= 1077 and 469 <= event.y <= 522:
        canvas.itemconfig(image_item, image = img3)
    else:
        canvas.itemconfig(image_item, image = img1)


def on_click(event):
    if 195 <= event.x <= 345 and 469 <= event.y <= 522:
        os.system('python EmailScreen.py')
        root.destroy()
    if 900 <= event.x <= 1077 and 469 <= event.y <= 522:
        root.destroy()

root = tk.Tk()
root.title("Phishing Awareness Game - You lost")

img1 = PhotoImage(file = "GameOver/lose1.png")
img2 = PhotoImage(file = "GameOver/lose2.png")
img3 = PhotoImage(file = "GameOver/lose3.png")

canvas = tk.Canvas(root, width = 1280, height = 720)
canvas.pack()

image_item = canvas.create_image(640, 360, image = img1)

canvas.bind("<Motion>", on_hover)
canvas.bind("<Button-1>", on_click)
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
root.mainloop()

