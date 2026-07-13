import os
from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window =Tk()
window.geometry('600x800')

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
image_path = os.path.join(os.path.dirname(__file__), 'images', 'logo.png')
image =PhotoImage(file=image_path)
label=Label(window,image=image)
label.place(x=0,y=0)
window.mainloop()