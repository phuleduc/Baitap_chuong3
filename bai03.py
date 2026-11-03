n = int(input("Nhập n (1 đến 30): "))
while n < 1 or n > 30:
    print("Giá trị không hợp lệ!")
    n = int(input("Nhập n (1 đến 30): "))
tong = 0
for i in range(1, n + 1):
    val = int(input(f"Nhập số thứ {i}: "))
    tong += val
tb_cong = tong / n
print(f"Số lượng số đã nhập: {n}")
print(f"Tổng các số đã nhập: {tong}")
print(f"Trung bình cộng: {tb_cong}")
