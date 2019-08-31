from OOP3 import DeadPool,IronMan,Hulk,CaptainAmerica
import time
import random

liste = [CaptainAmerica(),DeadPool(),IronMan(),Hulk()]
karakter1 = liste[random.randint(0,len(liste)-1)]
karakter2 = liste[random.randint(0,len(liste)-1)]
print(karakter1.ad,"vs",karakter2.ad)

while karakter1.saglik > 0 and karakter2.saglik > 0:
    time.sleep(1)
    kSay1 =  random.randint(0,2)
    kSay2 =  random.randint(0,2)
    if kSay1 == 0:
        karakter1.Savunma()
    elif kSay2 == 1:
        karakter2.Vurus(karakter1.vurus)
    if kSay2 == 0:
        karakter2.Savunma()
    elif kSay2 == 1:
        karakter1.Vurus(karakter2.vurus)
else:
    print("Oyun Bitti")