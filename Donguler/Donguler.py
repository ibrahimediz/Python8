# import random 
# sayi1 = random.randint(1,50)
# sayi2 = random.randint(1,50)
# sayi3 = random.randint(1,50)
# sayi4 = random.randint(1,50)
# sayi5 = random.randint(1,50)
# sayi6 = random.randint(1,50)
# print(sayi1,sayi2,sayi3,sayi4,sayi5,sayi6)

# liste = []
# for i in range(1,7):
#     liste.append(random.randint(1,50))
# print(liste)




# print("1.")
# print("_"*30)

# for sayi in liste:
#     print(sayi)

# print("#"*30)

# print("2.")
# print("_"*30)

# for i in range(0,len(liste)):
#     print(liste[i])

# print("#"*30)

# print("3.")
# print("_"*30)

# print(*liste,sep="\n")

# print("#"*30)

# metin =  "BEŞİKTAŞ"

# for i in metin:
#     print("*",i,"*")


islem = """
(1) topla
(2) çıkar
(3) çarp
(4) bol
(5) çıkış
"""
anahtar = 1
while anahtar == 1:
    print(islem)
    soru = int(input("Yapmak İstediğin İşlemi Seç: "))
    if soru == 1:
        sayi1 = int(input("Toplamak İstediğiniz İlk Sayıyı Giriniz: "))
        sayi2 = int(input("Toplamak İstediğiniz İkinci Sayıyı Giriniz: "))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    elif soru == 2:
        sayi1 = int(input("Çıkarmak İstediğiniz İlk Sayıyı Giriniz: "))
        sayi2 = int(input("Çıkarmak İstediğiniz İkinci Sayıyı Giriniz: "))
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
    elif soru == 3:
        sayi1 = int(input("Çarpmak İstediğiniz İlk Sayıyı Giriniz: "))
        sayi2 = int(input("Çarpmak İstediğiniz İkinci Sayıyı Giriniz: "))
        print(sayi1, "x", sayi2, "=", sayi1 * sayi2)
    elif soru == 4:
        sayi1 = int(input("Bölmek İstediğiniz İlk Sayıyı Giriniz: "))
        sayi2 = int(input("Bölmek İstediğiniz İkinci Sayıyı Giriniz: "))
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
    elif soru == 5:
        print("Programdan Çıkılıyor")
        anahtar = 0

