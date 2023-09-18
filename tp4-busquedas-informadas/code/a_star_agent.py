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

#The algorithm is identical to UNIFORM-COST-SEARCH except
#that A∗ uses g + h instead of g.

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

from queue import PriorityQueue

from agent import Agent
from environment import Environment
from a_star_node import AStarNode

class AStarAgent(Agent):
    def search(self):
        print("A*")
        node = AStarNode(self.env)
        
        frontier = PriorityQueue() #crea una priority queue
        frontier.put(node) # enqueue con el costo del path como prioridad
        frontier_states = {node.state} #set con los states de los nodes en frontier

        explored: set = set() # un set vacío

        while not (frontier.empty()):
            node: AStarNode = frontier.get() #dequeue - chooses the lowest-cost node in frontier
            frontier_states.remove(node.state)

            if self.env.goal_test(node.state):
                self.show_solution(node, self.env)
                return node
            
            explored.add(node.state)
            self.states_explored += 1

            for action in self.env.actions:
                child = node.child_node(action)
                if (child.state not in explored) and (child.state not in frontier_states):
                    frontier.put(child)
                    frontier_states.add(child.state)
                elif (child.state in frontier_states): #else if child .STATE is in frontier... 
                    for i in frontier.queue:
                        if i.state == child.state:
                            if i.path_cost > child.path_cost: #...with higher PATH-COST then
                                frontier.queue.remove(i) #replace that frontier node with child
                                frontier.put(child)
                                frontier_states.add(child.state)
                                break

        print("No se encontró solución.")
        print("Estados explorados: ", self.states_explored)
        self.env.plot_environment()
        return None # if EMPTY?( frontier) then return failure

