from Juego import *

"""Juego del 8-Puzzle, resolución a traves de un sistema de inferencia visto en la asignatura de Inteligencia Artificial().
    Consiste en mover 8 piezas en un tablero de 9 hasta que queden totalmente ordenadas. Como en esta posición:
    
    -------------
	| 1 | 2 | 3 |
	-------------
	| 0 | 4 | 5 |
	-------------
	| 6 | 7 | 8 |
	-------------
	
"""
a = Juego() # instancia de un objeto de la clase juego.
a.inferencia() # llamada a la función de resolución del puzzle.
