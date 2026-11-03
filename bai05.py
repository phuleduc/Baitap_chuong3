a = float(input("Nhập số thực a (khác 0): "))
while a == 0:
    print("a phải khác 0! Vui lòng nhập lại.")
    a = float(input("Nhập số thực a (khác 0):"))
n = int(input("Nhập số nguyên n (0 đến 20): "))
while n < 0 or n > 20:
    print("n ngoài phạm vi (0 đến 20)! Vui lòng nhập lại.")
    n = int(input("Nhập số nguyên n (0 đến 20): "))
ket_qua = 1.0
if n == 0:
    ket_qua = 1.0
else:
    for i in range(n):
        ket_qua *= a

print(f"Kết quả của {a}^{n} là: {ket_qua}")

