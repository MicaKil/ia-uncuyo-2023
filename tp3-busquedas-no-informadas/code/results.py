# SIN IDS

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por  una grilla de 100x100 en donde los obstáculos se generan al azar. Se
# trata de un entorno completamente observable, determinista
# y estático.
# 2. Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha)
# 3. El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no
# informada:
#    - Búsqueda por Anchura
#    - Búsqueda por Profundidad
#    - Búsqueda Por Profundidad limitada
#    - Búsqueda Uniforme
# 4. Al finalizar el proceso de formulación se deberán imprimir por pantalla:
#    - La matriz generada con los obstáculos (opcional)
#    - La secuencia de estados completa para llegar desde el estado inicial al estado destino. (si es posible)

# Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio con una tasa de obstáculos del 8 por ciento,
# calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que
# fue posible). Evaluar cada uno de los algoritmos sobre el mismo conjunto de datos generado.  Presentar los
# resultados en un gráfico de cajas y bigotes o boxplots.

# Dentro tp3-busquedas-no-informadas crear un archivo de nombre no-informada-results.csv en formato csv (comma
# separated values) con los resultados de las 30 ejecuciones para cada uno de los algoritmos evaluados. El formato
# deberá ser el siguiente: agent_name, run_n, estate_n, solution_found

from environment import Environment
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from dls_agent import DLSAgent
from uniform_agent import UniformCostAgent

import csv
from statistics import mean, stdev
import pandas as pd
import matplotlib.pyplot as plt


# define una función para ejecutar un algoritmo y registrar los resultados
def run_algorithm(agent, env, run_number):
    agent_name = agent.__name__
    agent_instance = agent(env)
    if agent_name == "DLSAgent":
        result = agent_instance.search(limit)
    else:
        result = agent_instance.search()  # ejecuta el algoritmo
    states_explored = agent_instance.states_explored
    sol_founded = False
    path_cost = None
    if result != None:
        sol_founded = True
        path_cost = result.path_cost
    return {"agent_name": agent_name, "run_number": run_number, "states_explored": states_explored,
            "solution_found": sol_founded, "path_cost": path_cost}


# ----------------------------------------------------------------------------------------------
agents = [BFSAgent, DFSAgent, DLSAgent, UniformCostAgent]
size = 100
obstacle_prob = 0.08
limit = 250
num_runs = 30

results = []
environments = []

print("Ejecutando algoritmos...")
for run_number in range(1, num_runs + 1):
    print(f"Run number: {run_number}")
    env = Environment(size, obstacle_prob)
    environments.append(env)
    for agent in agents:
        result = run_algorithm(agent, env, run_number)
        results.append(result)

print("¡Ejecución finalizada!\nResultados:")

# ----------------------------------------------------------------------------------------------
# guarda los resultados en un archivo CSV
with open("no-informada-results.csv", mode="w", newline="") as file:
    fieldnames = ["agent_name", "run_number", "states_explored", "solution_found", "path_cost"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

agent_names = set(result["agent_name"] for result in results)

# ----------------------------------------------------------------------------------------------
# calculo de la media y desviación estándar....
for agent_name in agent_names:
    # de los states explored...
    states_filtered_results = [result["states_explored"] for result in results if result["agent_name"] == agent_name]
    states_average = mean(states_filtered_results)
    states_std_deviation = stdev(states_filtered_results)

    print(f"Agente: {agent_name}")
    print(f"Estados explorados en promedio: {states_average}")
    print(f"Desviación estándar: {states_std_deviation}")

    # y del path cost (costo de la solución)
    path_cost_filtered_results = [result["path_cost"] for result in results if
                                  result["agent_name"] == agent_name and result["path_cost"] is not None]
    path_cost_average = mean(path_cost_filtered_results)
    path_cost_std_deviation = stdev(path_cost_filtered_results)
    print(f"Costo de la solución en promedio: {path_cost_average}")
    print(f"Desviación estándar: {path_cost_std_deviation}")

    print()

# ----------------------------------------------------------------------------------------------
# gráficos de cajas y bigotes

df = pd.read_csv("no-informada-results.csv")  # carga los datos desde el archivo CSV

# *** states ***
states_data = []  # crea una lista con los datos de los estados explorados por cada agente

for agent in agents:
    data = df[df['agent_name'] == agent.__name__]['states_explored'].tolist()
    states_data.append(data)

# crea un gráfico de cajas y bigotes
plt.figure(figsize=(10, 6))
plt.title("Estados Explorados por Agente")
plt.xlabel("Agente")
plt.ylabel("Estados Explorados")

# usa boxplot para visualizar los datos
plt.boxplot(states_data)
plt.xticks(range(1, len(agents) + 1), [agent.__name__ for agent in agents])

plt.savefig("states_explored.png")  # guarda el gráfico en un archivo
plt.show()

# *** path_cost ***
path_cost_data = []  # crea una lista de listas de datos de path_cost, una lista por cada agente

for agent in agents:
    data = df[df['agent_name'] == agent.__name__]['path_cost'].tolist()
    data = [x for x in data if x is not None]  # Elimina valores atípicos
    path_cost_data.append(data)

# crea un gráfico de cajas y bigotes para path_cost
plt.figure(figsize=(10, 6))
plt.title("Costo de la Solución por Agente")
plt.xlabel("Agente")
plt.ylabel("Costo de la Solución (path_cost)")

# usa boxplot para visualizar los datos
plt.boxplot(path_cost_data)
plt.xticks(range(1, len(agents) + 1), [agent.__name__ for agent in agents])

plt.savefig("path_cost.png")  # guarda el gráfico en un archivo
plt.show()  # muestra el gráfico

# ----------------------------------------------------------------------------------------------
print("Gráficos de los entornos generados:")
for i, env in enumerate(environments):
    print(f"Entorno {i + 1}:")
    env.plot_environment_util()
    plt.savefig(f"entorno_{i + 1}.png")  # guarda el gráfico en un archivo
    plt.show()
