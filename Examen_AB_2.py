import cv2
import os
import sys
"""
Examen Final - Alisson Bernal

2. Diseñe e implemente una rutina en Python que encuentre cada jugador y arbitro que se
encuentre sobre el césped. Como resultado, imprima el número de jugador/arbitro encontrados en el
terminal y visualice sobre la imagen un rectángulo de color rojo sobre cada jugador/arbitro.
"""


if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    # Hue histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])

    # Hue histogram max and location of max
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())

    # Peak mask
    lim_inf = (max_pos - 11, 0, 0)
    lim_sup = (max_pos + 11, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
    mask_not = cv2.bitwise_not(mask)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, Ibw_soccer = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    soccer = Ibw_soccer.copy()


    # contours
    contours, hierarchy = cv2.findContours(soccer, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_draw = image.copy()
    conteo = 0

    for idx, cont in enumerate(contours):
        area = cv2.contourArea(cont)

        if len(contours[idx]) > 10 and area > 350 and area < 5000:
            conteo = conteo + 1

            hull = cv2.convexHull(contours[idx])
            M = cv2.moments(contours[idx])
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            area = M['m00']
            x, y, width, height = cv2.boundingRect(contours[idx])
            cv2.rectangle(image_draw, (x, y), (x + width, y + height), (0, 0, 255), 2)

    print('Numero de jugadores/arbitro: ', conteo)
    cv2.imshow("Image", image_draw)
    cv2.waitKey(0)
