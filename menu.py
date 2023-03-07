import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

def bt_click():
    print('Button clicked')

# Create the main window
root = tk.Tk()
root.title('Reminder')
root.geometry('600x400+150+150')
root.iconbitmap('assets/reminder.ico')

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save")
file_menu.add_command(label="Print")
file_menu.add_command(label="Export")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create the edit menu

edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Add license...')
edit_menu.add_command(label='Edit License...')
edit_menu.add_command(label='Delete license')

# Create the help menu
help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")


# Create button click with command attribute
button = ttk.Button(root, text='Click Me!', command=bt_click)
button.pack()

# Start the main event loop
root.mainloop()
