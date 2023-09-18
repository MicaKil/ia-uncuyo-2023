from agent import Agent
from node import Node

from queue import *
        
#function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
# node ←a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
# if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
# frontier ←a FIFO queue with node as the only element #whereas breadth-first-search uses a FIFO queue, depth-first search uses a LIFO queue.

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

def dfs(agent: Agent, limit):
    node = Node(agent.env)
    if agent.env.goal_test(node.state):
        return node
    
    frontier = LifoQueue() #crea una LIFO queue
    frontier.put(node) # enqueue
    frontier_states = {node.state} #set con los states de los nodes en frontier

    explored: set = set() # un set vacío 

    #print_queue(frontier)
    while not (frontier.empty()):
        #print("Iteración: ", i)
        node = frontier.get() #dequeue
        #print(node)

        if node.path_cost >= limit:
            continue # Depth limit reached, skip this node

        frontier_states.remove(node.state)
        explored.add(node.state)
        agent.states_explored += 1
        #print("Explored: ", explored)
        for action in agent.env.actions:
            child = node.child_node(action)
            if (child.state not in explored) and (child.state not in frontier_states):
                if agent.env.goal_test(child.state):
                    agent.show_solution(child, agent.env)
                    return child
                frontier.put(child) #enqueue
                frontier_states.add(child.state)

    print("Solución no encontrada")
    print("Estados explorados: ", agent.states_explored)
    return None # if EMPTY?( frontier) then return failure