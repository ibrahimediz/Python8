import numpy as np
import cv2

img = cv2.imread(r'D:\ibrahim_ediz\Ornekler\OPENCV\res1.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()