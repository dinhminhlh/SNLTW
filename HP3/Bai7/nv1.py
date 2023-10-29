from tkinter import *
from tkinter import Menu

window = Tk()
window.title("My program")
#Khoi tao menu
menu = Menu(window)
window.config(menu=menu)
#Tao item trong menu
new_item = Menu(menu)
menu.add_cascade(label='File', menu=new_item)
#Them item(Hien thi lua chon o duoi menu)
new_item.add_command(label="New Text File")
new_item.add_command(label="New File...")
new_item.add_command(label="New window")
new_item.add_separator()  #Them duong ke
new_item.add_command(label="Exit", command=quit)

window.mainloop()
