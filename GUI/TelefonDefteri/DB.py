import sqlite3 as sql
class DBGenel():
    def __init__(self,filePath):
        self.filePath = filePath
    

    def dbAc(self):
        self.db = sql.connect(self.filePath)
        self.cur = self.db.cursor()
    

    def select(self,**kwargs):
        try:
            self.dbAc()
            sozluk = kwargs.items()
            sorgu = "SELECT {} FROM {} {} "
            sutunlar = ""
            tablo = ""
            sart = " where 1 = 1 "
            for key,value in sozluk:
                if key == "SUTUN":
                    for item in value:
                        sutunlar += item + ","
                    sutunlar = sutunlar.strip(",")
                elif key == "TABLO":
                    tablo = value
                elif key == "SART":
                    for a,b,c in value:
                        if a == "1":
                            sart += " AND "
                        elif a == "0":
                            sart += " OR "
                        sart += "{} = {}".format(b,c)
            sorgu = sorgu.format(sutunlar,tablo,sart)
            sonuc =  self.cur.execute(sorgu)
            return sonuc.fetchall()
        except Exception as hata:
            print(hata)
        finally:
            self.db.close()
            

    def insert(self,**kwargs):
        sonuc = 0
        try:
            self.dbAc()
            sorgu = " INSERT INTO {} ({}) VALUES ({})"
            tablo = ""
            sutunlar = ""
            degerler = ""
            for key,value in kwargs.items():
                if key=="TABLO":
                    tablo = value
                elif key == "DEGER":
                    for a,b in value:
                        sutunlar += a + ","
                        degerler += b + ","
                    sutunlar = sutunlar.rstrip(",")
                    degerler = degerler.rstrip(",")
            sorgu = sorgu.format(tablo,sutunlar,degerler)
            self.cur.execute(sorgu)
            self.db.commit()
            sonuc = 1
        except Exception as hata:
            print(hata)
            sonuc = -1
            self.db.rollback()
        finally:
            self.db.close()
            return sonuc
