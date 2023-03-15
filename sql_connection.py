import time

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess
from mysql.connector import connect, Error
import json


windll.shcore.SetProcessDpiAwareness(1)


def connect_sql():

    with open('assets/secret.json') as f:
        config = json.load(f)

    try:
        with connect(
                host=config.get('sql_address'),
                user=config.get('db_username'),
                # password=getpass("Enter password: "),
                password=config.get('db_pass'),
                database=config.get('db_dbName')
        ) as connection:
            progress()
            #time.sleep(5)
            #sql_connection_label()
            #showinfo(title='sql', message='Connection with MySQL server was established')
            #print('Connection with MySQL server was established')
            #time.sleep(3)
            #check_db_exists(config.get('db_name'), connection)

    except Error as e:
            #print(e)
            showinfo(title='test', message=messages(5))


def progress():
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 5
        root.update_idletasks()
        time.sleep(0.2)

    else:
        #showinfo(message='The progress completed!')
        connection_status_label = ttk.Label(root, text=messages(1), foreground='green', font=('Ariel', 10))
        connection_status_label.place(x=10, y=60)

def messages(val):

    if val == 1:
        return 'Connection with MySQL server was established successfully'
    elif val == 2:
        return 'Database was created successfully'
    elif val == 3:
        return 'Tables were created successfully'
    elif val == 4:
        return 'Checking connectivity to SQL server:'
    elif val == 5:
        return 'Could not connect with MySQL. Please check connection details'
# Create the main window

root = tk.Tk()
root.title('Reminder')
root.geometry('600x400+250+250')
root.iconbitmap('assets/reminder.ico')


# PB sql connection label

sql_connection_label = ttk.Label(root, text=messages(4))
sql_connection_label.place(x=10, y=30)


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=300
)

# place the progressbar

pb.place(x=230, y=30, width=300)



connect_sql()

# Start the main event loop
root.mainloop()