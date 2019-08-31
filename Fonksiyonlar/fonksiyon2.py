def toplam(a=0,b=0):
    return a + b
def cikarma(a=0,b=0):
    return a - b
def carpma(a=1,b=1):
    return a * b
def bolme(a=0,b=1):
    return a + b

def calistir(fonk,a,b):
    return fonk(a,b)

def faktoriyel(a,b):
    sonuc = 1
    for i in range(1,a+1):
        sonuc *=i
    return sonuc
    print("Çalışır mıyım ?")




while True:
    print("""
    1. Toplama
    2.Çıkarma
    3. çarpma
    4. bölme
    5.faktoriyel alma
    6.çıkış"""
    )
    islem = int(input("İşlem Seçiniz"))
    a = int(input("ilk Sayı"))
    b = int(input("ikinci sayı"))
    if islem==1:
        fonk = toplam
    elif islem == 2:
        fonk = cikarma
    elif islem == 5:
        fonk = faktoriyel
    elif islem == 6:
        break
    print(calistir(fonk,a,b))


