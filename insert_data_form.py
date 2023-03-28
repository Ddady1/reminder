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
root.geometry('800x500+250+250')
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
product_entry.place(x=115, y=10, width=300)
product_entry.focus()


# manufacture name

manufacture_label = ttk.Label(root, text='Manufaturer Name:', foreground='blue', font=('Ariel', 10))
manufacture_label.place(x=450, y=10)

manufacture_entry = ttk.Entry(root, textvariable=manufacturer)
manufacture_entry.place(x=565, y=10, width=200)


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















root.mainloop()