import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import os
import json
import subprocess
from PIL import ImageTk, Image
import time
from tktooltip import ToolTip
windll.shcore.SetProcessDpiAwareness(1)



def check_json():
    path = 'assets/secret.json'
    if os.path.isfile(path):
        confirm()
    write_json(var_list, var_list_string)


def write_json(var_list, string_list):
    first_run_time = time.time()
    string_list.append('first_run_time')
    var_list.append(first_run_time)
    dict = {}
    i = 0
    for var in var_list:
        con = var.get()
        dict[string_list[i]] = con
        i += 1

    js_object = json.dumps(dict, indent=4)
    with open('assets/secret.json', 'w') as f:
        f.write(js_object)
    #from sql_connection import connect_sql
    #connect_sql()
    subprocess.call('sql_connection.py', shell=True)

def cancel_bt():
    root.quit()

def clear_bt(entries):
    for en in entries:
        en.delete(0, 'end')

def confirm():

    answer = askyesno(title='confirmation', message='The file already exists. Would like to overwrite it?')
    if answer:
        write_json(var_list, var_list_string)

def check_fields():
    for var in var_list:
        con = var.get()
        if con == '':
            bt_stat = tk.DISABLED
            return bt_stat
        else:
            bt_stat = tk.NORMAL
            return bt_stat



# Create root window

root = tk.Tk()
root.title('Reminder-Initial setup')
root.geometry('600x450+250+250')
root.resizable(False, False)
root.iconbitmap('assets/reminder.ico')

# Creating exclamation mark image

exclamation_image = Image.open('assets/exclamation_trans.png')
exclamation_image = exclamation_image.resize((20, 15), Image.LANCZOS)
exclamation_image_lab = ImageTk.PhotoImage(exclamation_image)

# Create variables

sql_address = tk.StringVar()
db_username = tk.StringVar()
db_pass = tk.StringVar()
db_port = tk.StringVar()
db_dbName = tk.StringVar()
db_freq = tk.StringVar()

var_list = [sql_address, db_username, db_pass, db_port, db_dbName, db_freq]
var_list_string = ['sql_address', 'db_username', 'db_pass', 'db_port', 'db_dbName', 'db_check_freq']

# Setup grid

'''setup = ttk.Frame(root)
setup.pack(padx=10, pady=10, fill='x', expand=True)'''

# Label frame

lf = ttk.Labelframe(root, text='SQL Connection details:')
lf.pack(fill='both', ipadx=10, ipady=50, padx=50, pady=20, anchor=tk.NW)


# SQL address

sql_address_label = ttk.Label(lf, text='SQL server address:')
sql_address_label.pack(fill='x', expand=True)
sql_address_exa = ttk.Label(image=exclamation_image_lab)
sql_address_exa.place(x=155, y=42)
ToolTip(sql_address_exa, msg='-The address of the SQL server')

sql_address_entry = ttk.Entry(lf, textvariable=sql_address)
sql_address_entry.pack(fill='x', expand=True)
sql_address_entry.focus()

# DB username

db_username_label = ttk.Label(lf, text='DB Username:')
db_username_label.pack(fill='x', expand=True)
db_username_exa = ttk.Label(image=exclamation_image_lab)
db_username_exa.place(x=130, y=98)
ToolTip(db_username_exa, msg='-The username that was created with the DB')

db_username_entry = ttk.Entry(lf, textvariable=db_username)
db_username_entry.pack(fill='x', expand=True)

# DB password

db_pass_label = ttk.Label(lf, text='DB password:')
db_pass_label.pack(fill='x', expand=True)
db_pass_exa = ttk.Label(image=exclamation_image_lab)
db_pass_exa.place(x=125, y=154)
ToolTip(db_pass_exa, msg='-The related username password')

db_pass_entry = ttk.Entry(lf, textvariable=db_pass, show='*')
db_pass_entry.pack(fill='x', expand=True)

# DB port

db_port_label = ttk.Label(lf, text='DB port: (Default: 3306)')
db_port_label.pack(fill='x', expand=True)
db_port_exa = ttk.Label(image=exclamation_image_lab)
db_port_exa.place(x=175, y=210)
ToolTip(db_port_exa, msg='-The default port is 3306.\nYou can change it according to your needs.')

db_port_entry = ttk.Entry(lf, textvariable=db_port)
db_port_entry.insert(0, '3306')
db_port_entry.pack(fill='x', expand=True)

# DB dbName

db_dbName_label = ttk.Label(lf, text='DB name: (Default: licenses)')
db_dbName_label.pack(fill='x', expand=True)
db_dbName_exa = ttk.Label(image=exclamation_image_lab)
db_dbName_exa.place(x=200, y=266)
ToolTip(db_dbName_exa, msg='-The default DB name is licenses,\nbut you can change it according to your needs.')

db_dbName_entry = ttk.Entry(lf, textvariable=db_dbName)
db_dbName_entry.insert(0, 'licenses')
db_dbName_entry.pack(fill='x', expand=True)

#  DB checking frequency

db_freq_label = ttk.Label(lf, text='DB existence checking frequency: (Default: always=0)')
db_freq_label.pack(fill='x', expand=True)
db_freq_exa = ttk.Label(image=exclamation_image_lab)
db_freq_exa.place(x=335, y=324)
ToolTip(db_freq_exa, msg='-How frequantly do you want the program to check the existence of the DB and tables.\n'
                         'The default is 0=Always, which means everytime you run the program.\n'
                         '1 is once a day. 2 is every 2 days since first run and etc.')

db_freq_entry = ttk.Entry(lf, textvariable=db_freq)
db_freq_entry.insert(0, 0)
db_freq_entry.pack(fill='x', expand=True)

# Save button (need to be correct)
#https://www.pythontutorial.net/tkinter/tkinter-validation/
#https://www.tutorialspoint.com/how-to-interactively-validate-an-entry-widget-content-in-tkinter
#bt_stat = check_fields()

save_button = ttk.Button(lf, text='Save', command=check_json)
save_button.pack(side='left', ipadx=5, ipady=5, expand=True)

# Clear button

entries_list = [sql_address_entry, db_username_entry, db_pass_entry, db_port_entry, db_dbName_entry, db_freq_entry]
clear_button = ttk.Button(lf, text='Clear all', command=lambda: clear_bt(entries_list))
clear_button.pack(side='left', ipadx=5, ipady=5, expand=True)


# Cancel button

cancel_button = ttk.Button(lf, text='Cancel', command=cancel_bt)
cancel_button.pack(side='left', ipadx=5, ipady=5, expand=True)




root.mainloop()