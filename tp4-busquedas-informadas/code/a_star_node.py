from node import Node
from environment import Environment

class AStarNode(Node):
    def __lt__(self, other):
        return super().__lt__(other) and self.heuristic() < other.heuristic()

    # def __lt__(self, other): #less than -> define or implement the functionality of the less than operator “<”
    #     return self.path_cost < other.path_cost # Define how nodes should be compared in the priority queue.

    def heuristic(self):
        goal_x, goal_y = self.env.goal
        distance = abs(self.state[0] - goal_x) + abs(self.state[1] - goal_y) # distancia Manhattan (suma de las diferencias absolutas de las coordenadas) 
        return distance