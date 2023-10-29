from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk

def btn():
    messagebox.showinfo('Thong bao', combo.get())

window = Tk()
window.title("Form Đăng Ký")
window.geometry('800x200')

label1 = Label(window,text='Form Đăng Ký')
label1.place(x=250,y=100)

label2 = Label(window,text='Họ và Tên:')
label2.place(x=20,y=150)

entry2 = Entry(window)
entry2.place(x=100,y=150)

combo = Combobox(window, font=('Times New Roman', 15))
combo['values'] = ('Han Quoc', 'Nhat Ban', 'Viet Nam', 'Trung Quoc')
combo.current(3)
combo.place(x = 50, y = 50)

c1 = tk.Checkbutton(window, text='Python')
c1.pack()
c2 = tk.Checkbutton(window, text='C++')
c2.pack()

window.mainloop()