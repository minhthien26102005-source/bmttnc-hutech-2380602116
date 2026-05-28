def kiemtra_so_nguyen_duong(n):
    if n < 1:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
number = int(input("Nhập vào số cần kiểm tra: "))
if kiemtra_so_nguyen_duong(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")
    

    