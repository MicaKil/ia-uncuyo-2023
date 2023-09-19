from agent import Agent
from node import Node
from queue import *


# whereas breadth-first-search uses a FIFO queue, depth-first

def dfs(agent: Agent, limit):
    node = Node(agent.env)
    if agent.env.goal_test(node.state):
        return node

    frontier = LifoQueue()  # crea una LIFO queue
    frontier.put(node)  # push
    frontier_states = {node.state}  # set con los states de los nodes en frontier

    explored: set = set()  # un set vacío

    while not (frontier.empty()):
        node = frontier.get()  # pop
        if node.path_cost >= limit:
            continue  # Depth limit reached, skip this node
        solution = xfs_util(agent, node, frontier, frontier_states, explored)
        if solution is not None:
            return solution
    return None  # if EMPTY?( frontier) then return failure

# function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
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


def bfs(agent: Agent):
    node = Node(agent.env)
    if agent.env.goal_test(node.state):
        return node
    frontier = Queue()  # crea una FIFO queue
    frontier.put(node)  # enqueue
    frontier_states = {node.state}  # set con los states de los nodes en frontier
    explored: set = set()  # un set vacío
    while not (frontier.empty()):
        node: Node = frontier.get()  # dequeue
        solution = xfs_util(agent, node, frontier, frontier_states, explored)
        if solution is not None:
            return solution
    print("No se encontró solución.")
    print("Estados explorados: ", agent.states_explored)
    agent.env.plot_environment()
    return None  # if EMPTY?( frontier) then return failure


def xfs_util(agent: Agent, node, frontier, frontier_states: set, explored: set):
    frontier_states.remove(node.state)
    explored.add(node.state)
    agent.states_explored += 1
    for action in agent.env.actions:
        child = node.child_node(action)
        if (child.state not in explored) and (child.state not in frontier_states):
            if agent.env.goal_test(child.state):
                agent.show_solution(child, agent.env)
                return child
            frontier.put(child)  # enqueue
            frontier_states.add(child.state)
    return None

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


def uniform_util(agent: Agent, node: Node):
    frontier = PriorityQueue()  # crea una priority queue
    frontier.put(node)  # enqueue con el costo del path como prioridad
    frontier_states = {node.state}  # set con los states de los nodes en frontier
    explored: set = set()  # un set vacío
    while not (frontier.empty()):
        node: Node = frontier.get()  # dequeue - chooses the lowest-cost node in frontier
        frontier_states.remove(node.state)
        if agent.env.goal_test(node.state):
            agent.show_solution(node, agent.env)
            return node
        explored.add(node.state)
        agent.states_explored += 1
        for action in agent.env.actions:
            child = node.child_node(action)
            if (child.state not in explored) and (child.state not in frontier_states):
                frontier.put(child)
                frontier_states.add(child.state)
            elif child.state in frontier_states:  # else if child .STATE is in frontier...
                for i in frontier.queue:
                    if i.state == child.state:
                        if i.path_cost > child.path_cost:  # ...with higher PATH-COST then
                            frontier.queue.remove(i)  # replace that frontier node with child
                            frontier.put(child)
                            frontier_states.add(child.state)
                            break
    print("No se encontró solución.")
    print("Estados explorados: ", agent.states_explored)
    agent.env.plot_environment()
    return None  # if EMPTY?( frontier) then return failure
