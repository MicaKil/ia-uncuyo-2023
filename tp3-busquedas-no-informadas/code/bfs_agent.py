from queue import *

from environment import Environment
from node import Node
from agent import Agent

#function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
# node ←a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
# if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
# frontier ←a FIFO queue with node as the only element
# explored ←an empty set
# loop do
    # if EMPTY?( frontier) then return failure
    # node←POP( frontier ) /* chooses the shallowest node in frontier */
    # add node.STATE to explored
    # for each action in problem.ACTIONS(node.STATE) do
        # child ←CHILD-NODE(problem, node, action)
        # if child .STATE is not in explored or frontier then
            # if problem.GOAL-TEST(child .STATE) then return SOLUTION(child )
            # frontier ←INSERT(child , frontier )

class BFSAgent(Agent):
    def search(self):
        node = Node(self.env)
        if self.env.goal_test(node.state):
            return node
        
        frontier = Queue() #crea una FIFO queue
        frontier.put(node) # enqueue
        frontier_states = {node.state} #set con los states de los nodes en frontier

        explored: set = set() # un set vacío 

        while not (frontier.empty()):
            node: Node = frontier.get() #dequeue
            frontier_states.remove(node.state)

            explored.add(node.state)
            self.states_explored += 1

            for action in self.env.actions:
                child = node.child_node(action)
                if (child.state not in explored) and (child.state not in frontier_states):
                    if self.env.goal_test(child.state):
                        self.show_solution(child, self.env)
                        return child
                    frontier.put(child) #enqueue
                    frontier_states.add(child.state)

        print("No se encontró solución.")
        print("Estados explorados: ", self.states_explored)
        self.env.plot_environment()
        return None # if EMPTY?( frontier) then return failure