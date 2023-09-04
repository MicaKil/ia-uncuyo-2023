# ## Ejercicio A

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un
# entorno completamente observable, determinista y estático.

from random import randint, random
from math import floor
import numpy as np

class Environment:
    def __init__(self):
        self.size = 100
        self.maze = np.full((self.size, self.size), '_', dtype=str)
        self.obstacle_prob = 0.08 #8% de prob
        self.obstacles = floor(self.size**2 * 0.08) #calc de núm de obstáculos
        self.gen_maze()

        #print(self.maze)
    
    # si está vacía la coor (x, y)
    def is_empty(self, x: int, y: int):
        return self.maze[x][y] == '_'
    
    #genera el laberinto 
    def gen_maze(self):
        for i in range(self.obstacles):
            (x, y) = (randint(0, self.size - 1), randint(0, self.size - 1)) 
            if self.is_empty(x, y):
                self.maze[x][y] = 'X'
            else:
                (x, y) = (randint(0, self.size - 1), randint(0, self.size - 1))