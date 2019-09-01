import numpy as np
import cv2

img = cv2.imread(r'D:\ibrahim_ediz\Ornekler\OPENCV\res1.jpg',cv2.IMREAD_COLOR)
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread(r'D:\ibrahim_ediz\Ornekler\OPENCV\3D-Matplotlib.png')
img2 = cv2.imread(r'D:\ibrahim_ediz\Ornekler\OPENCV\mainsvmimage.png')

add = img1+img2

cv2.imshow('add',add)
 
add2 = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('add2',add2)

cv2.waitKey(0)
cv2.destroyAllWindows()