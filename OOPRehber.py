from datetime import datetime
import os
class OOPDosya():
    dosyaFormat = ".csv"
    def __init__(self,**kwargs):
        self.dosya = None
        for key,value in kwargs.items():
            if key == "dosya":
                self.adres =os.getcwd()+os.sep+value+self.dosyaFormat
            if key == "veriler":
                self.degiskenler = value


    def dosyaAcma(self):
        if os.path.exists(self.adres):
            kip = "r+"
        else:
            kip = "w+"
        self.dosya = open(self.adres,kip)


    def dosyaAcma2(self,adres=""):
        if os.path.exists(adres):
            kip = "r+"
        else:
            kip = "w+"
        self.dosya = open(adres,kip)

    def HataLog(self,Mesaj="",HataMesaji="",HataYer=""):
        try:
            adim = "Log1"
            self.dosyaAcma2(os.getcwd()+os.sep+"hata.csv")
            adim = "Log2"
            hata = "{};{};{};{}\n".format(Mesaj,HataMesaji,HataYer,str(datetime.now()))
            adim = "Log3"
            self.dosya.read()
            adim = "Log4"
            self.dosya.write(hata)
        except Exception as hata:
            print("Log Hatası",hata,adim)
        finally:
            self.dosya.close()

    def dosyaOkuma(self):
        try:
            adim = "dO1A"
            self.dosyaAcma()
            adim = "dO1A1"
            print("-"*20)
            tumListe = self.dosya.readlines()
            adim = "dO1A3"
            for item in tumListe:
                adim = "dO1A3_for"
                liste =  item.split(";")
                print("{}-{}-{}-{}".format(tumListe.index(item)+1,liste[0],liste[1],liste[2]))
            print("-"*20)
            adim = "dO1A4"
        except Exception as hata:
            print(adim)
            self.HataLog("Dosya Okuma",hata,adim)

    def dosyaSilDuzelt(self,islem = 0):
        self.dosyaOkuma()
        kayitNum =  input("Kayıt Seçiniz")
        self.dosyaAcma()
        liste = self.dosya.readlines()
        if islem == 0:
            kayit =  self.veriTopla()
            liste[int(kayitNum)-1] = kayit
        elif islem == 1:
            liste.pop(int(kayitNum)-1)
        self.dosyaKayit(liste)
        print("Kayıt İşlemi Gerçekleşti")
        
    def dosyaYazma(self):
        self.dosyaAcma()
        kayit = self.veriTopla()
        liste = self.dosya.readlines()
        liste.append(kayit)
        self.dosyaKayit(liste)
        print("Kayıt İşlemi Gerçekleşti")

    def veriTopla(self):
        kayit = ""
        for item in self.degiskenler:
            kayit += input(item+" Giriniz")
            if self.dosyaFormat == ".csv":
                kayit += ";"
            else:
                kayit += "\t"
        return kayit

    def dosyaKayit(self,liste):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(liste)
        self.dosya.close()

    def dosyaArama(self):
        arama = input("Aramak istediğiniz metni giriniz")
        self.dosyaAcma()
        liste =  self.dosya.readlines()
        sonuc = []
        for item in liste:
            eleman =  item.split(";")
            if arama in eleman[0] or arama in eleman[1] or arama in eleman[2]:
                sonuc.append(item)
        for item in sonuc:
            liste =  item.split(";")
            print("{}-{}-{}-{}".format(sonuc.index(item)+1,liste[0],liste[1],liste[2]))

    def dosyaYazma(self):
        self.dosyaAcma()
        kayit = self.veriTopla()
        liste = self.dosya.readlines()
        liste.append(kayit)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(liste)
        self.dosya.close()
        print("Kayıt İşlemi Gerçekleşti")

    def Menu(self):
        adim = ""
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
                    self.dosyaArama()
                elif islem == 2:
                    self.dosyaYazma()
                elif islem == 3:
                    self.dosyaSilDuzelt(1)
                elif islem == 4:
                    self.dosyaSilDuzelt()
                elif islem == 5:
                    adim = "AnaI5A"
                    self.dosyaOkuma()
                    adim = "AnaI5B"
                elif islem == 6:
                    break
            except Exception as hata:
                self.HataLog("Ana Menü",hata,adim)



if __name__=="__main__":
    defter = OOPDosya(dosya ="banka", veriler=["Adı","Soyadı","Banka Hesap No","Bakiye"])
    defter.Menu()