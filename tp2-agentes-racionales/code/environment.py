# Ejercicio B)
# Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según 
# las siguientes especificaciones:

# 1. La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de
# tiempo concreto, a lo largo de una «vida» de 1000 acciones.

# 2. La «dimensión» de la grilla se conoce a priori, pero la distribución de la suciedad y la localización inicial del
# agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula en que se
# encuentra el agente.

# 3. Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso en que
# lo pueda llevar fuera de la grilla.

# 4. Las acciones permitidas son:
#    1. Arriba
#    2. Abajo
#    3. Izquierda
#    4. Derecha
#    5. Limpiar (aspirar)
#    6. NoHacerNada

# 5. El agente percibe su locación y si esta contiene suciedad

# **Posible** interfaz a utilizar:
# ```
# class Environment:
# 	def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate)		
#     def accept_action(self,action):
#     def is_dirty(self):
# 	  def get_performance(self): 
#  	  def print_environment(self): 
# ```

from random import randint, random
import numpy as np


class Environment:
    def __init__(self, size_x: int, size_y: int, dirt_rate: float):
        self.sizeX = int(size_x)
        self.sizeY = int(size_y)

        if size_x <= 0 or size_y <= 0:
            raise ValueError("sizeX y sizeY deben ser enteros mayores a cero (0).")

        self.grid = np.zeros((self.sizeX, self.sizeY))  # inicializa la grilla

        self.dirt_rate = dirt_rate
        self.initial_dirt = 0
        # llena de forma aleatoria la grilla con puntos de suciedad

        self.gen_dirt()  # genera la suciedad del entorno

        self.cur_dirt = self.initial_dirt

    def gen_dirt(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if random() <= self.dirt_rate:
                    self.grid[i][j] = 1
                    self.initial_dirt += 1

        if self.initial_dirt == 0:  # si no se generó suciedad...
            self.grid[randint(0, self.sizeX - 1)][randint(0, self.sizeY - 1)] = 1  # en un lugar random la coloca
            self.initial_dirt = 1

    # retorna si está sucia la pos x y
    def is_dirty(self, x, y):
        return self.grid[x][y] == 1

        # getters y setters

    def get_size_x(self):
        return self.sizeX

    def get_size_y(self):
        return self.sizeY

    def set_clean(self, x, y):
        self.grid[x][y] = 0
        self.cur_dirt -= 1

    def get_init_dirt(self):
        return self.initial_dirt

    def print_env(self):
        print(self.grid)
