# UNIFORM-COST-SEARCH

from node import Node
from agent import Agent
from search_algorithms import uniform_util


class UniformCostAgent(Agent):
    def search(self):
        node = Node(self.env)
        return uniform_util(self, node)
