from environment import Environment
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from dls_agent import DLSAgent
from uniform_agent import UniformCostAgent

e = Environment(100, 0.08)
print("Inicio: ", e.start)
print("Destino: ", e.goal, "\n")

print("Solución BFS: ")
bfs_a = BFSAgent(e)
bfs_n = bfs_a.search()

print("Solución DFS: ")
dfs_a = DFSAgent(e)
dfs_n = dfs_a.search()

print("Solución DLS: ")
dls_a = DLSAgent(e)
dls_n = dls_a.search(250)

print("Solución Uniforme: ")
u_a = UniformCostAgent(e)
u_n = u_a.search()