import sqlite3 as sql
try :
    db = sql.connect(r"D:\ibrahim_ediz\Ornekler\DB\chinook.db")
    cur = db.cursor()
    sanatci = input("Listelemek istediğin sanatçının adını gir")
    sorgu = """
    insert into artists (Name) Values ('{}');
            """.format(sanatci)
    cur.execute(sorgu)
    db.commit()
    sorgu = """select * from artists order by ArtistId desc  LIMIT 1"""
    liste =  cur.execute(sorgu).fetchall()
    print(*liste,sep="\n")
except Exception as hata:
    print(hata)
finally:
    db.close()
input()
