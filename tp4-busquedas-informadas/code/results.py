from runner import runner
from agent import BFSAgent, DFSAgent, DLSAgent, UniformCostAgent
from a_star_agent import AStarAgent

agents = [BFSAgent, DFSAgent, DLSAgent, UniformCostAgent, AStarAgent]
size = 100
obstacle_prob = 0.08
limit = 250
num_runs = 30

runner(agents, size, obstacle_prob, limit, num_runs)
