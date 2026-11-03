n = int(input("Nhập n (1 đến 100): "))
while n < 1 or n > 100:
    print("Giá trị ngoài phạm vi!")
    n = int(input("Nhập n (1 đến 100): "))

print("Các số từ 1 đến n:")
count_chan = 0
for i in range(1, n + 1):
    print(i, end=" ")
    if i % 2 == 0:
        count_chan += 1
print()
print(f"Số lượng số chẵn trong đoạn từ 1 đến {n} là: {count_chan}")
