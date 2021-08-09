import cv2
import os
import numpy as np

class basicColor:
    def __init__(self):
        self.path_input = input("Por favor indique la ruta de la imagen con la que desea trabajar: ")
        self.name = input("Por favor indique el nombre de la imagen y su formato: ")

    def displayProperties(self):
        # unir la ruta con el nombre de la imagen
        path_file = os.path.join(self.path_input, self.name)
        # lectura de la imagen
        image = cv2.imread(path_file)
        # validar que la imagen sea válida
        assert image is not None, "No es una imagen: {}".format(path_file)
        # visualizar el número de píxeles y de canales de la imagen
        output_pixeles = (image.shape[0] * image.shape[1]) / 1000000
        output_canales = image.shape[2]
        print('La imagen tiene ' + str(output_pixeles) + 'MP y ' + str(output_canales) + ' canales')

    def makeBW(self):
        path_file = os.path.join(self.path_input, self.name)
        image = cv2.imread(path_file)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Imagen oiginal", image)
        cv2.imshow("Imagen Otsu", Ibw_otsu)
        cv2.waitKey(0)

    def colorize(self):
        self.h_input = input("Por favor indique h: ")
        self.h_input = int(self.h_input)
        path_file = os.path.join(self.path_input, self.name)
        image = cv2.imread(path_file)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h = image_hsv[:, :, 0]
        s = image_hsv[:, :, 1]
        v = image_hsv[:, :, 2]

        h_new = (h * 0 + self.h_input).astype(np.uint8)
        image_hsv_new = cv2.merge([h_new, s, v])
        image_bgr_new = cv2.cvtColor(image_hsv_new, cv2.COLOR_HSV2BGR)
        cv2.imshow("Imagen Colorizada con hue = " + str(h), image_bgr_new)
        cv2.waitKey(0)

