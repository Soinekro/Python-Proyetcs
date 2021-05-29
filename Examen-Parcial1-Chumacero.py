import cv2
import numpy as np

image= cv2.imread("artificial.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127,255,0)
contours, hierrarchi = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
"""
print("Numero de contornos = " + str(len(contours)))
print(contours[0])
"""
cv2.drawContours(image, contours, -1, (0,255,0),0)
cv2.imshow('IMAGEN', image)
cv2.imshow('IMAGEN EN GRIS', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()