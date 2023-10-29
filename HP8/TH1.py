StudentList = [
    ["Trần Mai Ngô", 10, 8.56],
    ["Lý Quốc Tuân", 6, 1.95],
    ["Nguyễn Minh Phú", 1, 9.56],
    ["Lê Nhân Tô", 6, 1.24],
    ["Hồ Đức Trịnh", 4, 2.77],
    ["Hà Vinh Khoa", 5, 0.98],
    ["Đinh Thắm Tăng", 6, 6.65],
    ["Lâm Dung Kha", 12, 3.21],
    ["Lý Ngô Sa", 1, 9.44],
    ["Đinh Tú Tăng", 4, 8.81],
    ["Phan Thủy Tuân", 5, 6.24]
]

# Hiển thị danh sách học sinh từ 1 đến 10
print("Danh sách học sinh từ 1 đến 10:")
for i in range(10):
    print(f"{i+1}. {StudentList[i][0]}")
## print(StudentList[0:10])

# Nhập vào điểm
diem = float(input("Nhập điểm: "))

# Hiển thị học sinh có điểm >= điểm nhập vào
print(f"Danh sách học sinh có điểm >= {diem}:")
for student in StudentList:
    if student[1] >= diem:
        print(student[0])

# Tính điểm TBC của học sinh và thêm vào danh sách
print("Học sinh có điểm TBC >= 8.0:")
for student in StudentList:
    diem_tb = (student[1] + student[2]) / 2
    student.append(diem_tb)
    if diem_tb >= 8.0:
        print(student[0])
