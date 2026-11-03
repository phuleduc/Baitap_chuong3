n = int(input("Nhập số lượt tối đa n (1 đến 30): "))
while n < 1 or n > 30:
    print("Giá trị không hợp lệ")
    n = int(input("Nhập số lượt tối đa n (1 đến 30): "))

dem = 0
tong = 0

for i in range(1, n + 1):
    val = int(input(f"Nhập số nguyên thứ {i} (nhập -1 để dừng): "))
    if val == -1:
        break
    dem += 1
    tong += val

print("\n--- KẾT QUẢ ---")
print(f"Số lượng giá trị thực tế đã nhập: {dem}")
print(f"Tổng các giá trị đã nhập: {tong}")

if dem > 0:
    tb_cong = tong / dem
    print(f"Trung bình cộng: {tb_cong}")
else:
    print("Không có dữ liệu nào được nhập trước tín hiệu kết thúc, không thể tính trung bình!")

