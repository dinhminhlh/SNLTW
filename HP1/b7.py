n = int(input("Nhap so can kiem tra: "))

if n < 2:
  print("Khong phai so nguyen to")
else:
  check = True
  for i in range(2, n):
    if n % i == 0:
      check = False
      break

if check:
  print("so nguyen to")
else:
  print("khong phai so nguyen to")
