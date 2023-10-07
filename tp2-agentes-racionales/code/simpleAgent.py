from random import randint
from agent import Agent


class SimpleAgent(Agent):  # hereda de agent
    def think(self):  # implementa las acciones a seguir por el agente
        if self.perspective():
            self.suck()
        action = randint(0, 3)  # toma 0 y 3
        match action:
            case 0:
                self.up()
            case 1:
                self.down()
            case 2:
                self.left()
            case 3:
                self.right()
