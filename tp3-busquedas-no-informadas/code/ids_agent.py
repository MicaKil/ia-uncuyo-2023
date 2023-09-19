# function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
# for depth = 0 to ∞ do
# result ←DEPTH-LIMITED-SEARCH(problem, depth)
# if result != cutoff then return result

from search_algorithms import *


class IDSAgent(Agent):
    def search(self):
        for depth in range(1000):
            result = dfs(self, depth)
            if result is not None:
                return result
        print("No se encontró solución.")
        print("Estados explorados: ", self.states_explored)
        (self.env.plot_environment())
        return None
