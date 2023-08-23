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
    def __init__(self, sizeX: int, sizeY: int, dirt_rate):
        self.sizeX = int(sizeX)
        self.sizeY = int(sizeY)
        self.grid = np.zeros((self.sizeX, self.sizeY))
        print(self.grid)
        self.init_posX = randint(0, sizeX - 1) # -1 pq lo incluye
        self.init_posY = randint(0, sizeY - 1) 
        self.dirt_rate = dirt_rate

a = Environment(2, 3, 0.1)


# ------------------------------------------------------------------------------------------------------------------------------------------
# ## Ejercicio C)
# Implementar un agente reflexivo simple para el entorno de la aspiradora del ejercicio anterior.

# Posible interfaz para el Agente:
# ```
# class Agent:           
#     def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
#     def up(self):
#     def down(self):      
#     def left(self):
#     def right(self):
#     def suck(self): # Limpia
#     def idle(self): # no hace nada
#     def perspective(self,env): #sensa el entorno
#     def think(self): # implementa las acciones a seguir por el agente
# ```

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