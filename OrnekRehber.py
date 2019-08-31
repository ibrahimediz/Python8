from datetime import datetime
import os
def dosyaAcma(adres =os.getcwd()+os.sep+"defter.csv" ):
    import os
    if os.path.exists(adres):
        kip = "r+"
    else:
        kip = "w+"
    return open(adres,kip)

def HataLog(Mesaj="",HataMesaji="",HataYer=""):
    try:
        adim = "Log1"
        dosya = dosyaAcma(os.getcwd()+os.sep+"hata.csv")
        adim = "Log2"
        hata = "{};{};{};{}\n".format(Mesaj,HataMesaji,HataYer,str(datetime.now()))
        adim = "Log3"
        dosya.read()
        adim = "Log4"
        dosya.write(hata)
    except Exception as hata:
        print("Log Hatası",hata,adim)
    finally:
        dosya.close()

def dosyaOkuma():
    try:
        adim = "dO1A"
        dosya = dosyaAcma()
        adim = "dO1A1"
        print("-"*20)
        tumListe = dosya.readlines()
        adim = "dO1A3"
        for item in tumListe:
            adim = "dO1A3_for"
            liste =  item.split(";")
            print("{}-{}-{}-{}".format(tumListe.index(item)+1,liste[0],liste[1],liste[2]))
        print("-"*20)
        adim = "dO1A4"
    except Exception as hata:
        print(adim)
        HataLog("Dosya Okuma",hata,adim)

def dosyaSilDuzelt(islem = 0):
    dosyaOkuma()
    kayitNum =  input("Kayıt Seçiniz")
    dosya = dosyaAcma()
    liste = dosya.readlines()
    if islem == 0:
        adi = input("Adını Giriniz")
        soyadi = input("Soyadı Giriniz")
        telefon = input("Telefon Giriniz")
        kayit = "{};{};{}\n".format(adi,soyadi,telefon)
        liste[int(kayitNum)-1] = kayit
    elif islem == 1:
        liste.pop(int(kayitNum)-1)
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()
    print("Kayıt İşlemi Gerçekleşti")

def dosyaArama():
    arama = input("Aramak istediğiniz metni giriniz")
    dosya = dosyaAcma()
    liste = dosya.readlines()
    sonuc = []
    for item in liste:
        eleman =  item.split(";")
        if arama in eleman[0] or arama in eleman[1] or arama in eleman[2]:
            sonuc.append(item)
    for item in sonuc:
        liste =  item.split(";")
        print("{}-{}-{}-{}".format(sonuc.index(item)+1,liste[0],liste[1],liste[2]))

def dosyaYazma():
    dosya = dosyaAcma()
    adi = input("Adını Giriniz")
    soyadi = input("Soyadı Giriniz")
    telefon = input("Telefon Giriniz")
    kayit = "{};{};{}".format(adi,soyadi,telefon)
    liste = dosya.readlines()
    liste.append(kayit)
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()
    print("Kayıt İşlemi Gerçekleşti")

metin =  """
1 - Arama
2 - Ekleme
3 - Silme
4 - Düzeltme
5 - Listeleme
6 - Çıkış
""" 
while True:
    print(metin)
    try:
        islem = int(input("İşlem Seçiniz"))
        if islem == 1:
            dosyaArama()
        elif islem == 2:
            dosyaYazma()
        elif islem == 3:
            dosyaSilDuzelt(1)
        elif islem == 4:
            dosyaSilDuzelt()
        elif islem == 5:
            adim = "AnaI5A"
            dosyaOkuma()
            adim = "AnaI5B"
        elif islem == 6:
            break
    except Exception as hata:
        HataLog("Ana Menü",hata,adim)
