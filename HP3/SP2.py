from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
# your code goes hereimport tkinter as tk
from tkinter import messagebox

login_window = tk.Tk()
login_window.geometry('300x200')
login_window.title("dang nhap")


# Hàm kiểm tra tài khoản và mật khẩu
def authenticate():
  username = username_entry.get()
  password = password_entry.get()

  # Ở đây, bạn có thể thêm kiểm tra tài khoản và mật khẩu
  # Nếu đúng, hiển thị cửa sổ chính, ngược lại thông báo lỗi đăng nhập.
  if username == "nhan" and password == "tm":
    show_main_window()
  
  else:
    messagebox.showerror("Lỗi đăng nhập","Tài khoản hoặc mật khẩu không đúng.")




# Hàm để hiển thị cửa sổ chính sau khi đăng nhập thành công
def show_main_window():
  window1 = tk.Tk()
  window1.title('nhà hàng')
  window1.geometry('500x300')
  
  def order():
    customer = customer_entry.get()

    messagebox.showinfo("bạn đã đặt hàng thành công!", "đơn hàng của bạn sẽ sớm được nhận về bạn.")
    print(" => hóa đơn:")
    
    print("+ họ tên: ", customer)

    st = sdt.get()
    print("+ số điện thoại: ", st)

    dcs = dc.get()
    print("+ địa chỉ:", dcs)

    MA = combo.get()
    print("+ món ăn: ", MA)

    DA= combo2.get()
    print("+ nước uống: ", DA)
    
  text1 = Label(window1, text="xin chào")
  text1.place(x=65, y=10)
  text2 = Label(window1, text="đến với nhà hàng của chúng tôi")
  text2.place(x=0, y=30)

  combo = Combobox(window1, font=('Time New Roman', 10))
  combo['value'] = ('phở bò tái', 'phở gà', 'cơm rang dưa bò',
                    'bánh mì thịt dưa bò', 'bún đậu mắm tôm', 'bún riêu cua',
                    'bún bò huế')
  combo.current(3)
  combo.place(x=10, y=100)

  combo2 = Combobox(window1, font=('Time New Roman', 10))
  combo2['value'] = ('sting dâu tây', 'pepsi', 'coca cola', 'aquafina', 'C2',
                     'chanh muối', 'Bia hà nội', 'không cần')
  combo2.current(3)
  combo2.place(x=10, y=160)

  text3 = Label(
      window1,
      text="+ xin vui lòng chọn món ăn bạn muốn ăn:",
  )
  text3.place(x=0, y=70)

  text4 = Label(window1, text="+ chọn đồ uống ở đây (ko cũng đc):")
  text4.place(x=0, y=130)

  customer_label = tk.Label(window1, text="họ tên khách hàng:")
  customer_label.place(x=300, y=10)
  customer_entry = tk.Entry(window1)
  customer_entry.place(x=300, y=30)

  text5 = Label(window1, text="số điện thoại:")
  text5.place(x=300, y=60)
  sdt = Entry(window1)
  sdt.place(x=300, y=90)

  text6 = Label(window1, text="địa chỉ:")
  text6.place(x=300, y=130)
  dc = Entry(window1)
  dc.place(x=300, y=150)

  B = Button(window1, text="đặt hàng", command=order)
  B.place(x=10, y=190)
  
  def quit():
    window1.destroy()
    messagebox.showinfo("bạn đã hủy đơn hàng", " xin hãy khởi động lại chương trình.")
    
  B1 = tk.Button(window1, text="hủy", command=quit)
  B1.place(x=10, y=225)


    
    
  login_window.destroy()
  window1.mainloop()


# Tạo trường nhập liệu tên đăng nhập
username_label = tk.Label(login_window, text="Tên đăng nhập:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

# Tạo trường nhập liệu mật khẩu
password_label = tk.Label(login_window, text="Mật khẩu:")
password_label.pack()
password_entry = tk.Entry(login_window,
                          show="*")  # Hiển thị dấu * thay vì ký tự thật
password_entry.pack()

# Tạo nút đăng nhập
login_button = tk.Button(login_window, text="Đăng nhập", command=authenticate)
login_button.pack()



login_window.mainloop()
