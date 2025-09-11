from tkinter import *
def drag_start(event):
 wiget=event.widget
 wiget.startX=event.x
 wiget.startY=event.y
def drop_motion(event):
 wiget = event.widget
 x=wiget.winfo_x()-wiget.startX+event.x
 y = wiget.winfo_y() - wiget.startY + event.y
 wiget.place(x=x,y=y)
window =Tk()
label =Label(window,bg='red',width=15,height=12)
label.place(x=0,y=0)
label2 =Label(window,bg='green',width=15,height=10)
label2.place(x=200,y=150)
label.bind('<Button-1>',drag_start)
label.bind('<B1-Motion>',drop_motion)
label2.bind('<Button-1>',drag_start)
label2.bind('<B1-Motion>',drop_motion)
window.mainloop()
