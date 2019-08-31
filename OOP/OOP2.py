    
#Deadpool
#Hulk
#IronMan
#CaptainAmerica

# saglik = 100
# savunma = 5
# vurus = 10
# yetenek = "Onarım"
# kiyafet = True

# def Vurus():
#     global saglik 
#     saglik -= vurus
#     return saglik

# def Savunma():
#     global saglik
#     saglik += savunma
#     return saglik



# class MarvelHero():
#     saglik = 100
#     savunma = 5
#     vurus = 10
#     yetenek = "Onarım"
#     kiyafet = True
#     ad  = ""

#     def Savunma():
#         global saglik
#         saglik += savunma
#         return saglik

#     def Vurus():
#         global saglik 
#         saglik -= vurus
#         return saglik

# deadPool = MarvelHero()
# deadPool.ad = "Deadpool"
# deadPool.saglik = 200
# Hulk = MarvelHero()
# Hulk.ad = "Hulk"
# print(Hulk.ad)
# print(deadPool.ad)
class MarvelHero():
    oyunKarakteri = "Marvel"
    def __init__(self,ad,saglik,savunma,vurus,yetenek):
        #instance attributes
        self.saglik = saglik
        self.savunma = savunma
        self.vurus = vurus
        self.ad = ad
        self.yetenek = yetenek
        self.kiyafet = True


    #instance Method
    def Savunma(self):
        self.saglik += self.savunma
        print(self.ad," Kendini {} oranında savundu".format(self.savunma))

    def Vurus(self,darbe):
        self.saglik -= darbe
        print(self.ad,"{} oranında darbe aldı saglik {}".format(darbe,self.saglik))







# print("Deadpool",deadpool.saglik)
# MarvelHero.oyunKarakteri = "Stan Lee"
# print(Hulk.saglik)
# deadpool.Vurus(Hulk.vurus)
# print(Hulk.saglik)

# MarvelHero.ad
