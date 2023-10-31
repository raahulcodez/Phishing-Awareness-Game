from tkinter import Tk, Canvas
from PIL import Image, ImageTk
import os
import subprocess

def on_hover(event):
    if 409 <= event.x <= 614 and 348 <= event.y <= 400:
        canvas.itemconfig(image_item, image=img2)
    else:
        canvas.itemconfig(image_item, image=img1)

def on_click(event):
    if 409 <= event.x <= 614 and 348 <= event.y <= 403:
        root.destroy()
        subprocess.Popen(['python','Ransom.py'])
        subprocess.Popen(['python', 'Notepadclue.py'])
        subprocess.Popen(['python', 'ChatMain.py'])

root = Tk()
root.title("Gmail")

img1 = ImageTk.PhotoImage(Image.open("EmailScreens/Email1.png"))
img2 = ImageTk.PhotoImage(Image.open("EmailScreens/Email2.png"))

canvas = Canvas(root, width=1280, height=720)
canvas.pack()

image_item = canvas.create_image(640, 360, image=img1)

canvas.bind("<Motion>", on_hover)
canvas.bind("<Button-1>", on_click)
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
root.mainloop()
