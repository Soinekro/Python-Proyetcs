import numpy as np
import time
from IPython.display import display
from sympy import init_printing, Matrix
import os

init_printing()
class cuatro_en_linea:
    def __init__(self):
        print("1. Humano vs Computadora")
        print("2. Humano vs Humano")
        seleccion   =   input("seleccione el modo de juego: ")
        seleccion   =   self.comprobar_seleccion(seleccion)
        self.modo   =   seleccion+1
        self.tablero    =   np.zeros((6,7)).astype(int)
        self.opcion     =   [0,1,2,3,4,5,6]
        self.columnas_llenas  = set()
    def comprobar_seleccion(self, seleccion, columnas_llenas=set()):
        while True:
            if not seleccion.isdigit():
                seleccion = input("Seleccion no valida, debes ingresar un Numero: ")
            elif int(seleccion) -1 < 0 or int(seleccion)-1>6 or int(seleccion)-1 in columnas_llenas:
                seleccion = input(f"Seleccion no valida, escoga una opcion Valida: ")
            else:
                break
        return int(seleccion)-1

    def Comprobar_ganar(self,booleano,cadena):
        #comprobar filas
        for fila in booleano:
            if sum(fila) >=4:
                if sum(fila[:4]) >= 4 or sum(fila[1:5]) >= 4 or sum(fila[3:]) >= 4:
                    return True, f'!{cadena} gano! 4 en una fila!'
        #comprobar columnas
        for fila in booleano.T:
            #solo si hay por los meno 4
            if sum(fila) >=4:
                if sum(fila[:4]) >= 4 or sum(fila[1:5]) >= 4 or sum(fila[3:]) >= 4:
                    return True, f'!{cadena} gano! 4 en una fila!'
        #comprobar diagonales
        for k in range(-2,4):
            if sum(np.diag(booleano,k)[:4]) >= 4 or sum(np.diag(booleano,k)[::-1][:4]) >=4:
                return True , f'!{cadena} gano! 4 en una diagonal'
            if sum(np.diag(np.rot90(booleano),k-1)[:4]) >= 4 or sum(np.diag(np.rot90(booleano),k-1)[::-1][:4]) >= 4:
                return True, f'!{cadena} ganaste ! 4 en una diagonal!'
        return False,''

    def turno(self, jugador, Computadora, seleccion = ''):
        os.system('clear')
        display(self.tablero)
        if not Computadora:
            seleccion = input(f"jugador {jugador}, seleccione una columna: ")
            seleccion = self.comprobar_seleccion(seleccion)
        if np.prod(self.tablero[:, seleccion]) != 0:
            self.opcion.remove(seleccion)
            if Computadora:
                self.opcion.remove(seleccion)
                seleccion=np.random.choice(self.opcion)
            else:
                s = input("esta columna esta llena, por favor seleccione otra: ")
                seleccion = self.comprobar_seleccion(s,columnas_llenas=self.columnas_llenas)
        if sum(self.tablero[:,seleccion]) != 0 :
            fila = np.argmax((self.tablero>0)[:,seleccion])-1
        else:
            fila = -1
        if not Computadora:
            self.tablero[fila, seleccion] = int(jugador)
        else:
            self.tablero[fila, seleccion] = 3
    
    def jugar(self):
        while True:
            #jugadpr 1 turno
            time.sleep(.3)
            self.turno('1', Computadora=False,seleccion='')
            win, cadena = self.Comprobar_ganar(self.tablero==1, 'jugador 1')
            if win:
                time.sleep(.3)
                os.system('clear')
                display(self.tablero)
                print(cadena)
                break
            if self.modo == 1:
                time.sleep(.3)
                self.turno('CPU', Computadora=True , seleccion=np.random.choice(self.opcion))
                cadena = 'Computadora'
                win, cadena= self.Comprobar_ganar(self.tablero==3,cadena)
            else:
                time.sleep(.3)
                self.turno('2', Computadora=False , seleccion='')
                cadena="Jugador 2"
                win, cadena = self.Comprobar_ganar(self.tablero==2, cadena)
            if win:
                time.sleep(.3)
                os.system('clear')
                display(self.tablero)
                print(cadena)
                break
if __name__=='__main__':
    cuatro_en_linea().jugar()