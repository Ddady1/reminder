import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
import os
import json
import subprocess


windll.shcore.SetProcessDpiAwareness(1)


# Create the main window

root = tk.Tk()
root.title('Reminder-Data Form')
root.geometry('700x500+250+250')
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


# product name

product_label = ttk.Label(root, text='Product Name:', foreground='blue', font=('Ariel', 10))
product_label.place(x=20, y=10)

product_entry = ttk.Entry(root, textvariable=product_name)
product_entry.place(x=115, y=10, width=200)
product_entry.focus()


# manufacture name

manufacture_label = ttk.Label(root, text='Manufacturer Name:', foreground='blue', font=('Ariel', 10))
manufacture_label.place(x=355, y=10)

manufacture_entry = ttk.Entry(root, textvariable=manufacturer)
manufacture_entry.place(x=480, y=10, width=200)


# supplier name

supplier_label = ttk.Label(root, text='Supplier Name:', foreground='blue', font=('Ariel', 10))
supplier_label.place(x=20, y=100)

supplier_entry = ttk.Entry(root, textvariable=supplier_name)
supplier_entry.place(x=115, y=100)


# start date

start_date_label = ttk.Label(root, text='Start Date:', foreground='blue', font=('Ariel', 10))
start_date_label.place(x=300, y=100)

start_date_entry = ttk.Entry(root, textvariable=start_date)
start_date_entry.place(x=370, y=100, width=80)


# expiration date

expired_date_label = ttk.Label(root, text='Expiration Date:', foreground='blue', font=('Ariel', 10))
expired_date_label.place(x=500, y=100)

expired_date_entry = ttk.Entry(root, textvariable=exp_date)
expired_date_entry.place(x=600, y=100, width=80)


# invoice number

inv_num_label = ttk.Label(root, text='Invoice Number:', foreground='blue', font=('Ariel', 10))
inv_num_label.place(x=20, y=190)

inv_num_entry = ttk.Entry(root, textvariable=invoice_no)
inv_num_entry.place(x=117, y=190)


# quantity

qty_label = ttk.Label(root, text='Quantity:', foreground='blue', font=('Ariel', 10))
qty_label.place(x=310, y=190)

qty_entry = ttk.Entry(root, textvariable=qty)
qty_entry.place(x=370, y=190, width=80)


# invoice date

inv_date_label = ttk.Label(root, text='Invoice Date:', foreground='blue', font=('Ariel', 10))
inv_date_label.place(x=520, y=190)

inv_date_entry = ttk.Entry(root, textvariable=invoice_date)
inv_date_entry.place(x=600, y=190, width=80)


# license number

lic_number_label = ttk.Label(root, text='License Number:', foreground='blue', font=('Ariel', 10))
lic_number_label.place(x=20, y=280)

lic_number_entry = ttk.Entry(root, textvariable=lic_no)
lic_number_entry.place(x=123, y=280, width=200)


# authorization number

auth_no_label = ttk.Label(root, text='Authorization Number:', foreground='blue', font=('Ariel', 10))
auth_no_label.place(x=345, y=280)

auth_no_entry = ttk.Entry(root, textvariable=autho_no)
auth_no_entry.place(x=480, y=280, width=200)














root.mainloop()