import random
kolonSayisi = int(input("Kolon Sayısı Gir"))
buyukliste = []
for i in range(0,kolonSayisi):
    liste = []
    for j in range(0,6):
        sayi = random.randint(1,50)
        while sayi in liste:
            sayi = random.randint(1,50)
        liste.append(sayi)
    liste.sort()
    buyukliste.append(liste)

for abuzer in buyukliste:
    print(abuzer)
