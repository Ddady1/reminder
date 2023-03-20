import time

import mysql.connector

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import subprocess
from mysql.connector import connect, Error
import json


windll.shcore.SetProcessDpiAwareness(1)


def connect_sql():

    #global con
    global config

    with open('assets/secret.json') as f:
        config = json.load(f)

    '''try:
        with connect(
                host=config.get('sql_address'),
                user=config.get('db_username'),
                # password=getpass("Enter password: "),
                password=config.get('db_pass'),
                database=config.get('db_dbName')
        ) as connection:
            con = connection
            progress(10, 60, 1)


    except Error as e:
            #print(e)
            showinfo(title='Connection error.', message=messages(5))

    return con'''

    connection = None
    try:
        connection = mysql.connector.Connect(
            host=config.get('sql_address'),
            user=config.get('db_username'),
            password=config.get('db_pass')
        )
        progress(10, 60, 1)

    except Error as e:
        showinfo(title='Connection error.', message=messages(5))

    return connection


def progress(xval, yval, msg):
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 5
        root.update_idletasks()
        time.sleep(0.2)

    else:
        #showinfo(message='The progress completed!')
        connection_status_label = ttk.Label(root, text=messages(msg), foreground='green', font=('Ariel', 10))
        connection_status_label.place(x=xval, y=yval)


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

def check_db_exist(con):

    db = con.cursor()
    db.execute('show databases')
    lst = db.fetchall()
    i = 0
    while i < len(lst):
        if config.get('db_dbName') in lst[i]:
            answer = askyesno(title='DB status', message=messages(6))
            if answer:
                print('Deleting db')
                #db.execute('DROP DATABASE ' + config.get('db_dbName')) # NEED TO UNTAG THIS LINE ON PRODUCTION
                # check tables existance code
        else:
            i += 1
    #create_db()


def create_db():
    dbname = config.get('db_dbName')
    create_db_query = f'CREATE DATABASE {dbname}'

    try:
        with con.cursor() as cursor:
            cursor.execute(create_db_query)
            progress(10, 120, 2)
    except Error as e:
        showinfo(title='Error', message=e)

# Create the main window

root = tk.Tk()
root.title('Reminder')
root.geometry('600x400+250+250')
root.iconbitmap('assets/reminder.ico')


# PB sql connection label

sql_connection_label = ttk.Label(root, text=messages(4))
sql_connection_label.place(x=10, y=30)

# PB checking database existence label

db_exist_label = ttk.Label(root, text=messages(7))
db_exist_label.place(x=10, y=90)


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=300
)

# place the progressbar

pb.place(x=230, y=30, width=300)



con = connect_sql()

check_db_exist(con)

# Start the main event loop
root.mainloop()