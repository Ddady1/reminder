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















root.mainloop()