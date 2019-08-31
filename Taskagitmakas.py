# veri = 

# tercih = 0
# ComP = 0
# UserP = 0
# while UserP or ComP < 3:
#     for i in range(0,3):
#         print(i,"-",veri[i][0])
#     tercih = int(input("tercihini yap"))
#     for i in range(0,3):
#         time.sleep(1)
#         print(i+1)
#     compTercih = random.randint(0,2)
#     print(veri[compTercih][0]) 
#     if veri[compTercih][1] == tercih:
#         UserP += 1
#         print("Bilgisayar Kaybetti","UserP:",UserP,"ComP:",ComP)
#     elif veri[tercih][1] == compTercih:
#         ComP += 1
#         print("Kullanıcı Kaybetti","UserP:",UserP,"ComP:",ComP)
#     else:
#         print("berabere","UserP:",UserP,"ComP:",ComP)

import time
import random
class Tkm():
    
    def __init__(self,oyuncu = 1 ):
        self.Oyuncu = oyuncu
        self.OyuncuP = 0
    def PuanAl(self):
        self.OyuncuP += 1

    def __str__(self):
        return self.Oyuncu

class Oyun():
    veri = {0:["Taş",1],1:["Kağıt",2],2:["Makas",0]}
    def __init__(self,oyuncu1,oyuncu2):
        self.p1 = Tkm(oyuncu1)
        self.p2 = Tkm(oyuncu2)
        self.Oyna()

    def Oyna(self):

        while self.p1.OyuncuP or self.p2.OyuncuP < 3:
            for i in range(0,3):
                time.sleep(1)
                print(i+1)
            self.Kontrol(self.TercihYap(self.p1),self.TercihYap(self.p2))




    def Kontrol(self,PBir,PIki):
        if self.veri[PBir][1] == PIki:
            self.p2.PuanAl()
            print("p2 Kazandı")
        elif self.veri[PIki][1] == PBir:
            self.p1.PuanAl()
            print("p1 Kazandı")
        else:
            print("berabere")
    
    def TercihYap(self,Player):
        tercih = 0
        if Player.Oyuncu == 0:
            for i in range(0,3):
                print(i,"-",self.veri[i][0])
            tercih = int(input("tercihini yap"))
        elif Player.Oyuncu == 1:
            tercih = random.randint(0,2)
        self.tercihYazdir(tercih)
        self.PuanYazdir()
        return tercih
    def PuanYazdir(self):
        print("Oyuncu1:",self.p1.OyuncuP,"Oyuncu2:",self.p2.OyuncuP)
    def tercihYazdir(self,tercih):
        print(self.veri[tercih][0])