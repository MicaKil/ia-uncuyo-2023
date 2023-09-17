from environment import Environment
from agent import *

class Node:
    # cuando crea un nodo por 1ra vez
    def __init__(self, env: Environment):
        self.env = env
        
        self.state = self.env.start
        self.parent = None #the node in the search tree that generated this node;
        self.action = None #the action that was applied to the parent to generate the node;
        self.path_cost = 0 #the cost, traditionally denoted by g(n), of the path from the initial state to the node, as indicated by the parent pointers.
    
    def __str__(self):
        return f"Node: State={self.state}, Action={self.action}, Path Cost={self.path_cost}"

    def __lt__(self, other): #less than -> define or implement the functionality of the less than operator “<”
        return self.path_cost < other.path_cost # Define how nodes should be compared in the priority queue.
    
    # function CHILD-NODE(problem, parent , action) returns a node
    #     return a node with
    #     STATE = problem.RESULT(parent.STATE, action),
    #     PARENT = parent, 
    #     ACTION = action,
    #     PATH-COST = parent.PATH-COST + problem.STEP-COST(parent.STATE, action)

    #lo llama el padre del nodo
    def child_node(self, action):
        child = Node(self.env)
        (x, y) = self.state #posiciones viejas (la del padre)
        child.state = action(x, y)
        child.parent = self
        child.action = action.__name__
        child.path_cost = self.path_cost + 1
        return child
    
    def get_path(self):
        path = []
        path.insert(0, f"State = {self.state}, Action = {self.action}")
        while self.parent != None:
            self = self.parent
            path.insert(0, f"State = {self.state}, Action = {self.action}")

        return path

    def show_path(self):
        path_cost = self.path_cost
        path = self.get_path()
        for i in path:
            print(i)
        print("Costo de la solución: ", path_cost)
