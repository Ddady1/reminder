from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo') # Inserts text to explain in textbox
text['state'] = 'disabled' # Disabling from user to write in textbox. <'normal'> is default


text_cont = text.get('1.10', 'end') # Getting the content of textbox
print(text_cont)

root.mainloop()