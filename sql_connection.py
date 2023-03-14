import time

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess
from mysql.connector import connect, Error
import json


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
            showinfo(title='test', message='not working')


def progress():
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 5
        root.update_idletasks()
        time.sleep(0.2)

    else:
        #showinfo(message='The progress completed!')
        connection_status_label = ttk.Label(root, text='Connection with MySQL server was established', foreground='green')
        connection_status_label.place(x=10, y=60)

def sql_connection_label():
    connection_status_label = ttk.Label(root, text='Connection with MySQL server was established', foreground='green')
    connection_status_label.place(x=10, y=60)

# Create the main window
root = tk.Tk()
root.title('Reminder')
root.geometry('600x400+250+250')
root.iconbitmap('assets/reminder.ico')


# PB sql connection label
sql_connection_label = ttk.Label(root, text='Checking connectivity to SQL server:')
sql_connection_label.place(x=10, y=30)


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=300
)

# place the progressbar
#pb.grid(column=0, row=0, columnspan=2, padx=100, pady=20)
pb.place(x=230, y=30, width=300)

# PB sql connection status

#connection_status_label = ttk.Label(root, text='Connection with MySQL server was established', foreground='green')
#connection_status_label.place(x=10, y=60)


connect_sql()

# Start the main event loop
root.mainloop()