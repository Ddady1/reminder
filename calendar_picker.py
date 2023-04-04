import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from ctypes import windll
from datetime import date


def update_label(event):
    date_label.config(text='Selected Date: ' + cal.get_date())
    # print(cal.get_date()) # for checking

def date_var():
    datevar = cal.get_date()
    print(datevar)
    quit(root.quit)

windll.shcore.SetProcessDpiAwareness(1)

text_color = 'DodgerBlue4'

# getting todays date

today = date.today()
todaysdate = today.strftime('%d/%m/%Y')




# Create the main window

root = tk.Tk()
root.title('Calendar')
root.geometry('400x330+350+350')
root.resizable(False, False)
root.iconbitmap('assets/reminder.ico')

#style = ttk.Style(root)
#style.theme_use('clam')


# creating calendar obj

cal = Calendar(root, selectmode='day',
               headersbackground='DodgerBlue4', headersforeground='white',
               normalforeground='DodgerBlue4', bordercolor='DodgerBlue4',
               showweeknumbers=False, background='DodgerBlue4', firstweekday='sunday', weekendays=[7],
               showothermonthdays=False, date_pattern='d/m/y')
cal.pack(pady=20)

cal.bind('<<CalendarSelected>>', update_label)

# date label

date_label = ttk.Label(root, foreground='DodgerBlue4', text='Selected Date: ' + cal.get_date())
date_label.pack(pady=20)
# print(cal.get_date()) # for checking


# create button

btn = tk.Button(root, text='Submit', fg='DodgerBlue4', command=date_var)
btn.pack()








root.mainloop()
