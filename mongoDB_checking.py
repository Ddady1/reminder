import time

###import mysql.connector

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess
###from mysql.connector import connect, Error
import json
from mogoDB_connect import client


windll.shcore.SetProcessDpiAwareness(1)
#dbExist = False

# For testing purposes
'''for db_name in client.list_database_names():
    print(db_name)'''

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
        return 'Could not connect with MySQL. Please check connection details and try again.'
    elif val == 6:
        return 'Database by this name already exists.\nWould like to overwrite it?\nCAUTION: Deleting the database will erase permanently all data in it!'
    elif val == 7:
        return 'Checking if Database already exists:'
    elif val == 8:
        return 'Old Database was deleted'
    elif val == 9:
        return 'Database already exists!!!'
    elif val == 10:
        return 'Creating Database:'
    elif val == 11:
        return 'Creating Tables:'
    elif val == 12:
        return 'Table by this name already exists.\nWould like to overwrite it?\nCAUTION: Deleting the table will erase permanently all data in it!'




# Create the main window

root = tk.Tk()
root.title('Reminder-DB connect')
root.geometry('600x400+250+250')
root.iconbitmap('assets/reminder.ico')


# PB sql connection label

sql_connection_label = ttk.Label(root, text=messages(4))
sql_connection_label.place(x=10, y=30)

# PB checking database existence label

db_exist_label = ttk.Label(root, text=messages(7))
db_exist_label.place(x=10, y=90)

# PB creating DB

db_create_label = ttk.Label(root, text=messages(10))
db_create_label.place(x=10, y=180)

# PB creating Tables

table_creat_label = ttk.Label(root, text=messages(11))
table_creat_label.place(x=10, y=240)


# cancel button

'''btn_cancel = tk.Button(root, text='Cancel', fg='DodgerBlue4', command=root.quit)
btn_cancel.place(x=400, y=330)'''


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=300
)

# place the progressbar

#pb.place(x=230, y=30, width=300)
#progressbar_position(230, 30, 300)



# Start the main event loop
root.mainloop()