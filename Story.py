import tkinter as tk
from PIL import Image, ImageTk
import os

def on_click(event):
    root.destroy()
    os.system("python main.py")

# Create the main window
root = tk.Tk()
root.title("Phishing Awareness Game")

# Load the image
image = Image.open("Main Screen/Story.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Bind the click event to the on_click function
label.bind("<Button-1>", on_click)

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
# Start the main event loop
root.mainloop()
