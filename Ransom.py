import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess  # Import the subprocess module
import os

def update_timer():
    global timer_value
    timer_value -= 1
    if timer_value % 60 >= 10:
        timer_label.config(text=f'Time left: {timer_value // 60}:{timer_value % 60} ', foreground="black", font=("Helvetica", 16, "bold"))
    else:
        timer_label.config(text=f'Time left: {timer_value // 60}:0{timer_value % 60} ', foreground="black", font=("Helvetica", 16, "bold"))
    if timer_value > 0:
        root.after(1000, update_timer)
    else:
        execute_lose()
        input_entry.pack_forget()
        submit_button.pack_forget()
        timer_label.pack_forget()
        root.after(3000, root.destroy)  # Close window after 3 seconds

def load_img(img_path):
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    canvas.itemconfig(image_item, image=img)
    canvas.image = img

def check_input(event=None):
    user_input = input_entry.get()
    if user_input == '1365':
        execute_win()
        input_entry.pack_forget()
        submit_button.pack_forget()
        timer_label.pack_forget()
        root.after(3000, root.destroy)  # Close window after 3 seconds
    else:
        messagebox.showinfo("Incorrect Input", "Please enter the correct code.", icon="warning")

def execute_win():
    subprocess.Popen(["python", "win.py"])
    

def execute_lose():
    subprocess.Popen(["python", "lose.py"])

def on_closing():
    pass  # Add any cleanup code you want here



root = tk.Tk()
root.title("Phishing Awareness Game")
root.geometry("600x400")  # Set window dimensions
root.resizable(False, False)  # Disable resizing

# Create canvas
canvas = tk.Canvas(root, width=600, height=400, background="black")
canvas.pack()

# Display initial image
image_item = canvas.create_image(300, 200, anchor='center')  # Reposition image

# Load initial image
load_img("ransom.png")

# Create timer label
timer_value = 600
timer_label = ttk.Label(root, text=f'Time left: {timer_value} seconds', foreground="black", font=("Helvetica", 16, "bold"))
timer_label.place(relx=0.5, rely=0.1, anchor="center")

# Create input entry
input_entry = ttk.Entry(root, font=('Helvetica', 16), foreground="black", width=20)
input_entry.place(relx=0.5, rely=0.9, anchor="center")
input_entry.bind('<Return>', check_input)

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=check_input, style="Submit.TButton")
submit_button.place(relx=0.85, rely=0.9, anchor="center")  # Adjust position

# Define custom ttk styles
style = ttk.Style()
style.configure("Submit.TButton", font=("Helvetica", 12, "bold"))

# Start the timer
update_timer()



root.mainloop()
