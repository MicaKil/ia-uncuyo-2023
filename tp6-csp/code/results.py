# ## Ejercicio 6
# 1. Implementar una solución al problema de las n-reinas utilizando una formulación CSP.
# 2. Implementar una solución utilizando backtracking.
# 3. Implementar una solución utilizando encadenamiento hacia adelante.
# 4. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.
# 5. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8,
# 10, 12 y 15 reinas.
# 6. Realizar un gráfico de cajas para los puntos 4 y 5.

from n_queens_CSP import NQueensCSP
from backtracking_search import backtracking_search
from inference import mac, forward_checking
import time
import statistics
import csv
import matplotlib.pyplot as plt
from copy import deepcopy


def calculate_statistics(execution_times, states_explored):
    # tiempo de ejecución promedio y la desviación estándar para encontrar dicha solución.
    avg_execution_time = statistics.mean(execution_times)
    std_execution_time = statistics.stdev(execution_times)
    # cantidad de estados previos promedio y su desviación estándar
    avg_states_explored = statistics.mean(states_explored)
    std_states_explored = statistics.stdev(states_explored)

    return avg_execution_time, std_execution_time, avg_states_explored, std_states_explored


def run_algorithm(inference_type, num_executions, problem):
    execution_times = []
    explored_states = []

    for i in range(num_executions):
        problem_copy = deepcopy(problem)
        print(f"        Ejecución {i + 1} de {num_executions} ...")
        start_time = time.time()
        solution, states = backtracking_search(problem_copy, inference_type)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        explored_states.append(states)

    return calculate_statistics(execution_times, explored_states)


def save_results(results):
    with open('../results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Board Size', 'Algorithm', 'Avg Execution Time', 'Std Execution Time',
                      'Avg States Explored', 'Std States Explored']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({'Board Size': result[0], 'Algorithm': result[1], 'Avg Execution Time': result[2],
                             'Std Execution Time': result[3], 'Avg States Explored': result[4],
                             'Std States Explored': result[5]})


def plot_boxplot(results):
    inference_types = ['mac', 'forward_checking']
    execution_times = {alg: [] for alg in inference_types}
    states_explored = {alg: [] for alg in inference_types}

    for result in results:
        execution_times[result[1]].append(result[2])
        states_explored[result[1]].append(result[4])

    times_data = [execution_times[alg] for alg in inference_types]
    states_data = [states_explored[alg] for alg in inference_types]

    plt.figure(figsize=(10, 6))
    plt.boxplot(times_data, labels=inference_types)
    plt.title("Tiempos de Ejecución Promedio por Algoritmo")
    plt.ylabel("Tiempo de Ejecución (s)")
    plt.xlabel("Algoritmos")
    plt.grid(True)
    plt.savefig("times.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.boxplot(states_data, labels=inference_types)
    plt.title("Estados Explorados Promedio por Algoritmo")
    plt.ylabel("Estados Explorados")
    plt.xlabel("Algoritmos")
    plt.grid(True)
    plt.savefig("states.png")
    plt.show()


def runner(num_executions, board_sizes):
    inference_types = [mac, forward_checking]
    results = []

    for board_size in board_sizes:
        print(f"Board size: {board_size}")
        problem = NQueensCSP(board_size)
        for inference_type in inference_types:
            print(f"    Algoritmo: {inference_type.__name__}")
            avg_execution_time, std_execution_time, avg_states_explored, std_states_explored = (
                run_algorithm(inference_type, num_executions, problem))
            results.append((board_size, inference_type.__name__, avg_execution_time, std_execution_time,
                            avg_states_explored, std_states_explored))

    save_results(results)
    plot_boxplot(results)
    return results


#-----------------------------------------------------------------------------------------------------------------------
num_executions = 30
board_sizes = [4, 8, 10, 12]

runner(num_executions, board_sizes)
