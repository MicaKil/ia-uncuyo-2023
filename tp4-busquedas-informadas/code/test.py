from a_star_agent import AStarAgent
from environment import Environment

e = Environment(10, 0.08)
print("Inicio: ", e.start)
print("Destino: ", e.goal, "\n")

a_star_agent = AStarAgent(e)
a_star_agent.search()