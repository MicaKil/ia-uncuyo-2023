# Ejercicio A
# Ejecutar cada uno de los algoritmos implementados en la parte I 30 veces y calcular para el caso de 4, 8,10,(12,15)
# reinas:
# 1. El número (porcentaje) de veces que se llega a un estado de solución óptimo.
# 2. El tiempo de ejecución promedio y la desviación estándar para encontrar dicha solución.
# 3. La cantidad de estados previos promedio y su desviación estándar por los que tuvo que pasar para llegar a una
# solución.
# 4. Generar una tabla con los resultados para cada uno de los algoritmos desarrollados y guardarla en formato .csv
# 5. Realizar un gráfico de cajas (boxplot) que muestre la distribución de los tiempos de ejecución de cada algoritmo.

from n_queens_problem import NQueensProblem
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
import genetic.genetic as genetic
import genetic.selection as selection
import genetic.crossover as crossover
import genetic.mutation as mutation
import genetic.culling as culling
import time
import statistics
import csv
import matplotlib.pyplot as plt
import pandas as pd


def calculate_statistics(success_count, num_executions, execution_times, states_explored):
    # 1. El número (porcentaje) de veces que se llega a un estado de solución óptimo.
    success_percentage = (success_count / num_executions) * 100
    # 2. El tiempo de ejecución promedio y la desviación estándar para encontrar dicha solución.
    avg_execution_time = statistics.mean(execution_times)
    std_execution_time = statistics.stdev(execution_times)
    # 3. La cantidad de estados previos promedio y su desviación estándar
    avg_states_explored = statistics.mean(states_explored)
    std_states_explored = statistics.stdev(states_explored)

    return success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored


# define una función para ejecutar un algoritmo y calcular métricas
def run_algorithm(algorithm_name, num_executions, problem):
    success_count = 0
    execution_times = []
    states_explored = []

    for i in range(num_executions):
        print(f"        Ejecución {i + 1} de {num_executions} ...")
        start_time = time.time()
        best_state, value, explored_states = algorithm_name(problem)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        states_explored.append(explored_states)

        if problem.goal_test(value):
            success_count += 1

    return calculate_statistics(success_count, num_executions, execution_times, states_explored)


def run_genetic_algorithm(num_executions, population, problem, fitness_fn, select_fn, crossover_fn, mutate_fn,
                          cull_fn):
    success_count = 0
    execution_times = []
    states_explored = []

    for i in range(num_executions):
        print(f"        Ejecución {i + 1} de {num_executions} ...")
        start_time = time.time()
        best_state, value, explored_states = genetic.genetic(population, fitness_fn, problem, select_fn, crossover_fn,
                                                             mutate_fn, cull_fn)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        states_explored.append(explored_states)

        if problem.goal_test(value):
            success_count += 1

    return calculate_statistics(success_count, num_executions, execution_times, states_explored)


# guardar los resultados en un archivo CSV
def save_results(results):
    with open('../busquedas-locales-results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Board Size', 'Algorithm', 'Success Percentage', 'Avg Execution Time', 'Std Execution Time',
                      'Avg States Explored', 'Std States Explored']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({'Board Size': result[0], 'Algorithm': result[1], 'Success Percentage': result[2],
                             'Avg Execution Time': result[3], 'Std Execution Time': result[4],
                             'Avg States Explored': result[5], 'Std States Explored': result[6]})


def runner(num_executions, board_sizes):
    algorithms = [hill_climbing, simulated_annealing]
    results = []

    for n in board_sizes:
        print(f"Calculando para n = {n} ...")
        # problema a resolver
        problem = NQueensProblem(n)
        for algorithm in algorithms:
            print(f"    Calculando para {algorithm.__name__} ...")
            success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored \
                = run_algorithm(algorithm, num_executions, problem)
            results.append([n, algorithm.__name__, success_percentage, avg_execution_time, std_execution_time,
                            avg_states_explored, std_states_explored])
        # genetic stuff
        population_size = 10 * n
        population = genetic.gen_population(problem, population_size)
        select_fn = selection.set_selection_type(selection.tournament_selection, population_size // 4)
        crossover_fn = crossover.set_crossover_type(crossover.order_crossover)
        mutate_fn = mutation.set_mutation_type(mutation.random_swap)
        cull_fn = culling.set_cull_type(culling.elitism_cull)
        fitness_fn = genetic.set_fitness_fn(problem)

        print(f"    Calculando para genetic ...")
        success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored \
            = run_genetic_algorithm(num_executions, population, problem, fitness_fn, select_fn, crossover_fn, mutate_fn,
                                    cull_fn)
        results.append([n, 'genetic', success_percentage, avg_execution_time, std_execution_time, avg_states_explored,
                        std_states_explored])

    return results


def plot_boxplot(results):
    algorithms = ['hill_climbing', 'simulated_annealing', 'genetic']
    execution_times = {alg: [] for alg in algorithms}

    for result in results:
        _, algorithm, _, execution_time, _, _, _ = result
        execution_times[algorithm].append(execution_time)

    # crea una lista de tiempos de ejecución para cada algoritmo
    data = [execution_times[alg] for alg in algorithms]

    # crea el gráfico de cajas
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=algorithms)
    plt.title('Distribución de Tiempos de Ejecución por Algoritmo')
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.grid(True)
    plt.savefig(f"run_times.png")
    plt.show()


# Función para crear un gráfico de cajas desde un archivo CSV
def create_boxplot_from_csv(csv_filename):
    # lee los datos del archivo CSV en un DataFrame de pandas
    df = pd.read_csv(csv_filename)

    # selecciona las columnas relevantes para el gráfico de cajas
    algorithms = ['hill_climbing', 'simulated_annealing', 'genetic']
    data = {alg: df[df['Algorithm'] == alg]['Avg Execution Time'] for alg in algorithms}

    # crea el gráfico de cajas
    plt.figure(figsize=(10, 6))
    plt.boxplot(data.values(), labels=data.keys())
    plt.title('Distribución de Tiempos de Ejecución por Algoritmo')
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo de Ejecución Promedio (segundos)')
    plt.grid(True)

    plt.savefig(f"run_times2.png")
    plt.show()

    HC_SA = [data['hill_climbing'], data['simulated_annealing']]
    plt.figure(figsize=(10, 6))
    plt.boxplot(HC_SA, labels=['hill_climbing', 'simulated_annealing'])
    plt.title('Distribución de Tiempos de Ejecución por Algoritmo')
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo de Ejecución Promedio (segundos)')
    plt.grid(True)
    plt.savefig(f"run_times_HC_SA.png")
    plt.show()


def run(num_executions, board_sizes):
    results = runner(num_executions, board_sizes)
    save_results(results)
    plot_boxplot(results)


# tamaños de tablero (n) para probar
board_sizes_ = [4, 8, 10, 12]  # 15 -> mi pc se muere con 10

# número de ejecuciones por algoritmo
num_executions_ = 30

#run(num_executions_, board_sizes_)

#create_boxplot_from_csv('busquedas-locales-results.csv')
