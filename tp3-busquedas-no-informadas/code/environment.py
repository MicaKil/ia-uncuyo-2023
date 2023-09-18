# ## Ejercicio A

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un
# entorno completamente observable, determinista y estático.

import matplotlib.pyplot as plt
from random import randint
from math import floor
import numpy as np

class Environment:
    def __init__(self, size: int, obstacle_prob: float):
        self.size = size
        self.obstacle_prob = obstacle_prob # % de prob
        self.obstacles = floor(self.size**2 * self.obstacle_prob) #calc de núm de obstáculos
        
        #genera el laberinto
        self.maze = np.zeros((self.size, self.size), dtype=int) #matriz de ceros
        self.gen_maze() 
        
        self.goal = self.set_goal() #coordenada destino
        self.start = self.gen_coordenada() #coordenada inicial

        self.actions = [self.up, self.down, self.left, self.right]
    
    # si está vacía la coordenada (x, y)
    def is_empty(self, x: int, y: int):
        return self.maze[x][y] == 0 or self.maze[x][y] == 3
    
    
    #genera el laberinto 
    def gen_maze(self):
        for i in range(self.obstacles):
            (x, y) =  self.gen_coordenada()
            self.maze[x][y] = 1

    # retorna 1 coordenada al azar
    def rand_coordenada(self): 
        return (randint(0, self.size - 1), randint(0, self.size - 1))
    
    # genera 1 coordenada (tuple) en un lugar no ocupado del laberinto  
    def gen_coordenada(self):
        (x, y) = self.rand_coordenada() 
        while not (self.is_empty(x, y)): 
            (x, y) = self.rand_coordenada()
        return (x, y)
    
    # settea al goal randomly
    def set_goal(self):
        (x, y) = self.gen_coordenada()
        self.maze[x][y] = 3
        return (x, y)
    
    def goal_test(self, state):
        (x, y) = state
        return self.maze[x][y] == 3
    
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
    
    def plot_environment_util(self):
        # crea una copia del laberinto para no modificar el original
        maze_copy = np.copy(self.maze)

        # marca el inicio en el laberinto (el destino ya está marcado con un 3)
        start_x, start_y = self.start
        goal_x, goal_y = self.goal
        maze_copy[start_x][start_y] = 2  # Marcar inicio con un valor diferente

        # crea un mapa de colores personalizado
        cmap = plt.cm.colors.ListedColormap(['white', 'black', 'red', 'green'])

        # crea la representación gráfica del laberinto
        plt.imshow(maze_copy, cmap=cmap, interpolation='nearest', vmin=0, vmax=3)

        # define los límites de la leyenda
        bounds = [0, 1, 2, 3, 4]
        norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

        # crea una leyenda personalizada
        cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), cmap=cmap, boundaries=bounds)
        cbar.set_ticks([0.5, 1.5, 2.5, 3.5])
        cbar.set_ticklabels(['Vacío', 'Obstáculo', f'Inicio {self.start}', f'Destino {self.goal}'])

    def plot_environment(self):
        self.plot_environment_util()
        plt.show()