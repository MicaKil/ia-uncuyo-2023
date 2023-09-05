from environment import Environment
from agent import *

class node:
    def __init__(self, env: Environment, state: (int, int), parent):
        self.env = env
        self.state = state
        self.parent = parent #the node in the search tree that generated this node;
        self.action = None #the action that was applied to the parent to generate the node;
        self.path_cost = 0#the cost, traditionally denoted by g(n), of the path from the initial state to the node, as indicated by the parent pointers.
        self.explored = False
        
        #def child_node(self, parent: node, action):
