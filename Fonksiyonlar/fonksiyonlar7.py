# def topla(a,b):
#     c = a + b
#     return a,b,c

# a = 5
# b= 6
# c = a+b
# print(type(topla(5,2)))

# a,b,c = topla(5,2)
# print("{} + {} = {}".format(a,b,c))


def yazdir(metin):
    while len(metin) > 1:
        print(metin)
        yazdir(metin[0:len(metin)-1])

yazdir("BEŞİKTAŞ")