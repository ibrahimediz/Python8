# class Sınıfİsmi(Miras):
#     SınıfNiteligi = 0
#     def __init__(self):
#         self.ornekNitelik = 0

#     def OrnekMetod(self):
#         pass
    
#     @classmethod
#     def SınıfMetodu(cls):
#         cls.SınıfNiteligi
    
#     @staticmethod
#     def Pi():
#         return 22/7

#     @property
#     def say()

class Personel():
    __PersonelListe = []
    def __init__(self,personBirim,personTip,personAd):
        self.personBirim=personBirim
        self.personTip = personTip
        self.personAd = personAd
        self.personListeGuncelle()
    
    def personListeGuncelle(self):
        self.__PersonelListe.append(self.personAd)
    
    @classmethod
    def Listele(cls):
        print(cls.__PersonelListe)
    
    @staticmethod
    def pi():
        return 22/7

    @property
    def selam(self):
        return "Merhaba "+self.personAd

ali = Personel("Teknik","Yakışıklı","Ali")
devrim = Personel("VeriTabanı","Sporcu","Devrim")

Personel.Listele()
print(Personel.pi())

ali.selam
