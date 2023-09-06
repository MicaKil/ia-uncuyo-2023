from environment import Environment
from agent import Agent
from node import Node
from bfs import *


e = Environment(100, 0.08)
print("Destino: ", e.goal)
agent = BFS_Agent(e)

sol = agent.search()
for i in sol:
    print(i)

print("Estados explorados: ", agent.states_explored)