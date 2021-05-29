import numpy as np 
import cv2

img = cv2.imread('B.jpg')   #libreria open cv
cv2.imshow('imagen', img)    #cargar imagen
cv2.waitKey('q')               #abrir imagen y cerrarlo de inmediato
cv2.destroyAllWindows()     #destruir sesion 