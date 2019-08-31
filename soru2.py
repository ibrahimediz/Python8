"""
 1. verilen liste değişkeni içerisine üç farklı veri tipinde eleman ekleyiniz
 2. liste içinde 14 sayısının kaç defa geçtiğini ekrana yazdırınız
 3. listenin tersine çevrilmiş halini ekrana yazdırınız
 4. listeden eklediğiniz elemanları silerek listeyi tekrar yazdırınız
"""
# verilen liste 
liste = [12,23,54,65,1,[12,14],(123,"54"),{"14":14}]
# 1.
liste1 = ["1",1,1.0]
liste.extend(liste1)
print(liste)
# 2. 
print(liste.count(14))
# 3. 
liste.reverse()
print(liste)
# 4.
liste = liste[3:]
print(liste)