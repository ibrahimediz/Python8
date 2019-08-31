Not = 34
"""
0-25 EE
26-44 FE
45-50 FF
51-59 FD
60-65 DD
66-69 DC
70-75 CC
76-80 CB
81-89 BB
90-95 BA
96-100 AA
"""
if Not>0 and Not<=25:
    print("EE")
elif Not>25 and Not<=44:
    print("EF")
else:
    print("Hesaplanmadı")

a = 2
b= 3
c = 1
if (a>0 and not b < 1 ) and  (a == 4 or c > 0):
    print("İf Çalışır")
else:
    print("Else Çalışır")

liste = [1,2,3,6,8,9,4,3]
sayi = int(input("aramak istediğim sayıyı gir"))
if  sayi in liste:
    print("Sayı Listede var Sayının indisi:",liste.index(sayi))
else:
    print("Sayı Yok")
print(liste)

sifre = input("Şifre Giriniz")
if not sifre:
    print("Şifre Girmediniz")

metin = input("İfade giriniz")
harf  = "u"
if harf in metin:
    print("u var")


a = int("1")
b = 1
if a is b:
    print(a)
else:
    print("--")