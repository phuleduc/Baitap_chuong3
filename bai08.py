n = int(input("Nhập n (1 đến 30): "))
while n < 1 or n > 30:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n = int(input("Nhập n (1 đến 30): "))

dem_hop_le = 0
dem_khong_hop_le = 0
tong_hop_le = 0.0

for i in range(1, n + 1):
    val = float(input(f"Nhập giá trị thứ {i}: "))
    if val < 0 or val > 100:
        print("Thông báo: Giá trị không hợp lệ!")
        dem_khong_hop_le += 1
        continue
    
    dem_hop_le += 1
    tong_hop_le += val

print("\n--- KẾT QUẢ THỐNG KÊ ---")
print(f"Số lượng giá trị hợp lệ: {dem_hop_le}")
print(f"Số lượng giá trị không hợp lệ: {dem_khong_hop_le}")
print(f"Tổng các giá trị hợp lệ: {tong_hop_le}")

if dem_hop_le > 0:
    tb_cong = tong_hop_le / dem_hop_le
    print(f"Trung bình cộng các giá trị hợp lệ: {tb_cong}")
else:
    print("Không thể tính trung bình cộng do không có giá trị hợp lệ nào!")