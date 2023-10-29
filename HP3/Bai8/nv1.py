from tkinter import *
from tkinter import messagebox

def thongbao():
    messagebox.showinfo('Thong bao','Dang nhap thanh cong')

def formdangky():
    window2 = Tk()
    window2.title("Dang ky")
    window2.geometry('400x400')
    taikhoan = Label(window,text="Tai khoan: ")
    taikhoan.place(x=50, y=30)
    matkhau = Label(window,text="Mat khau: ")
    matkhau.place(x=50, y = 60)

window = Tk()
window.title("My program")
window.geometry('400x200')

taikhoan = Label(window,text="Tai khoan: ")
taikhoan.place(x=50, y=30)
matkhau = Label(window,text="Mat khau: ")
matkhau.place(x=50, y = 60)

textbox1 = Entry(window)
textbox1.place(x = 120, y = 30)
textbox2 = Entry(window,show='*')
textbox2.place(x = 120, y = 60)

btn1=Button(window,text="Dang nhap",command=thongbao)
btn1.place(x=80,y=90)
btn2=Button(window,text="Dang ky")
btn2.place(x=190,y=90)

window.mainloop()