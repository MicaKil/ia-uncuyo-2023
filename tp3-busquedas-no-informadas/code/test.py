from environment import Environment
from agent import Agent
from node import Node
from bfs import *
from dfs import *

def printSol(agent: Agent):
    sol = agent.search()
    if sol == None:
        print("No encontró la solución")
    else:
        for i in sol[0]:
            print(i)
    print("Costo de la solución: ", sol[1])
    print("Estados explorados: ", agent.states_explored)

e = Environment(10, 0.08)
print("Matriz: \n", e.maze)
print("Inicio: ", e.start)
print("Destino: ", e.goal)

printSol(BFS_Agent(e))
printSol(DFS_Agent(e))