from agent import BFSAgent, DFSAgent, DLSAgent, UniformCostAgent
from runner import runner

agents = [BFSAgent, DFSAgent, DLSAgent, UniformCostAgent]
size = 100
obstacle_prob = 0.08
limit = 250
num_runs = 30

runner(agents, size, obstacle_prob, limit, num_runs)
