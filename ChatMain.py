import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def check_pin(event=None):  # Modified function to accept an event
    user_input = pin_entry.get()
    if user_input == '0945':
        root.destroy()
        os.system("python ChatWindow.py")
    else:
        messagebox.showinfo("Incorrect Pin", "Please enter the correct pin.", icon="warning")

root = tk.Tk()
root.title("Messenger")

# Set a fixed window size for the initial mini window
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Allow the window to be resizable
root.resizable(True, True)

# Load the image
image = Image.open("Chat/ChatPin.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Create input entry
pin_entry = tk.Entry(root, font=('Courier New', 28), foreground="black", width=18, show="*")
pin_entry.place(relx=0.5, rely=0.6, anchor="center")  # Moved down

# Create submit button
submit_button = tk.Button(root, text="Submit", command=check_pin, font=("Helvica", 20, "bold"))
submit_button.place(relx=0.75, rely=0.6, anchor="center")  # Slightly moved right

# Bind the Enter key to the check_pin function
pin_entry.bind('<Return>', check_pin)

# Start the main event loop
root.mainloop()
