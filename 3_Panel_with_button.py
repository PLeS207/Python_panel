import tkinter as tk


root1 = tk.Tk()
root2 = tk.Tk()
root3 = tk.Tk()

root1.title('Платформа 1')
root1.geometry('220x100+0+0')

root2.title('Платформа 2')
root2.geometry('220x100-0+0')

root3.title('Платформа 3')
root3.geometry('220x100+500-0')

b1 = tk.Button(root1, text='Кнопка 1')
b2 = tk.Button(root1, text='Кнопка 2')
b3 = tk.Button(root1, text='Кнопка 3')

c1 = tk.Button(root2, text='Кнопка 1')
c2 = tk.Button(root2, text='Кнопка 2')
c3 = tk.Button(root2, text='Кнопка 3')

a1 = tk.Button(root3, text='Кнопка 1')
a2 = tk.Button(root3, text='Кнопка 2')
a3 = tk.Button(root3, text='Кнопка 3')

b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=2, column=1, columnspan=2, sticky='we')

c1.grid(row=1, column=1)
c2.grid(row=1, column=2)
c3.grid(row=2, column=1, columnspan=2, sticky='we')

a1.grid(row=1, column=1)
a2.grid(row=1, column=2)
a3.grid(row=2, column=1, columnspan=2, sticky='we')
root1.mainloop()
