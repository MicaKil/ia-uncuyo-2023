from abc import ABC, abstractmethod
from random import randint
from environment import *

class Agent(ABC): #agente abstracto
    def __init__(self, env: Environment): #recibe como parámetro un objeto de la clase Environment
        self.env = env
        (self.X, self.Y) = (env.start) # settea la pos inicial
        self.states_explored = 0
        self.actions = [self.up, self.down, self.left, self.right]

    def up(self):
        (self.X, self.Y) = self.env.up(self.X, self.Y)
        return (self.X, self.Y)
    
    def down(self):
        (self.X, self.Y) = self.env.down(self.X, self.Y)
        return (self.X, self.Y)

    def left(self):
        (self.X, self.Y) = self.env.left(self.X, self.Y)
        return (self.X, self.Y)
    
    def right(self):
        (self.X, self.Y) = self.env.right(self.X, self.Y)
        return (self.X, self.Y)
    
    @abstractmethod
    def search(self):
        pass