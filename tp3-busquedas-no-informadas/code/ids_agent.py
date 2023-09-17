#function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
# for depth = 0 to ∞ do
# result ←DEPTH-LIMITED-SEARCH(problem, depth)
# if result != cutoff then return result

from agent import Agent
from dfs import *

class IDSAgent(Agent):
    def search(self):
        for depth in range(1000):
            result = dfs(self, depth)
            if result != None:
                return result
        return None