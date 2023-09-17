#Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se trata de un entorno completamente observable, determinista y estático.
# 2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
# 3. El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:
#    - Búsqueda por Anchura
#    - Búsqueda por Profundidad 
#    - Búsqueda Por Profundidad limitada
#    - Búsqueda Uniforme
# 4. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
#    - La matriz generada con los obstáculos (opcional)
#    - La secuencia de estados completa para llegar desde el estado inicial al estado destino. (si es posible)

from environment import Environment
from agent import Agent
from node import Node
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from dls_agent import DLSAgent
from ids_agent import IDSAgent
from uniform_agent import UniformCostAgent

e = Environment(100, 0.08)
print("Matriz: \n", e.maze)
print("Inicio: ", e.start)
print("Destino: ", e.goal, "\n")

print("Solución BFS: ")
bfs_a = BFSAgent(e)
bfs_n = bfs_a.search()
# bfs_n.show_path()
print("Costo de la solución: ", bfs_n.path_cost)
print("Estados explorados BFS: ", bfs_a.states_explored, "\n")

print("Solución DFS: ")
dfs_a = DFSAgent(e)
dfs_n = dfs_a.search()
if dfs_n == None:
    print("No se encontró solución")
else:
    # dfs_n.show_path()
    print("Costo de la solución: ", dfs_n.path_cost)
print("Estados explorados DFS: ", dfs_a.states_explored, "\n")

print("Solución DLS: ")
dls_a = DLSAgent(e)
dls_n = dls_a.search(250)
if dls_n == None:
    print("No se encontró solución")
else:
    # dls_n.show_path()
    print("Costo de la solución: ", dls_n.path_cost)
print("Estados explorados DLS: ", dls_a.states_explored, "\n")

print("Solución IDS: ")
ids_a = IDSAgent(e)
ids_n = ids_a.search()
if ids_n == None:
    print("No se encontró solución")
else:
    # ids_n.show_path()
    print("Costo de la solución: ", ids_n.path_cost)
print("Estados explorados IDS: ", ids_a.states_explored, "\n")

print("Solución Uniforme: ")
u_a = UniformCostAgent(e)
u_n = u_a.search()
# u_n.show_path()
print("Costo de la solución: ", u_n.path_cost)
print("Estados explorados Uniforme: ", u_a.states_explored)
