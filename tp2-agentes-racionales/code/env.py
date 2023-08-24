# Ejercicio B)
# Implementar un simulador que determine la medida de rendimiento para el entorno del mundo de la aspiradora según 
# las siguientes especificaciones:

    # 1. La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de tiempo concreto, 
    # a lo largo de una «vida» de 1000 acciones. 

    # 2. La «dimensión» de la grilla se conoce a priori pero la distribución de la suciedad y la localización inicial del agente no se 
    # conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula en que se encuentra el agente.

    # 3. Las acciones Izquierda, Derecha, Arriba, Abajo mueven al agente en dichas direcciones, excepto en el caso en que lo pueda 
    # llevar fuera de la grilla.

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

from random import randint
import numpy as np

class Environment:
    def __init__(self, sizeX: int, sizeY: int, dirt_rate: float):
        self.sizeX = int(sizeX)
        self.sizeY = int(sizeY)
        self.grid = np.zeros((self.sizeX, self.sizeY)) 
        
        self.dirt_rate = dirt_rate
        self.initialDirt = 0 
        # llena de forma aleatoria la grilla con puntos de suciedad
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if randint(0, 9) <= dirt_rate*10:
                    self.grid[i][j] = 1
                    self.initialDirt += 1
    
    # #retorna % de casillas limpias
    # def getPerformance(self): 
    #     # cuenta el núm de casillas limpias
    #     cleanCount = 0
    #     for i in range(self.sizeX):
    #         for j in range(self.sizeY):
    #             if self.grid[i][j] == 0:
    #                 cleanCount += 1
    #     #la performance es cleanCount/sobre el total de casillas * 100
    #     return cleanCount/(self.sizeX*self.sizeY) * 100
    
    # retorna si está sucia la pos x y
    def isDirty(self, x, y):
        if self.grid[x][y] == 1:
            return True
        return False
    
    def getSizeX(self):
        return self.sizeX
    
    def getSizeY(self):
        return self.sizeY
    
    def setClean(self, x, y):
        self.grid[x][y] = 0

    def getInitDirt(self):
        return self.initialDirt

    def printEnv(self):
        print(self.grid)
        print(" ")

# ------------------------------------------------------------------------------------------------------------------------------------------
# ## Ejercicio G)
# Desarrollar un agente reflexivo que funcione para el entorno FrozenLake de la biblioteca Gymnasium. (OPCIONAL)

# **Descripción:**

# FrozenLake  es un entorno de cuadrícula donde un agente debe navegar desde un punto de inicio hasta una meta, evitando caer en los agujeros del hielo. 

# La medida de rendimiento recompensa al agente con un punto por cada casilla que cruza exitosamente sin caer en un agujero durante un período de tiempo específico, a lo largo de una vida de 1000 acciones.

# La dimensión de la cuadrícula se conoce de antemano, pero la distribución de los agujeros y la ubicación inicial del agente no se conocen (son aleatorios). Las casillas permanecen sólidas una vez cruzadas, y el objetivo del agente es alcanzar la meta sin caer en un agujero.
# Las acciones *"Left", "Right", "Up" y "Down"* mueven al agente en esas direcciones, excepto cuando dicho movimiento sacaría al agente de la cuadrícula o lo llevaría a un agujero.

# Las acciones permitidas son:
# - 0: Move left
# - 1: Move down
# - 2: Move right
# - 3: Move up

# El agente percibe su ubicación y si esa casilla contiene un agujero o es la meta.

# A continuación una porción de código que implementa un agente aleatorio en el entorno frozenLake. Se puede tomar como guía para implementar un agente reactivo que funcione sobre el mismo entorno.

# ------------------------------------------------------------------------------------------------------------------------------------------
# ## Ejercicio H)
# Evaluar el desempeño del agente agente reflexivo (medida de desempeño y unidades de tiempo consumidas) para: (OPCIONAL)

# 1. Entornos de : 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
# 2. Porcentaje de agujeros en el ambiente: 0.1, 0,2 0,4, 0.8
# 3. Repetir 10 veces cada combinación.