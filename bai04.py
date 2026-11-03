n = int(input("Nhập n (1 đến 9): "))
while n < 1 or n > 9:
    print("Giá trị ngoài phạm vi!")
    n = int(input("Nhập n (1 đến 9): "))
for i in range(1, n + 1):
    print(f"--- BẢNG CỬU CHƯƠNG {i} ---")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

