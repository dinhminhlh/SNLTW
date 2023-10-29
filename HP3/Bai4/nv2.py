from tkinter import*

window = Tk()
window.geometry("400x250")

label=Label(window,text="LOGIN")
label.pack()

Id=Label(window,text="ID:").place(x=30,y=50)
Password=Label(window,text="Password:").place(x=30,y=90)
e1=Entry(window).place(x=110,y=50)
e2=Entry(window,show='*').place(x=110,y=90)

login=Button(window,text="Login").place(x=90,y=120)
quit=Button(window,text="Quit").place(x=200,y=120)

window.mainloop()