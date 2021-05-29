import numpy as np
import cv2

cap= cv2.VideoCapture(0) #iniciamos camara

while(True):
    ret, frame = cap.read()

    cv2.imshow('CamaraPython', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()