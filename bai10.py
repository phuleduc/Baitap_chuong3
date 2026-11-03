n = int(input("Nhập số lượng sinh viên n (1 đến 60): "))
while n < 1 or n > 60:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n = int(input("Nhập số lượng sinh viên n (1 đến 60): "))

co_mat = 0
vang_mat = 0
co_phep = 0

for i in range(1, n + 1):
    tt = int(input(f"Nhập trạng thái điểm danh SV thứ {i} (1: Có mặt, 0: Vắng, 2: Có phép): "))
    while tt != 0 and tt != 1 and tt != 2:
        print("Trạng thái không hợp lệ! Vui lòng nhập lại (chỉ chọn 0, 1, 2).")
        tt = int(input(f"Nhập lại trạng thái điểm danh SV thứ {i}: "))
        
    if tt == 1:
        co_mat += 1
    elif tt == 0:
        vang_mat += 1
    elif tt == 2:
        co_phep += 1

ty_le_co_mat = (co_mat / n) * 100
ty_le_khong_co_mat = ((vang_mat + co_phep) / n) * 100

print("\n--- BÁO CÁO THỐNG KÊ ĐIỂM DANH ---")
print(f"Số sinh viên có mặt: {co_mat}")
print(f"Số sinh viên vắng mặt: {vang_mat}")
print(f"Số sinh viên có phép: {co_phep}")
print(f"Tỷ lệ sinh viên có mặt: {ty_le_co_mat:.2f}%")
print(f"Tỷ lệ sinh viên không có mặt (vắng + phép): {ty_le_khong_co_mat:.2f}%")
if (co_mat + vang_mat + co_phep) == n:
    print("Kiem tra: Tong so sinh vien thuoc ba nhom BANG n (Chinh xac).")
else:
    print("Kiem tra: Tong so sinh vien KHONG bang n (Loi dữ liệu).")