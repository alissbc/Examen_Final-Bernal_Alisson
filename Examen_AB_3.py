import cv2
import os
import sys
import numpy as np
import math
"""
Examen Final - Alisson Bernal

3. Diseñe e implemente una rutina en Python que permita especificar una recta y posteriormente,
visualizar una recta paralela a esta a partir de otro punto. El usuario debe realizar tres clics, dos para
definir la recta de referencia y otro para indicar donde quiere visualizar la recta paralela. Como
resultado, debe visualizarse en azul la recta de referencia y en amarillo la recta paralela.
a. El usuario utilizando el ratón (mouse) selecciona dos puntos (p1 y p2) sobre la imagen para
definir la recta de referencia (determine la recta l1 que une los dos puntos, use coordenadas
homogéneas)
b. El usuario utilizando el ratón (mouse) selecciona un punto (p3) sobre la imagen para definir
donde visualizar la recta paralela l2 (determine la recta l2, sabiendo que l1 es paralelo a l2 y que
p3 pertenece a la recta l2).
"""

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

points = []

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_draw = np.copy(image)

    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    # se generan vectores vacios para almacenar los puntos de referencia de manera temporal
    points1 = []
    points2 = []

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click)

    point_counter1 = 0
    point_counter2 = 0
    while True:
        cv2.imshow("Image", image_draw)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            points1 = points.copy()
            points = []
            break
        if len(points) > point_counter1:
            point_counter = len(points)
            cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [255, 0, 0], -1)
    while True:
        cv2.imshow("Image", image_draw)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("x"):
            points2 = points.copy()
            points = []
            break
        if len(points) > point_counter2:
            point_counter = len(points)
            cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [0, 255, 255], -1)

    N1 = len(points1)
    print(N1)
    N2 = len(points2)
    print(N2)

    #assert N1 >= 3, 'Deben ser dos puntos azules (recat referencia)'
    #assert N2 > 1, 'Debe ser uno punto amarillo (paralela)'
    #cv2.waitKey(key)

    print(points1)
    print(points2)

    new_image = cv2.line(image, points1[0], points1[1], (255, 0, 0), 2)
    cv2.imshow('Image', new_image)
    cv2.waitKey(0)

    A = points1[0]
    B = points1[1]
    print(A[0])

    vX = B[0] - A[0]
    vY = B[1] - A[1]
    mag = math.sqrt(vX * vX + vY * vY)
    vX = vX / mag
    vY = vY / mag
    temp = vX
    vX = 0 - vY
    vY = temp

    length = 20

    cX = B[0] + vX * length
    cY = B[1] + vY * length
    dX = B[0] - vX * length
    dY = B[1] - vY * length

    C = [(cX, cY)]
    D = [(dX, dY)]
    print(C)
    print(D)

    #new_image_parallel = cv2.line(new_image, C, D, (255, 0, 0), 2)
    #cv2.imshow('Image', new_image_parallel)
    #cv2.waitKey(0)
