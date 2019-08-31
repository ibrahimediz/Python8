def sinirsizToplama(*args):
    sonuc = 0
    for item in args:
        sonuc += item
    return sonuc

def sinirsizCarpim(*args):
    sonuc = 1
    for item in args:
        sonuc *= item
    return sonuc

liste = []
while True:
    sayi = int(input("(Çıkmak için 0) Toplam için sayi giriniz"))
    if sayi != 0:
        liste.append(sayi)
    else:
        break
sonuc = 0
print(sonuc)
print("Sonuç {}".format(sinirsizToplama(*liste)))
print("Sonuç {}".format(sinirsizCarpim(*liste)))
