birler = {"0":"","1":"bir","2":"iki","3":"üç","4":"dört"}
onlar = {"0":"","1":"on","2":"yirmi","3":"otuz","4":"kırk"}
uclu = {"0":"","1":"bin","2":"milyon","3":"milyar","4":"trilyon"}

metin = input("Okumasını isterdiğiniz sayıyı giriniz")
metin = metin.replace(",","").replace(".","")
liste = []
while len(metin)%3>0:
    metin = "0" + metin
for i in range(0,int(len(metin)/3)):
    liste.append(metin[0+(i*3):(i*3)+3])
    
print(liste)
liste.reverse()
print(liste)
genelYazi = ""
i = 0
for item in liste:
    yazi = ""
    if not item[0] == "0":
        if item[0] == "1":
            yazi += " yüz "
        else:
            yazi += birler[item[0]] + " yüz "
    yazi += onlar[item[1]] + " "
    yazi += birler[item[2]] + " "
    yazi += uclu[str(i)] + " "
    i+=1
    genelYazi = yazi + genelYazi
print(metin,genelYazi)
        


