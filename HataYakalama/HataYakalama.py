from datetime import datetime
def dosyaAcma(adres =r"C:\Hata.csv" ):
    import os
    if os.path.exists(adres):
        kip = "r+"
    else:
        kip = "w+"
    return open(adres,kip)

def HataLog(Mesaj="",HataMesaji="",HataYer=""):
    try:
        dosya = dosyaAcma()
        hata = "{};{};{};{}\n".format(Mesaj,HataMesaji,HataYer,str(datetime.now()))
        dosya.read()
        dosya.write(hata)
    except Exception:
        print("Log Hatası")
    finally:
        dosya.close()
try:
    sayi1 = input("Bölüm  için bir sayı gir")
    sayi2 = input("Bölüm için bir sayı daha gir")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError as hata:
    HataLog("Değer Hatası",hata,"1A")
except ZeroDivisionError as hata2:
    HataLog("Sıfıra Bölünme Hatası",hata2,"1B")
finally:
    print("İyi Günler")


print("Merhaba Ben Hala çalışmaya devam ediyorum")
input()
# try:
#     sayi1 = input("Bölüm  için bir sayı gir")
#     sayi2 = input("Bölüm için bir sayı daha gir")
#     sayi1 = int(sayi1)
#     sayi2 = int(sayi2)
#     print(sayi1,"/",sayi2,"=",sayi1/sayi2)
# except  (ValueError,ZeroDivisionError):
#     print("Değer Hatası")
# except Exception:
#     print("Sen gonuşma Soner")

# try:
#     sayi1 = input("Bölüm  için bir sayı gir")
#     sayi2 = input("Bölüm için bir sayı daha gir")
#     sayi1 = int(sayi1)
#     sayi2 = int(sayi2)
# except ValueError:
#     print("Değer Hatası")
# else:
#     try:
#         print(sayi1,"/",sayi2,"=",sayi1/sayi2)
#     except ZeroDivisionError:
#         print("Değer Hatası")


