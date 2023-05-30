import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess
import os
from mysql.connector import connect, Error
import json
import time
#from sql_connection import connect_sql

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        # Create the main window
        #root = tk.Tk()
        self.title('Reminder')
        self.geometry('600x400+150+150')
        self.iconbitmap('assets/reminder.ico')
        self.create_menu()

    windll.shcore.SetProcessDpiAwareness(1)

    def check_json(self):
        path = 'assets/secret.json'
        if not os.path.isfile(path):
            self.yesno_popup()
        else:
            subprocess.call('mongoDB_checking.py', shell=True)
            '''from sql_connection import connect_sql
            connect_sql()'''





    def yesno_popup(self):
        answer = askyesno(title='First Setup', message='In order to connect to the database, some details are needed.\nWould you like to setup the connection now?\nYou can do it later from the Edit->Settings menu.')
        if answer:
            subprocess.call('first_setup.py', shell=True)

    def menu_about(self):
        showinfo(title='About', message='Reminder ver. 1.0.0\nBy David Hay Racha')


    def create_menu(self):
        # Create the menu bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Create the file menu
        file_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Print")
        file_menu.add_command(label="Export")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create the edit menu

        edit_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Add license...', command=lambda: subprocess.run(['python', 'insert_data_form.py']))
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
        help_menu.add_command(label="About", command=self.menu_about)



# Call first setup popup

###yesno_popup()





# Start the main event loop
#root.mainloop()


if __name__ == "__main__":
    app = App()
    app.check_json()
    app.mainloop()

    #app.mainloop()
