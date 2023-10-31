import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser  

def check_pin(event=None):
    user_input = pin_entry.get()
    if user_input == '2204':
        webbrowser.open("https://aerial-diagnostic-576.notion.site/Film-Diary-22-a91c52d5b83f425287cc4cfefa0932be?pvs=4")
        root.destroy()
    else:
        messagebox.showinfo("Incorrect Pin", "Please enter the correct pin.", icon="warning")

def close_window():
    messagebox.showinfo("Time's up!", "You took too long to enter the pin. Closing the window.")
    root.destroy()

root = tk.Tk()
root.title("Redirecting...")

window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")
root.resizable(True, True)

image = Image.open("Chat/Kendrick.png")
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()

pin_entry = tk.Entry(root, font=('Courier New', 28), foreground="black", width=18, show="*")
pin_entry.place(relx=0.5, rely=0.7, anchor="center")  # Lowered the text box down

submit_button = tk.Button(root, text="Submit", command=check_pin, font=("Helvica", 20, "bold"))
submit_button.place(relx=0.75, rely=0.7, anchor="center")  # Adjusted the button position

pin_entry.bind('<Return>', check_pin)

# Schedule the close_window function to run after 45 seconds (45000 milliseconds)
root.after(45000, close_window)

root.mainloop()
