from OOP2 import MarvelHero

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool",200,5,50,"Onarım")
        self.silah = "Kılıç"
    
    def yenilenme(self):
        self.saglik = 200

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan",300,5,75,"Kıyafet")
        self.silah = "Ateş"

    def yeniKiyafet(self):
        self.saglik = 300

    def Vurus(self,darbe):
        self.saglik -= darbe*2
        print(self.ad," {} oranında darbe aldı saglik {}".format(darbe,self.saglik))



class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",500,50,100,"Dönüşüm")
        self.silah = "Ateş"

    def donusum(self):
        self.saglik = 500

    def Vurus(self,darbe):
        self.saglik -= darbe/2
        print(self.ad," {} oranında darbe aldı saglik {}".format(darbe,self.saglik))



class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America",500,50,100,"Genotip")
        self.silah = "Ateş"




