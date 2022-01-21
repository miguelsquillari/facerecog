import cv2 as cv
import os
import sys
import time

cantPicture: int = 300
picturedir: str = "c:/Temp/detector/"
capture = cv.VideoCapture(0)
pic = 0
print("path::", os.path.exists(picturedir))


if sys.platform.startswith('win'):
    picturedir = "c:/Temp/detector2/"
elif sys.platform.startswith('linux'):
    picturedir = "/home/Temp/detector"


if not os.path.exists(picturedir):
    os.mkdir(picturedir)

while pic < 10:
    ret, img = capture.read()
    print(ret)
    if ret==False:
        break

    path = picturedir + "rostro_{}".format(pic) + ".jpg"
    print("ruta: " + path)

    cv.imwrite(path, img)
    cv.imshow("Registrando ...", img)
    pic = pic + 1
    cv.waitKey(1)
    time.sleep(0.4)

capture.release()
cv.destroyAllWindows()
