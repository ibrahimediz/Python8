# a = 2
# def disfonksiyon(a):
#     a = 5
#     def icfonksiyon(a):
#         a = 10
#         return a
#     return a


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


# print(disfonksiyon(a))

sonuc = 0
def hesapMakinesi(**kwargs):
    sonucHsp = 0
    for key,value in kwargs.items():
        if key == "topla":
            for i in value:
               sonucHsp = toplam(i,sonucHsp)
            print(sonucHsp)
            sonucHsp = 0
        if key == "cikarma":
            a,b = value
            sonucHsp = cikarma(a,b)
            print(sonucHsp)


hesapMakinesi(topla=[1,2,3],cikarma=[25,5])
