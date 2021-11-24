import cv2
import os
import sys
from matplotlib import pyplot as plt
"""
Examen Final - Alisson Bernal

1. Diseñe e implemente una rutina en Python que estime el porcentaje de pixeles de la imagen que
corresponden al césped. Como resultado, debe visualizarse en el terminal el porcentaje de la imagen
que corresponde al césped y una imagen binaria donde se observen en blanco los pixeles de césped.
Sugerencia: Utilice filtrado en color. Observe que la mayoría de lo pixeles pertenecen al césped.
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    all_pixels = (image.shape[0] * image.shape[1])

    # Hue histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
    #plt.plot(hist_hue, color='gray')
    #plt.xlim([0, 256])
    #plt.show()

    # Hue histogram max and location of max
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())

    # Peak mask
    lim_inf = (max_pos - 11, 0, 0)
    lim_sup = (max_pos + 11, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
    pixels = cv2.countNonZero(mask)
    #mask_not = cv2.bitwise_not(mask)

    cesped_pixels = pixels / all_pixels
    print('El porcentaje de la imagen que corresponde al cesped es: ', round(cesped_pixels * 100, 2), '%')

    cv2.namedWindow("Imagen binaria - blanco cesped", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Imagen binaria - blanco cesped", 1280, 720)
    cv2.imshow("Imagen binaria - blanco cesped", mask)
    cv2.waitKey(0)