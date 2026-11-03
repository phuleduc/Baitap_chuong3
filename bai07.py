initial_money = float(input("Nhập số tiền tiết kiệm ban đầu (> 0): "))
while initial_money <= 0:
    print("Số tiền phải lớn hơn 0! Vui lòng nhập lại.")
    initial_money = float(input("Nhập số tiền tiết kiệm ban đầu (> 0): "))
n = int(input("Nhập số tháng n (1 đến 24): "))
while n < 1 or n > 24:
    print("Số tháng phải nằm trong khoảng 1 đến 24! Vui lòng nhập lại.")
    n = int(input("Nhập số tháng n (1 đến 24): "))

so_du = initial_money
tong_tien_gui_them = 0.0
tong_tien_lai = 0.0

for thang in range(1, n + 1):
    lai_thang = so_du * 0.005 
    tong_tien_lai += lai_thang
    
    gui_them = float(input(f"Nhập số tiền gửi thêm cuối tháng {thang} (> 0): "))
    while gui_them <= 0:
        print("Số tiền gửi thêm phải lớn hơn 0! Vui lòng nhập lại.")
        gui_them = float(input(f"Nhập số tiền gửi thêm cuối tháng {thang} (> 0): "))
        
    tong_tien_gui_them += gui_them
    so_du = so_du + lai_thang + gui_them
    
    print(f"Số dư cuối tháng {thang}: {so_du:.2f}")

print("\n--- KẾT QUẢ THỐNG KÊ ---")
print(f"Số dư cuối cùng: {so_du:.2f}")
print(f"Tổng số tiền đã gửi thêm trong {n} tháng: {tong_tien_gui_them:.2f}")
print(f"Tổng số tiền lãi nhận được: {tong_tien_lai:.2f}")

