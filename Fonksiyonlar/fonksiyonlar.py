# def kendisiTopla(x):
#     print(x+x)

# kendisiTopla(2)
# kendisiTopla(3)
# def faktoriyel(x):
#     for i in range(1,x):
#         x *= i
#     print(x)

# def faktoriyel2(y):
#     sonuc = 1
#     for i in range(1,y+1):
#         sonuc *= i
#     print(y)


# faktoriyel(5)
# faktoriyel2(5)


def toplama():
    a = int(input("ilk sayı"))
    b = int(input("ikinci sayı"))
    print(a+b)
def bolme():
    a = int(input("ilk sayı"))
    b = int(input("ikinci sayı"))
    print(a/b)
def carpim():
    a = int(input("ilk sayı"))
    b = int(input("ikinci sayı"))
    print(a*b)
def cikarma():
    a = int(input("ilk sayı"))
    b = int(input("ikinci sayı"))
    print(a-b)

def MerhabaYazProc(isim="",soyisim= ""):
    print("Merhaba {} {}".format(isim,soyisim))

MerhabaYazProc(soyisim="Ediz",isim ="İbrahim")


def MerhabaYazFonk(isim=""):
    return "Merhaba {}".format(isim)

print(type(MerhabaYazFonk("Ediz")))
print(type(MerhabaYazProc(soyisim="Ediz",isim ="İbrahim")))