from tkinter import*

def label(a,b,text):
    window = Tk()
    window.title("Hello")
    window.geometry('300x300+'+str(a)+'+'+str(b))
    label=Label(window,text=text)
    label.pack()
    window.mainloop()

label(100,100,'Teky')