# para el caso de un agente con comportamiento totalmente aleatorio. En cada periodo de tiempo,
# el agente toma una acción al azar.

from random import randint
from agent import Agent


class RandAgent(Agent):  # hereda de agent
    def think(self):  # implementa las acciones a seguir por el agente
        action = randint(0, 5)  # toma 0 y 5
        match action:
            case 0:
                self.up()
            case 1:
                self.down()
            case 2:
                self.left()
            case 3:
                self.right()
            case 4:
                self.suck()
            case 5:
                self.idle()
