# Implementar un agente basado en objetivos que dado un punto de inicio y
# un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por una grilla de 100x100 en donde los
# obstáculos se generan al azar. Se trata de un entorno completamente observable,
# determinista y estático.
# 2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
# 3. El agente deberá ser capaz de resolver el problema planteado mediante un algoritmo de
# búsqueda A*.
# 4. Proponer una heurística admisible y consistente para el problema.
# 5. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
# a. La matriz generada con los obstáculos
# b. La secuencia de estados completa para llegar desde el estado inicial al estado
# destino. (si es posible)

# The algorithm is identical to UNIFORM-COST-SEARCH except
# that A∗ uses g + h instead of g.

# function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
# node ←a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
# frontier ←a priority queue ordered by PATH-COST, with node as the only element
# explored ←an empty set
# loop do
# if EMPTY?( frontier) then return failure
# node←POP( frontier ) /* chooses the lowest-cost node in frontier */
# if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
# add node.STATE to explored
# for each action in problem.ACTIONS(node.STATE) do
# child ←CHILD-NODE(problem, node, action)
# if child .STATE is not in explored or frontier then
# frontier ←INSERT(child , frontier )
# else if child .STATE is in frontier with higher PATH-COST then
# replace that frontier node with child

from a_star_node import AStarNode
from agent import Agent
from search_algorithms import uniform_util


class AStarAgent(Agent):
    def search(self):
        print("A*")
        node = AStarNode(self.env)

        return uniform_util(self, node)
