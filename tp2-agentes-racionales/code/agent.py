#Ejercicio C)

# Implementar un agente reflexivo simple para el entorno de la aspiradora del ejercicio anterior.

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

from random import randint
from env import *

class Agent:
    def __init__(self, env: Environment): #recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.totalLife = 1000 #mil acciones
        self.totalCleaned = 0 

        # setea las pos iniciales
        self.X = randint(0, env.getSizeX() - 1)
        self.Y = randint(0, env.getSizeY() - 1)

    def up(self):
        if self.X > 0:
            self.X -= 1
        self.totalLife -= 1 #consume una acción
    
    def down(self):
        if self.X < self.env.getSizeX() - 1:
            self.X += 1
        self.totalLife -= 1

    def left(self):
        if self.Y > 0:
            self.Y -= 1
        self.totalLife -= 1
    
    def right(self):
        if self.Y < self.env.getSizeY() - 1:
            self.Y += 1
        self.totalLife -= 1

    def suck(self): 
        self.env.setClean(self.X, self.Y)
        self.totalCleaned += 1
        self.totalLife -= 1

    def perspective(self): #sensa el entorno
        if self.env.isDirty(self.X, self.Y): #si está sucio limpia
            self.suck()

    def think(self): # implementa las acciones a seguir por el agente
        self.perspective()
        _case = randint(0, 4)
        if _case == 0:
            self.up()
        elif _case == 1:
            self.down()
        elif _case == 2:
            self.left()
        else:
            self.right()

    def getTotalLife(self):
        return self.totalLife
    
    def getTotalCleaned(self):
        return self.totalCleaned
    
    def getPerformance(self):
        try:
            return (self.totalCleaned/self.env.getInitDirt()) * 100
        except:
            return 100
    