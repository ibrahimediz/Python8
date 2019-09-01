import numpy as np
import cv2

img = cv2.imread(r'D:\ibrahim_ediz\Ornekler\OPENCV\res1.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)
font = cv2.FONT_HERSHEY_SIMPLEX
metin = input("Mesajınız")
cv2.putText(img,metin,(10,50),font,1,(0,250,200),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()