from node import Node
from datetime import datetime


class AStarNode(Node):
    node_count = 0

    def __init__(self, env):
        super().__init__(env)
        self.estimated_cost = self.path_cost + self.heuristic()
        self.creation_time = AStarNode.node_count
        AStarNode.node_count += 1

    def __str__(self):
        return (f"Node: State={self.state}, Action={self.action}, Path Cost={self.path_cost}, "
                f"Estimated Cost={self.estimated_cost}, Creation Time={self.creation_time}")

    def __lt__(self, other):  # define or implement the functionality of the less than operator “<”
        # compara estimated_cost
        if self.estimated_cost < other.estimated_cost:
            return True
        elif self.estimated_cost > other.estimated_cost:
            return False
        else:
            # si los estimated_costs son iguales, compara creation_time
            return self.creation_time > other.creation_time  # se queda con el más nuevo

    def heuristic(self):
        goal_x, goal_y = self.env.goal
        # distancia Manhattan (suma de las diferencias absolutas de las coordenadas)
        distance = abs(self.state[0] - goal_x) + abs(self.state[1] - goal_y)
        return distance

    def child_node(self, action):
        child = AStarNode(self.env)
        (x, y) = self.state  # posiciones viejas (la del padre)
        child.state = action(x, y)
        child.parent = self
        child.action = action.__name__
        child.path_cost = self.path_cost + 1
        child.estimated_cost = child.path_cost + child.heuristic()
        return child
