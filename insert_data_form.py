#import calendar_picker
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import os
import json
import subprocess
#import calendar_picker

def get_start(e):
    start_date_entry.delete(0, 'end')
    #result = subprocess.check_output(['python', 'calendar_picker.py'], text=True)
    result = subprocess.run(['python', 'calendar_picker.py'], capture_output=True, text=True)
    start_date_entry.insert(0, result.stdout.rstrip())


def get_expired(e):
    expired_date_entry.delete(0, 'end')
    #result = subprocess.check_output(['python', 'calendar_picker.py'], text=True)
    result = subprocess.run(['python', 'calendar_picker.py'], capture_output=True, text=True)
    expired_date_entry.insert(0, result.stdout.rstrip())


def get_inv_date(e):
    inv_date_entry.delete(0, 'end')
    result = subprocess.run(['python', 'calendar_picker.py'], capture_output=True, text=True)
    inv_date_entry.insert(0, result.stdout.rstrip())



windll.shcore.SetProcessDpiAwareness(1)

text_color = 'DodgerBlue4'

# Create the main window

root = tk.Tk()
root.title('Reminder-Data Form')
root.geometry('450x800+250+250')
root.resizable(False, False)
root.iconbitmap('assets/reminder.ico')


# Create variables

product_name = tk.StringVar()
manufacturer = tk.StringVar()
supplier_name = tk.StringVar()
start_date = tk.StringVar()
exp_date = tk.StringVar()
invoice_no = tk.StringVar()
qty = tk.StringVar()
invoice_date = tk.StringVar()
lic_no = tk.StringVar()
autho_no = tk.StringVar()
person_Fname = tk.StringVar()
person_Lname = tk.StringVar()
person_email = tk.StringVar()
person_mobile = tk.StringVar()


# main window label

main_label = ttk.Label(root, text='Licenses Information Form', foreground=text_color, font=('Ariel', 14, 'bold'))
main_label.place(x=100, y=10)


# product name

product_label = ttk.Label(root, text='Product Name:', foreground=text_color, font=('Ariel', 10))
product_label.place(x=20, y=50)

product_entry = ttk.Entry(root, textvariable=product_name)
product_entry.place(x=20, y=70, width=300)
product_entry.focus()


# manufacture name

manufacture_label = ttk.Label(root, text='Manufacturer Name:', foreground=text_color, font=('Ariel', 10))
manufacture_label.place(x=20, y=100)

manufacture_entry = ttk.Entry(root, textvariable=manufacturer)
manufacture_entry.place(x=20, y=120, width=300)


# supplier name

supplier_label = ttk.Label(root, text='Supplier Name:', foreground=text_color, font=('Ariel', 10))
supplier_label.place(x=20, y=150)

supplier_entry = ttk.Entry(root, textvariable=supplier_name)
supplier_entry.place(x=20, y=170)


# start date

start_date_label = ttk.Label(root, text='Start Date:', foreground=text_color, font=('Ariel', 10))
start_date_label.place(x=20, y=200)

start_date_entry = ttk.Entry(root, textvariable=start_date)
#start_date_entry.insert(0, 'dd/mm/yyyy')
start_date_entry.place(x=20, y=220, width=80)
start_date_entry.bind('<FocusIn>', get_start)



# expiration date

expired_date_label = ttk.Label(root, text='Expiration Date:', foreground=text_color, font=('Ariel', 10))
expired_date_label.place(x=200, y=200)

expired_date_entry = ttk.Entry(root, textvariable=exp_date)
expired_date_entry.place(x=200, y=220, width=80)
expired_date_entry.bind('<FocusIn>', get_expired)


# invoice number

inv_num_label = ttk.Label(root, text='Invoice Number:', foreground=text_color, font=('Ariel', 10))
inv_num_label.place(x=20, y=250)

inv_num_entry = ttk.Entry(root, textvariable=invoice_no)
inv_num_entry.place(x=20, y=270)


# quantity

qty_label = ttk.Label(root, text='Quantity:', foreground=text_color, font=('Ariel', 10))
qty_label.place(x=20, y=300)

qty_entry = ttk.Entry(root, textvariable=qty)
qty_entry.place(x=20, y=320, width=80)


# invoice date

inv_date_label = ttk.Label(root, text='Invoice Date:', foreground=text_color, font=('Ariel', 10))
inv_date_label.place(x=20, y=350)

inv_date_entry = ttk.Entry(root, textvariable=invoice_date)
inv_date_entry.place(x=20, y=370, width=80)
inv_date_entry.bind('<FocusIn>', get_inv_date)


# license number

lic_number_label = ttk.Label(root, text='License Number:', foreground=text_color, font=('Ariel', 10))
lic_number_label.place(x=20, y=400)

lic_number_entry = ttk.Entry(root, textvariable=lic_no)
lic_number_entry.place(x=20, y=420, width=300)


# authorization number

auth_no_label = ttk.Label(root, text='Authorization Number:', foreground=text_color, font=('Ariel', 10))
auth_no_label.place(x=20, y=450)

auth_no_entry = ttk.Entry(root, textvariable=autho_no)
auth_no_entry.place(x=20, y=470, width=300)


# line seperator with label

seperator = ttk.Separator(root, orient='horizontal')
seperator.place(x=18, y=500, width=400)
sep_contact_label = ttk.Label(root, text='Contact person information', foreground=text_color, font=('Ariel', 10, 'bold'))
sep_contact_label.place(x=20, y=510)


# contact first name

first_name_label = ttk.Label(root, text='First Name:', foreground=text_color, font=('Ariel', 10))
first_name_label.place(x=20, y=540)

first_name_entry = ttk.Entry(root, textvariable=person_Fname)
first_name_entry.place(x=20, y=560)


# contact last name

last_name_label = ttk.Label(root, text='Last Name:', foreground=text_color, font=('Ariel', 10))
last_name_label.place(x=195, y=540)

last_name_entry = ttk.Entry(root, textvariable=person_Lname)
last_name_entry.place(x=195, y=560)


# contact email

email_label = ttk.Label(root, text='Email Address:', foreground=text_color, font=('Ariel', 10))
email_label.place(x=20, y=590)

email_entry = ttk.Entry(root, textvariable=person_email)
email_entry.place(x=20, y=610, width=250)


# contact mobile

mobile_label = ttk.Label(root, text='Phone\Mobile number:', foreground=text_color, font=('Ariel', 10))
mobile_label.place(x=20, y=640)

mobile_entry = ttk.Entry(root, textvariable=person_mobile)
mobile_entry.place(x=20, y=670)









root.mainloop()