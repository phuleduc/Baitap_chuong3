# Nhập số mặt hàng n trong khoảng từ 1 đến 20
n = int(input("Nhập số mặt hàng n (1 đến 20): "))
while n < 1 or n > 20:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n = int(input("Nhập số mặt hàng n (1 đến 20): "))

tong_so_luong = 0
tong_tien = 0.0

for i in range(1, n + 1):
    print(f"\n--- Nhập thông tin mặt hàng thứ {i} ---")
    
    don_gia = float(input("Nhập đơn giá (> 0): "))
    while don_gia <= 0:
        print("Đơn giá phải lớn hơn 0! Vui lòng nhập lại.")
        don_gia = float(input("Nhập đơn giá (> 0): "))
        
    so_luong = int(input("Nhập số lượng (> 0, số nguyên): "))
    while so_luong <= 0:
        print("Số lượng phải lớn hơn 0! Vui lòng nhập lại.")
        so_luong = int(input("Nhập số lượng (> 0, số nguyên): "))
        
    thanh_tien = don_gia * so_luong
    print(f"Thành tiền mặt hàng {i}: {thanh_tien}")
    
    tong_so_luong += so_luong
    tong_tien += thanh_tien

print("\n================ HÓA ĐƠN ================")
print(f"Tổng số lượng sản phẩm đã mua: {tong_so_luong}")
print(f"Tổng số tiền phải thanh toán: {tong_tien}")
n = int(input("Nhập số mặt hàng n (1 đến 20): "))
while n < 1 or n > 20:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n = int(input("Nhập số mặt hàng n (1 đến 20): "))

tong_so_luong = 0
tong_tien = 0.0

for i in range(1, n + 1):
    print(f"\n--- Nhập thông tin mặt hàng thứ {i} ---")
    
    don_gia = float(input("Nhập đơn giá (> 0): "))
    while don_gia <= 0:
        print("Đơn giá phải lớn hơn 0! Vui lòng nhập lại.")
        don_gia = float(input("Nhập đơn giá (> 0): "))
        
    so_luong = int(input("Nhập số lượng (> 0, số nguyên): "))
    while so_luong <= 0:
        print("Số lượng phải lớn hơn 0! Vui lòng nhập lại.")
        so_luong = int(input("Nhập số lượng (> 0, số nguyên): "))
        
    thanh_tien = don_gia * so_luong
    print(f"Thành tiền mặt hàng {i}: {thanh_tien}")
    
    tong_so_luong += so_luong
    tong_tien += thanh_tien

print("\n================ HÓA ĐƠN ================")
print(f"Tổng số lượng sản phẩm đã mua: {tong_so_luong}")
print(f"Tổng số tiền phải thanh toán: {tong_tien}")