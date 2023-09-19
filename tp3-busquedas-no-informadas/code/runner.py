# CON IDS

# Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

# Considerar lo siguiente:

# 1. El entorno del agente está compuesto por una grilla de 100x100 en donde los obstáculos se generan al azar. Se
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
# resultados en un gráfico de cajas y bigotes o boxplot.

# Dentro tp3-busquedas-no-informadas crear un archivo de nombre no-informada-results.csv en formato csv (comma
# separated values) con los resultados de las 30 ejecuciones para cada uno de los algoritmos evaluados. El formato
# deberá ser el siguiente: agent_name, run_n, estate_n, solution_found

from environment import Environment

import csv
from statistics import mean, stdev
import pandas as pd
import matplotlib.pyplot as plt


# define una función para ejecutar un algoritmo y registrar los resultados
def run_algorithm(agent, env: Environment, run_number: int, limit: int):
    agent_name = agent.__name__
    agent_instance = agent(env)
    if agent_name == "DLSAgent":
        result = agent_instance.search(limit)
    else:
        result = agent_instance.search()  # ejecuta el algoritmo
    states_explored = agent_instance.states_explored
    sol_founded = False
    path_cost = None
    if result is not None:
        sol_founded = True
        path_cost = result.path_cost
    return {"agent_name": agent_name, "run_number": run_number, "states_explored": states_explored,
            "solution_found": sol_founded, "path_cost": path_cost}


# ----------------------------------------------------------------------------------------------
# guarda los resultados en un archivo CSV
def save_to_csv(results: list):
    with open("no-informada-results.csv", mode="w", newline="") as file:
        fieldnames = ["agent_name", "run_number", "states_explored", "solution_found", "path_cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    agent_names = set(result["agent_name"] for result in results)
    return agent_names


# ----------------------------------------------------------------------------------------------
# calculo de la media y desviación estándar...
def calculate_mean_and_stdev(agent_names: set, results: list):
    for agent_name in agent_names:
        # de los states explored...
        states_filtered_results = [result["states_explored"] for result in results
                                   if result["agent_name"] == agent_name]
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
def boxplot_plotter(agents_bp: list):
    df = pd.read_csv("no-informada-results.csv")  # carga los datos desde el archivo CSV

    # *** states ***
    states_data = []  # crea una lista con los datos de los estados explorados por cada agente

    for agent in agents_bp:
        data = df[df['agent_name'] == agent.__name__]['states_explored'].tolist()
        states_data.append(data)

    # crea un gráfico de cajas y bigotes
    plt.figure(figsize=(10, 6))
    plt.title("Estados Explorados por Agente")
    plt.xlabel("Agente")
    plt.ylabel("Estados Explorados")
    # usa boxplot para visualizar los datos
    plt.boxplot(states_data)
    plt.xticks(range(1, len(agents_bp) + 1), [agent.__name__ for agent in agents_bp])
    plt.savefig("states_explored.png")  # guarda el gráfico en un archivo
    plt.show()

    # *** path_cost ***
    path_cost_data = []  # crea una lista de listas de datos de path_cost, una lista por cada agente

    for agent in agents_bp:
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
    plt.xticks(range(1, len(agents_bp) + 1), [agent.__name__ for agent in agents_bp])
    plt.savefig("path_cost.png")  # guarda el gráfico en un archivo
    plt.show()  # muestra el gráfico


# ----------------------------------------------------------------------------------------------
def calculate_solution_percentage(agent_names: set, results: list, num_runs: int):
    percentages = []
    agent_names_list = list(agent_names)  # Convierte el conjunto en una lista
    for agent_name in agent_names_list:
        sol_found_results = [result["solution_found"] for result in results
                             if result["agent_name"] == agent_name and result["solution_found"]]
        sol_percentage = (len(sol_found_results) / num_runs) * 100
        percentages.append(sol_percentage)
        print(f"Porcentaje de veces que {agent_name} encontró la solución: {sol_percentage:.2f}%")

    plt.figure(figsize=(10, 6))
    plt.bar(agent_names_list, percentages)
    plt.xlabel("Algoritmo de Búsqueda")
    plt.ylabel("Porcentaje de Soluciones Encontradas (%)")
    plt.title("Porcentaje de Soluciones Encontradas por Algoritmo")
    plt.ylim(0, 100)  # ajusta el rango del eje y de 0 a 100
    plt.xticks(rotation=45)  # rota las etiquetas del eje x para una mejor legibilidad
    plt.tight_layout()
    plt.savefig("solution_percentage.png")  # guarda el gráfico en un archivo
    plt.show()

# ----------------------------------------------------------------------------------------------
def env_plotter(environments: list):
    print("Gráficos de los entornos generados:")
    for i, env in enumerate(environments):
        print(f"Entorno {i + 1}:")
        env.plot_environment_util()
        plt.savefig(f"entorno_{i + 1}.png")  # guarda el gráfico en un archivo
        plt.show()


# ----------------------------------------------------------------------------------------------
def runner(agents_list: list, env_size: int, env_obstacle_prob: float, limit: int, num_runs: int):
    results = []
    environments = []

    print("Ejecutando algoritmos...")
    for run_number in range(1, num_runs + 1):
        print(f"Run number: {run_number}")
        env = Environment(env_size, env_obstacle_prob) # crea un entorno
        environments.append(env)
        for agent in agents_list:
            result = run_algorithm(agent, env, run_number, limit)
            results.append(result)

    print("¡Ejecución finalizada!\nResultados:")

    agent_names = save_to_csv(results)
    calculate_mean_and_stdev(agent_names, results)
    boxplot_plotter(agents_list)
    calculate_solution_percentage(agent_names, results, num_runs)
    env_plotter(environments)
