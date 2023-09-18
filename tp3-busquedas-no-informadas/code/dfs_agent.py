from agent import Agent
from dfs import *

class DFSAgent(Agent):
    def search(self):
        return dfs(self, float('inf'))

    # def search(self):
    #     global explored
    #     explored = set() # un set vacío 
    #     return self.recursive_dfs(Node(self.env))
    
    # def recursive_dfs(self, node):
    #     if self.env.goal_test(node.state):
    #         return node
    #     if node.path_cost > 500:
    #         return None

    #     global explored
    #     explored.add(node.state)

    #     for action in self.env.actions:
    #         child = node.child_node(action)
    #         self.states_explored += 1
    #         if (child.state not in explored):
    #             result = self.recursive_dfs(child)
    #             if result != None:
    #                 return result

    #     return None