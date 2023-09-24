class Node:
    # cuando crea un nodo por 1ra vez
    def __init__(self, problem, state):
        self.problem = problem
        self.state = state
        self.value = problem.heuristic_cost()

    def __str__(self):
        return f"Node: State={self.state}"
