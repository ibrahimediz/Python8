i = 0
while True:
    i += 1
    print(i,"deneme")
    if i == 9:
        continue
    print("--")
    if i == 11:
        for j in range(0,8):
            print("T")
            if j == 4:
                break
        break

        
"""
bir kullanıcının girdiği 
sayıya kadar olan tek sayıları yazdıran python kodu
"""

# sayi = int(input("Sayı Giriniz"))
# for i in range(0,sayi+1):
#     if i % 2 > 0:
#         print(i)
