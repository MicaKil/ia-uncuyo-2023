
from agent import Agent
from search_algorithms import bfs


class BFSAgent(Agent):
    def search(self):
        return bfs(self)
