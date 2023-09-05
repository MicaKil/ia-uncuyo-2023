
from abc import ABC, abstractmethod
from random import randint
from environment import *

class Agent(ABC): #agente abstracto
    def __init__(self, env: Environment): #recibe como parámetro un objeto de la clase Environment
        self.env = env
        self.totalLife = 1000 #mil acciones

        # settea las pos iniciales
        (self.X, self.Y) = (env.start)

    def up(self):
        if self.X > 0 and self.env.is_empty(self.X - 1, self.Y):
            self.X -= 1
        self.totalLife -= 1 #consume una acción
        return (self.X, self.Y)
    
    def down(self):
        if (self.X < self.env.getSizeX() - 1) and self.env.is_empty(self.X + 1, self.Y):
            self.X += 1
        self.totalLife -= 1
        return (self.X, self.Y)

    def left(self):
        if self.Y > 0 and self.env.is_empty(self.X, self.Y - 1):
            self.Y -= 1
        self.totalLife -= 1
        return (self.X, self.Y)
    
    def right(self):
        if (self.Y < self.env.getSizeY() - 1) and self.env.is_empty(self.X, self.Y + 1):
            self.Y += 1
        self.totalLife -= 1
        return (self.X, self.Y)