for i in range(0,10000000):
    strSayi = str(i)
    basamak = len(strSayi)
    toplam = 0
    for j in range(0,basamak):
        toplam+=int(strSayi[j])**basamak
    if i == toplam:
        print(i)
    
sayi = int(input("sayıyı giriniz"))
sonuc = 1
for i in range(1,sayi+1):
    sonuc *= i
print(sonuc)