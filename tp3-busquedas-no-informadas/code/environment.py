# ## Ejercicio A

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un
# entorno completamente observable, determinista y estático.

from random import randint, random
from math import floor
import numpy as np

class Environment:
    
    def __init__(self, size: int, obstacle_prob: float):
        self.size = size
        self.obstacle_prob = obstacle_prob # % de prob
        self.obstacles = floor(self.size**2 * self.obstacle_prob) #calc de núm de obstáculos
        
        #genera el laberinto
        self.maze = np.full((self.size, self.size), '_', dtype=str)
        self.gen_maze() 
        
        self.goal = self.set_goal() #coor destino
        self.start = self.gen_coor() #coor inicial

        self.actions = [self.up, self.down, self.left, self.right]
    
    # si está vacía la coor (x, y)
    def is_empty(self, x: int, y: int):
        return self.maze[x][y] == '_' or self.maze[x][y] == 'G'
    
    
    #genera el laberinto 
    def gen_maze(self):
        for i in range(self.obstacles):
            (x, y) =  self.gen_coor()
            self.maze[x][y] = 'X'

    # retorna 1 coordenada al azar
    def rand_coor(self): 
        return (randint(0, self.size - 1), randint(0, self.size - 1))
    
    # genera 1 coordenada (tuple) en un lugar no ocupado del laberinto  
    def gen_coor(self):
        (x, y) = self.rand_coor() 
        while not (self.is_empty(x, y)): 
            (x, y) = self.rand_coor()
        return (x, y)
    
    # settea al goal randomly
    def set_goal(self):
        (x, y) = self.gen_coor()
        self.maze[x][y] = 'G'
        return (x, y)
    
    def goal_test(self, state):
        (x, y) = state
        return self.maze[x][y] == 'G'
    
    def step_cost(action, state):
        return 1

    # actions
    def up(self, x: int, y: int):
        if x > 0 and self.is_empty(x - 1, y):
            x -= 1
        return (x, y)
    
    def down(self, x: int, y: int):
        if (x < self.size - 1) and self.is_empty(x + 1, y):
            x += 1
        return (x, y)

    def left(self, x: int, y: int):
        if y > 0 and self.is_empty(x, y - 1):
            y -= 1
        return (x, y)
    
    def right(self, x: int, y: int):
        if (y < self.size - 1) and self.is_empty(x, y + 1):
            y += 1
        return (x, y)