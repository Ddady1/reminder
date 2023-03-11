import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess


windll.shcore.SetProcessDpiAwareness(1)

def yesno_popup():
    answer = askyesno(title='First Setup', message='Would you like to setup the connection now?\n You can do it later from the Edit->Settings')
    if answer:
        subprocess.call('first_setup.py', shell=True)

def menu_about():
    showinfo(title='About', message='Reminder ver. 1.0.0\nBy David Hay Racha')


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
edit_menu.add_separator()
edit_menu.add_command(label='Settings', command=lambda: subprocess.call('first_setup.py', shell=True))

# Create the view menu

view_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Show all')
view_menu.add_command(label='Show only expired')
view_menu.add_command(label='Show only valid')
view_menu.add_command(label='Show by manufacture')

# Create the help menu
help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=menu_about)

# Call first setup popup

yesno_popup()
# Start the main event loop
root.mainloop()
