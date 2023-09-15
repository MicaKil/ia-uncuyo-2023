#Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un entorno completamente observable, determinista y estático.
# ![Alt text](pics/image.png)
# 2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
# 3. El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:
#    - Búsqueda por Anchura
#    - Búsqueda por Profundidad 
#    - Búsqueda Por Profundidad limitada
#    - Búsqueda Uniforme
# 4. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
#    - La matriz generada con los obstáculos (opcional)
#    - La secuencia de estados completa para llegar desde el estado inicial al estado destino. (si es posible)

#whereas breadth-first-search uses a FIFO queue, depth-first search uses a LIFO queue.

from queue import *

from node import Node
from agent import Agent

class DFS_Agent(Agent):
    def search(self):
        node = Node(self.env)
        if self.env.goal_test(node.state):
            return node
        
        frontier = LifoQueue() #crea una LIFO queue
        frontier.put(node) # enqueue
        frontier_states = {node.state} #set con los states de los nodes en frontier

        explored: set = set() # un set vacío 

        while not (frontier.empty()) and node.path_cost < 1000:
            print(frontier)
            node: Node = frontier.get() #dequeue
            frontier_states.remove(node.state)
            
            explored.add(node.state)

            for action in self.env.actions:
                child = node.child_node(action)
                self.states_explored += 1
                if (child.state not in explored) and (child.state not in frontier_states):
                    if self.env.goal_test(child.state):
                        return child.solution()
                    frontier.put(child) #enqueue
                    frontier_states.add(child.state)
        return None # if EMPTY?( frontier) then return failure