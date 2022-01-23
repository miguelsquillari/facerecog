import cv2 as cv
import os
import sys
import time
import imutils

cantPicture: int = 300
picturedir: str = "c:/Temp/detector/"
capture = cv.VideoCapture(0)
pic = 0
print("path::", os.path.exists(picturedir))


if sys.platform.startswith('win'):
    picturedir = "c:/Temp/detector2/"
elif sys.platform.startswith('linux'):
    picturedir = "/home/Temp/detector"

# si no existe la carpeta la creo.
if not os.path.exists(picturedir):
    os.mkdir(picturedir)

# Flags for video I/O : CAP_DSHOW
# Python: cv.CAP_DSHOW
# DirectShow (via videoInput)
capture = cv.VideoCapture(0, cv.CAP_DSHOW)


faceClassifier = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0


# tomo las pictures
while pic < 10:
    ret, img = capture.read()
    # print(ret)
    if ret == False:
        break

    img = imutils.resize(img, width=640)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    auxFrame = img.copy()

    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face = auxFrame[y:y + h, x:x + w]
        face = cv.resize(face, (250, 250), interpolation=cv.INTER_CUBIC)
        path = picturedir + "rostro_{}".format(pic) + ".jpg"
        cv.imwrite(path, face)
        #cv.imwrite(personPath + '/rotro_{}.jpg'.format(count), face)
        pic = pic + 1
        cv.waitKey(1)
        time.sleep(0.4)
    cv.imshow('imagen', img)


    #print("ruta: " + path)

    #cv.imwrite(path, img)
    #cv.imshow("Registrando ...", img)


capture.release()
cv.destroyAllWindows()
