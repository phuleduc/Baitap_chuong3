n=int(input("nhap so nguyen n"))
while n<1 or n>100:
    print ("khong hop le")
    n=int(input("nhap n tu 1 den 100"))
tong_chan=0
for i in range (1,n+1):
    if i%2==0:
        tong_chan+=i
tong_le=0
for i in range (1,n+1):
    if i % 2 !=0:
        tong_le +=i
print (f"tong cac so chan tu 1 den {n}la:{tong_chan}")
print (f"tong cac so le tu 1 den {n}la:{tong_le}")