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
#dbExist = False

def connect_sql(flag):

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
            password=config.get('db_pass'),
            database=config.get('db_dbName')
        )
        if not flag:
            return connection
        progressbar_position(230, 30, 300)
        progress(10, 60, 1, 'green')

    except Error as e:
        showinfo(title='Connection error.', message=messages(5))

    return connection

def progress_fake():
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 5
        root.update_idletasks()
        time.sleep(0.2)



def progress(xval, yval, msg, color):
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 5
        root.update_idletasks()
        time.sleep(0.2)

    else:
        #showinfo(message='The progress completed!')
        #connection_status_label = ttk.Label(root, text=messages(msg), foreground='green', font=('Ariel', 10))
        #connection_status_label.place(x=xval, y=yval)
        result_labels_position(xval, yval, msg, color)


def progressbar_position(xval, yval, width):

    pb.place(x=xval, y=yval, width=width)


def result_labels_position(xval, yval, msg, color):

    result_labels = ttk.Label(root, text=messages(msg), foreground=color, font=('Ariel', 10))
    result_labels.place(x=xval, y=yval)


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

def check_db_exist(con):

    progressbar_position(230, 90, 300)
    #progress(10, 120, 9, 'red')
    progress_fake()
    db = con.cursor()
    db.execute('show databases')
    lst = db.fetchall()
    i = 0
    while i < len(lst):
        if config.get('db_dbName') in lst[i]:
            result_labels_position(10, 120, 9, 'red')
            #global dbExist
            #dbExist = True
            answer = askyesno(title='DB status', message=messages(6))
            if answer:
                db.execute('DROP DATABASE ' + config.get('db_dbName')) # NEED TO UNTAG THIS LINE ON PRODUCTION
                result_labels_position(10, 150, 8, 'red')
                create_db(con)
                break

                # check tables existance code
            else:
                create_table(con)
                #check_table_exist(con)
                #show_db(con) # for checking purposes
                break
        else:
            i += 1
    #create_db(con)


def create_db(con):

    dbname = config.get('db_dbName')
    create_db_query = f'CREATE DATABASE {dbname}'

    try:
        with con.cursor() as cursor:
            cursor.execute(create_db_query)
            progressbar_position(230, 180, 300)
            progress(10, 210, 2, 'green')
    except Error as e:
        showinfo(title='Error Creating DB', message=e)

    #check_table_exist(con)
    create_table(con)


def check_table_exist(con):


    show_table = 'DESCRIBE license'
    try:
        with con.cursor() as cursor:
            cursor.execute(show_table)
            result = cursor.fetchall()
            print(result)
            for row in result:
                print(row)
    except Error as e:
        showinfo(title='Error Checking Table', message=e)


def create_table(con):

    con = connect_sql(False)
    create_table_q = '''
    CREATE TABLE lic (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first VARCHAR(100)
    )
    '''

    try:
        with con.cursor() as cursor:
            cursor.execute(create_table_q)
            con.commit()

    except Error as e:
        showinfo(title='Error Creating Table', message=e)

    #show_tables()


# For checking puposes

'''def show_tables():

    con = connect_sql(False)
    with con.cursor() as cursor:
        cursor.execute('SHOW TABLES')
        for t in cursor:
            print(t)'''


# for checking purposes
'''def show_db(con):
        # Show DB
    show_db_query = "SHOW DATABASES"
    with con.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)'''


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

# PB creating DB

db_create_label = ttk.Label(root, text=messages(10))
db_create_label.place(x=10, y=180)


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



con = connect_sql(True)

check_db_exist(con)

# Start the main event loop
root.mainloop()