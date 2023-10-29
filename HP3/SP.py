import tkinter as tk
from tkinter import messagebox

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quan ly so diem hoc sinh")

        self.students = []

        self.create_widgets()

    def create_widgets(self):
        self.listbox_students = tk.Listbox(self.root)
        self.listbox_students.pack(padx=10, pady=10)

        fields = ["Tên học sinh", "Điểm toán", "Điểm văn", "Điểm anh"]
        self.entries = {}
        for field in fields:
            label = tk.Label(self.root, text=field)
            label.pack(padx=10, pady=5)
            entry = tk.Entry(self.root)
            entry.pack(padx=10, pady=5)
            self.entries[field] = entry

        buttons = [
            ("Thêm", self.add_student),
            ("Sửa", self.edit_student),
            ("Xóa", self.delete_student),
            ("Hiển thị", self.show_details)
        ]
        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command)
            button.pack(padx=10, pady=5)

        self.load_data()

    def load_data(self):
        self.listbox_students.delete(0, tk.END)
        for student in self.students:
            self.listbox_students.insert(tk.END, student["Tên học sinh"])

    def add_student(self):
        student = {field: entry.get().strip() for field, entry in self.entries.items()}
        if all(student.values()):
            self.students.append(student)
            self.load_data()
            self.clear_entries()
        else:
            messagebox.showwarning("Thông báo", "Vui lòng điền đầy đủ thông tin.")

    def edit_student(self):
        selected_index = self.listbox_students.curselection()
        if not selected_index:
            messagebox.showwarning("Thông báo", "Vui lòng chọn một học sinh.")
            return

        student = {field: entry.get().strip() for field, entry in self.entries.items()}
        if all(student.values()):
            self.students[selected_index[0]] = student
            self.load_data()
            self.clear_entries()
        else:
            messagebox.showwarning("Thông báo", "Vui lòng điền đầy đủ thông tin.")

    def delete_student(self):
        selected_index = self.listbox_students.curselection()
        if not selected_index:
            messagebox.showwarning("Thông báo", "Vui lòng chọn một học sinh.")
            return

        confirmed = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa học sinh này?")
        if confirmed:
            del self.students[selected_index[0]]
            self.load_data()
            self.clear_entries()

    def show_details(self):
        selected_index = self.listbox_students.curselection()
        if not selected_index:
            messagebox.showwarning("Thông báo", "Vui lòng chọn một học sinh.")
            return

        student = self.students[selected_index[0]]
        details = ""
        for field, value in student.items():
            details += f"{field}: {value}\n"

        messagebox.showinfo("Thông tin chi tiết", details)

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

root = tk.Tk()
root.geometry('400x700')
app = StudentManagementApp(root)
app.run()