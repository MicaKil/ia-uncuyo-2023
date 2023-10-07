# Ejercicio C)

# Implementar un agente reflexivo simple para el entorno de la aspiradora del ejercicio anterior.

# 1. La medida de rendimiento premia con un punto al agente por cada recuadro que limpia (aspira) en un período de
# tiempo concreto, a lo largo de una «vida» de 1000 acciones.

# 2. La «dimensión» de la grilla se conoce a priori, pero la distribución de la suciedad y la localización inicial del
# agente no se conocen (aleatorio). Las cuadrículas se mantienen limpias y aspirando se limpia la cuadrícula en que
# se encuentra el agente.

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

from abc import ABC, abstractmethod
from environment import *


class Agent(ABC):  # agente abstracto
    def __init__(self, env: Environment):  # recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.totalLife = 1000  # mil acciones
        self.totalCleaned = 0

        # settea las pos iniciales
        self.X = randint(0, env.get_size_x() - 1)
        self.Y = randint(0, env.get_size_y() - 1)

    def up(self):
        if self.X > 0:
            self.X -= 1
        self.totalLife -= 1  # consume una acción

    def down(self):
        if self.X < self.env.get_size_x() - 1:
            self.X += 1
        self.totalLife -= 1

    def left(self):
        if self.Y > 0:
            self.Y -= 1
        self.totalLife -= 1

    def right(self):
        if self.Y < self.env.get_size_y() - 1:
            self.Y += 1
        self.totalLife -= 1

    def suck(self):
        self.env.set_clean(self.X, self.Y)
        self.totalCleaned += 1
        self.totalLife -= 1

    def idle(self):
        self.totalLife -= 1

    def perspective(self):  # sensa el entorno
        return self.env.is_dirty(self.X, self.Y)

    @abstractmethod
    def think(self):  # implementa las acciones a seguir por el agente
        pass

    # empieza al agente en el entorno
    def start(self):  # actúa mientras tenga vida y hay dirt
        while self.totalLife > 0 and self.env.cur_dirt > 0:
            self.think()
            # self.env.printEnv()
            # print(self.X, self.Y)

    # porcentaje del total limpiado sobre la suciedad inicial
    def get_performance(self):
        return (self.totalCleaned / self.env.get_init_dirt()) * 100

    # getters

    def get_total_life(self):
        return self.totalLife

    def get_total_cleaned(self):
        return self.totalCleaned
