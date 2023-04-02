import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from ctypes import windll
from datetime import date

windll.shcore.SetProcessDpiAwareness(1)

text_color = 'DodgerBlue4'

# getting todays date

today = date.today()
todaysdate = today.strftime('%d/%m/%Y')




# Create the main window

root = tk.Tk()
root.title('Calendar')
root.geometry('400x400+350+350')
root.resizable(False, False)
root.iconbitmap('assets/reminder.ico')

#style = ttk.Style(root)
#style.theme_use('clam')


# creating calendar obj

cal = Calendar(root, selectmode='day', year=2023, month=4, date=2,
               headersbackground='DodgerBlue4', headersforeground='white',
               normalforeground='DodgerBlue4', bordercolor='DodgerBlue4',
               showweeknumbers=False, background='DodgerBlue4', firstweekday='sunday', weekendays=[6, 7],
               showothermonthdays=False)
cal.pack(pady=40)


# create button

btn = ttk.Button(root, text='Submit')
btn.pack()




root.mainloop()
