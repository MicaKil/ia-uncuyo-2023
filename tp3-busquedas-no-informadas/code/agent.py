# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar.
# Se trata de un entorno completamente observable, determinista y estático.
# ![Alt text](pics/image.png)
# 2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
# 3. El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no
# informada:
#    - Búsqueda por Anchura
#    - Búsqueda por Profundidad
#    - Búsqueda Por Profundidad limitada
#    - Búsqueda Uniforme
# 4. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
#    - La matriz generada con los obstáculos (opcional)
#    - La secuencia de estados completa para llegar desde el estado inicial al estado destino. (si es posible)

from abc import ABC, abstractmethod
from environment import Environment
from search_algorithms import *
from node import Node


class Agent(ABC):  # agente abstracto
    def __init__(self, env: Environment):  # recibe como parámetro un objeto de la clase Environment
        self.env = env
        (self.X, self.Y) = env.start  # settea la pos inicial
        self.states_explored = 0
        self.actions = [self.up, self.down, self.left, self.right]

    def up(self):
        (self.X, self.Y) = self.env.up(self.X, self.Y)
        return self.X, self.Y

    def down(self):
        (self.X, self.Y) = self.env.down(self.X, self.Y)
        return self.X, self.Y

    def left(self):
        (self.X, self.Y) = self.env.left(self.X, self.Y)
        return self.X, self.Y

    def right(self):
        (self.X, self.Y) = self.env.right(self.X, self.Y)
        return self.X, self.Y

    @abstractmethod
    def search(self):
        pass

    def show_solution(self, node, env: Environment):
        print("¡Solución encontrada!")
        node.show_path()
        print("Estados explorados: ", self.states_explored)
        env.plot_environment()
        return None


class BFSAgent(Agent):
    def search(self):
        return bfs(self)


class DFSAgent(Agent):
    def search(self):
        result = dfs(self, float('inf'))
        if result is None:
            print("Solución no encontrada")
            print("Estados explorados: ", self.states_explored)
            self.env.plot_environment()
        return result


class DLSAgent(Agent):
    def search(self, limit):
        result = dfs(self, limit)
        if result is None:
            print("Solución no encontrada")
            print("Estados explorados: ", self.states_explored)
            self.env.plot_environment()
        return result


# function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
# for depth = 0 to ∞ do
#   result ←DEPTH-LIMITED-SEARCH(problem, depth)
#   if result != cutoff then return result
class IDSAgent(Agent):
    def search(self):
        for depth in range(1000):
            result = dfs(self, depth)
            if result is not None:
                return result
        print("No se encontró solución.")
        print("Estados explorados: ", self.states_explored)
        (self.env.plot_environment())
        return None


class UniformCostAgent(Agent):
    def search(self):
        node = Node(self.env)
        return uniform_util(self, node)
