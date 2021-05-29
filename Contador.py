import sys
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui, QtCore
import cv2
import numpy as np

qtCreatorFile = "Interfas_pot.ui"
UI_MainWindow , QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)

        self.puntos_FO_i=[]
        self.lineas =   []
        self.entradas   =   0
        self.salidas    =   0
        self.indicador  =   0
        self.stre - cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        self.fondo  =   []
        self.old_gray   =   []
        self.good_old   =   []
        self.setupUi(self)

        self.video  =   cv2.VideoCapture(0) 
        self.timer  =   QtCore.QTimer(self)
        self.timer.timeout().connect(self.counter)
        self.timer.start(1)
        self.pushButton.clicked.connect(self.parar)

    def counter(self):
        lk_params = dict( winSize = (15,15),
        maxlevel    =   2,
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

        ret, frame = self.video.read()
        ##cv2.imshow('CamaraPython', frame)
        frame = cv2.resize(frame, (640, 400))
        gray = cv2.outColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        gray = np.double(gray)

        if len(self.old_gray)==0:
            self.old_gray = gray
            self.fondo  = gray

        resta_fondo = abs(gray - self.fondo)
        resta_fondo = np.uint8(resta_fondo)
        gray = np.uint8(gray)


        resta_fondob = resta_fondo
        binarizar = cv2.threshold(resta_fondob, 60 ,255, cv2.THRESH_BINARY)[1]
        
        binarizar = cv2.dilate(binarizar, self.stre)
        binarizar = cv2.dilate(binarizar, self.stre)
        binarizar = cv2.dilate(binarizar, self.stre)
        binarizar = cv2.dilate(binarizar, self.stre)
        binarizar = cv2.dilate(binarizar, self.stre)

        binarizar = cv2.erode(binarizar, self.stre)
        binarizar = cv2.erode(binarizar, self.stre)
        binarizar = cv2.erode(binarizar, self.stre)

        cv2.inerite('frame.jpg'.binarizar)

        umbral = binarizar.copy()
        lm, contornos, hierrarchi = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



        for i in contornos:
            momentos = cv2.moments(i)
            if momentos['n00']<3000: 
                continue
            cx = int(momentos['n10']/ momentos['n00'])
            cy = int(momentos['n01']/ momentos['n00'])
            (x,y,w,h)= cv2.boundingRect(i)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
            self.puntos_FO_i.append([[cx,cy]])

            if cx < 254 and cx >246:
                self.indicador = 1
        
        if len(self.puntos_FO_i)!=0:
            self.puntos_FO_i = np.float32(self.puntos_FO_i)
            puntos_FO_o, err= cv2.calcOpticalFlowPyrLK(self.old_gray, gray, self.puntos_FO_i, None, **lk_params)

            good_new = puntos_FO_o[st==1]
            self.good_old = self.puntos_FO_i[st==1]

            for x in range(0,len(good_new)):
                self.lineas.append(np.zeros_like(frame))

            for i,(new,old) in enumerate(zip(good_new,self.good_old)):
                a,b = new.ravel()
                c,d = new.ravel()
                self.lineas[i] = cv2.line(self.lineas, (a,b), (c,d), [0,0,255],3)
                frame = cv2.circle(frame, (a,b), 4, (0,0,255),-i)

            for i in self.lineas:
                    frame=cv2.add(fame, i)
        
        self.puntos_FO_i = []

        if len(contornos) ==0:
            self.lineas=[]

        if self.indicador == 1 and len(self.good_old) !=0:
            for x in range(0,len(self.good_old)):
                if self.good_old[x][0]< 254 and self.good_old[x][0]>246:
                    diff_x = good_new[x][0] - self.good_old[x][0]
                    if diff_x > 0:
                        self.entradas = self.entradas+1
                        self.Entradas.setlext(str(self.entradas))
                        self.Entradas.setFont('Arial Black')
                    else:
                        self.salidas = self.salidas-1
                        self.Salidas.setTex(str(self.salidas))
                        self.Salidas.setFont('Arial Black')

        cv2.line(frame, (250,0), (250,640), [0,0,255], 3)

        imagen=QtGui.QImage(frame,frame.shape[1],frame.shape[0],frame.shape[1]*frame.shape[2],QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(imagen.rgbSwapped())
        self.lb_Original.setPixmap(pixmap)
        self.lb_Procesado.setPixmap(QtGui.QPixmap('frame.jpg'))

        self.old_gray
    def parar(self):
        self.webcan.release()
        cv2.destroyAllWindows()