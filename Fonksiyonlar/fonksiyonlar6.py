sonuc = 0

def toplam(a=0,b=0):
    return a + b
def cikarma(a=0,b=0):
    return a - b


def hesapMakinesi(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs.items())
    sonucHsp = 0
    for key,value in kwargs.items():
        print("key",key)
        print("value",value)
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
