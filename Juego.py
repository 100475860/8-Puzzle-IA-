import copy
import random

from Ficha import *
from copy import deepcopy


class Juego:
    def __init__(self):
        self.fichas = [Ficha(f"{i}") for i in range(9)]
        self.movimientos = 0
        self.che
        self.__iniciar_juego()

    def __iniciar_juego(self):
        # poner las fichas en las posiciones.
        cordenadas_iniciales = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        for i in range(len(cordenadas_iniciales)):
            self.fichas[i].x, self.fichas[i].y = cordenadas_iniciales[i]

        self.imprimir_tablero()

    def imprimir_tablero(self):
        print(f"\nMovimiento {self.movimientos}:")
        print("\t-------------")
        print(f"\t| {self.fichas[0]} | {self.fichas[1]} | {self.fichas[2]} |")
        print("\t-------------")
        print(f"\t| {self.fichas[3]} | {self.fichas[4]} | {self.fichas[5]} |")
        print("\t-------------")
        print(f"\t| {self.fichas[6]} | {self.fichas[7]} | {self.fichas[8]} |")
        print("\t-------------")

    def inferencia(self):

        while self.__comprobar_no_final(self.fichas):
            blanco, pos_blanco = self.find_ficha("0")
            movimientos = self.__calcular(blanco, self.fichas)

            # Quitar movimientos nulos y de fuera del tablero.
            elementos_que_no_sirven = []
            for i in range(len(movimientos)):
                if not movimientos[i] or not movimientos[i].chequear_rango():
                    elementos_que_no_sirven.append(movimientos[i])
            for i in elementos_que_no_sirven:
                movimientos.remove(i)

            print("Movimientos disponibles: \n")
            for i in movimientos:
                print(f"\t - {i}")
            print("\n")

            # Elegir móvimiento aleatoriamente
            choice = random.randint(0,len(movimientos)-1)
            choice = movimientos[choice]

            # Efectuar movimiento
            indice1, indice2 = pos_blanco, self.find_ficha(choice.val)[1]
            #self.fichas[indice1] , self.fichas[indice2] = self.fichas[indice2] , self.fichas[indice1]
            self.actualizar_posiciones(self.fichas[indice1],self.fichas[indice2])

            self.movimientos += 1
            self.imprimir_tablero()

        print("Ya ha acabado!!!")


    def find_ficha(self,valor:str):
        contador = 0
        for i in self.fichas:
            if i.val == valor:
                return [i,contador]
            contador += 1

    def actualizar_posiciones(self,ficha1:object,ficha2:object):
        ficha1.val, ficha2.val = ficha2.val, ficha1.val

    def __calcular(self, blanco: object, tablero: list):
        """Define todas las piezas interactuables con el blanco"""
        return [self.__arriba(blanco, tablero), self.__abajo(blanco, tablero), self.__izquierda(blanco, tablero),
                self.__derecha(blanco, tablero)]

    def __arriba(self, blanco: object, tablero: list) -> object:
        '''Definir la pieza que se va a intercambiar con el blanco en el movimiento de arriba'''
        for ficha in tablero:
            if ficha.y == blanco.y - 1 and blanco.x == ficha.x:
                return ficha
        return None

    def __abajo(self, blanco: object, tablero: list) -> object:
        """Definir la pieza que se va a intercambiar con el blanco en el movimiento de abajo"""
        for ficha in tablero:
            if ficha.y == blanco.y + 1 and ficha.x == blanco.x:
                return ficha
        return None

    def __izquierda(self, blanco: object, tablero: list) -> object:
        """Definir la pieza que se va a intercambiar con el blanco en el movimiento de izquierda"""
        for ficha in tablero:
            if ficha.x + 1 == blanco.x and ficha.y == blanco.y:
                return ficha
        return None

    def __derecha(self, blanco: object, tablero: list) -> object:
        """Definir la pieza que se va a intercambiar con el blanco en el movimiento de derecha"""
        for ficha in tablero:
            if ficha.x - 1 == blanco.x and ficha.y == blanco.y:
                return ficha
        return None

    def __comprobar_no_final(self, tablero: list):
        """Comprobar que el tablero no ha llegado al estado final"""
        valores = ["1", "2", "3", "0", "4", "5", "6", "7", "8"]

        for i in range(len(valores)):
            if valores[i] != tablero[i].val:
                return True
        return False

