import cv2
import numpy as np

image = cv2.imread('artificial.jpg')
ancho = image.shape[1]
alto = image.shape[0]

#rotar
angulo = cv2.getRotationMatrix2D((ancho//2,alto//2), 180, 1)
imageR = cv2.warpAffine(image, angulo, (ancho,alto))
cv2.imshow('IMAGEN NORMAL', image)
cv2.imshow('IMAGEN ROTADA', imageR)
cv2.waitKey(0)
cv2.destroyAllWindows()