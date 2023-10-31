import tkinter as tk

def open_file():
    with open("Diary.txt", "r") as file:
        content = file.read()
        display_window(content)

def display_window(content):
    window = tk.Toplevel(root)
    window.title("Diary.txt")

    text_widget = tk.Text(window, wrap=tk.WORD)
    text_widget.pack(expand=tk.YES, fill=tk.BOTH)
    text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("Notepad")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)

root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

root.mainloop()
