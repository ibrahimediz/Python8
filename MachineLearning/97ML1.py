# original code from: https://techtutorialsx.com/2017/05/02/python-opencv-face-detection-and-counting/
# face_count.py
# faces also checked for the existence of eyes, lips and nose
# Instead of ascii fonts, utf-8 fonts are used

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import sys
print(sys.path)


faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')
noseCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_nose.xml')

no_check = False

def print_text(image):  # only english characters
    cv2.putText(image, "Belirlenen yüz sayısı: " + str(faces.shape[0]), (0, image.shape[0] - 10),
                cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

def print_utf8_text(image, text, color):  # utf-8 characters
    fontName = 'arial.ttf'  # 'FreeSansBold.ttf' # 'FreeMono.ttf' 'FreeSerifBold.ttf'
    font = ImageFont.truetype(fontName, 18)  # select font
    img_pil = Image.fromarray(image)  # convert image to pillow mode
    draw = ImageDraw.Draw(img_pil)  # prepare image
    draw.text((0, image.shape[0] - 30), text, font=font,
              fill=(color[0], color[1], color[2], 0))  # b,g,r,a
    image = np.array(img_pil)  # convert image to cv2 mode (numpy.array())
    return image

# Check whether face contains any of eyes, lips and nose
def it_contains_eyes(frame, gray, x, y, w, h):
    if no_check: return True
    roi_gray = gray[y:y + h, x:x + w]

    eyes = eyeCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(20, 20)
    )
    count = 0
    for (ex, ey, ew, eh) in eyes:
        count += 1
    if count > 1:
        return True

    smiles = smileCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(3, 3)
    )
    if len(smiles) > 0: return True

    noses = noseCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(3, 3)
    )
    if len(noses) > 0: return True

    return False

imageNames = ['1.jpg','2.png']
for imageName in imageNames:
    image = cv2.imread(imageName)

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayImage)

    print(type(faces))

    if len(faces) == 0:
        print("Yüz bulunamadı")
    else:
        print(faces)
        print(faces.shape)
        print("Belirlenen yüz sayısı: " + str(faces.shape[0]))

        say = 0
        for (x, y, w, h) in faces:
            if it_contains_eyes(image, grayImage, x, y, w, h):
                say += 1
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

        cv2.rectangle(image, ((0, image.shape[0] - 25)), (270, image.shape[0]), (255, 255, 255), -1)
        # print_text()
        text = "Belirlenen yüz sayısı: " + str(say)  # , (0, image.shape[0] - 10)
        color = (0, 0, 0)
        image = print_utf8_text(image, text, color)

        cv2.imshow('Imaj', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()