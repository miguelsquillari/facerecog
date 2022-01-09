import mtcnn
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import cv2 as cv

caras = ''


def detectarRostro():
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv.imshow('Detectando rostro ..', frame)
        if cv.waitKey(1)==27:
            break
    cv.imwrite("c:/Temp/detector/rostro.jpg", frame)
    cap.release()
    cv.destroyAllWindows()
    setting()


def drawinFace(img, lista):
    print(caras)
    #leemos la imagen
    imagen = pyplot.imread(img)
    #ploteamos la imagen PARA PODER DIBIJAR SOBRE LA IMAGEN
    pyplot.imshow(imagen)
    # ejes polares
    ax = pyplot.gca()

    # ploteamos los rectangulos
    for result in lista:
        print(result)
        x, y, ancho, alto = result['box']
        #creando el rectangulo
        rect = Rectangle((x,y), ancho, alto, fill=False, color='green')
        ax.add_patch(rect)

    pyplot.show()


def setting():
    img = "c:/Temp/detector/rostro.jpg";
    pixeles = pyplot.imread(img)
    #creating il detectore
    detector = MTCNN()
    caras = detector.detect_faces(pixeles) # detectamos las caras apartir de la foto ...
    drawinFace(img,caras)


def main(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    detectarRostro()


if __name__ == '__main__':
    main('Deteccion de rostros')


