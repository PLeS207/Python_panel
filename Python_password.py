from tkinter import *
from tkinter.ttk import *
import time


def show():
    p = password.get()
    print(p)
    time.sleep(30)
    root.destroy()


root = Tk()

root.title('Платформа 1')
root.geometry('220x100+0+0')

password = StringVar()
passEntry = Entry(root, textvariable=password, show='*').pack()
submit = Button(root, text='Show Console', command=show).pack()
root.mainloop()
