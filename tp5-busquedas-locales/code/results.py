### Ejercicio A
# Ejecutar cada uno de los algoritmos implementados en la parte I 30 veces y calcular para el caso de 4, 8,10,(12,15)?
# reinas:
# 1. El número (porcentaje) de veces que se llega a un estado de solución óptimo.
# 2. El tiempo de ejecución promedio y la desviación estándar para encontrar dicha solución. (se puede usar la func
# time.time() de python)
# 3. La cantidad de estados previos promedio y su desviación estándar por los que tuvo que pasar para llegar a una
# solución.
# 4. Generar un tabla con los resultados para cada uno de los algoritmos desarrollados y guardarla en formato .csv
# 5. Realizar un gráfico de cajas (boxplot) que muestre la distribución de los tiempos de ejecución de cada algoritmo.

from n_queens_problem import NQueensProblem
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
from genetic import genetic
import time
import statistics
import csv


# Define una función para ejecutar un algoritmo y calcular métricas
def run_algorithm(algorithm, n, num_executions):
    success_count = 0
    execution_times = []
    states_explored = []

    for _ in range(num_executions):
        problem = NQueensProblem(n)
        start_time = time.time()
        result, _, explored_states = algorithm(problem)
        end_time = time.time()
        execution_times.append(end_time - start_time)
        states_explored.append(explored_states)

        if problem.goal_test(problem.get_value(result)):
            success_count += 1

    success_percentage = (success_count / num_executions) * 100
    avg_execution_time = statistics.mean(execution_times)
    std_execution_time = statistics.stdev(execution_times)
    avg_states_explored = statistics.mean(states_explored)
    std_states_explored = statistics.stdev(states_explored)

    return success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored

# Tamaños de tablero (n) para probar
board_sizes = [4, 8, 10, 12, 15]

# Número de ejecuciones por algoritmo
num_executions = 30

# Algoritmos a ejecutar
algorithms = [hill_climbing, simulated_annealing, genetic]  # Agrega los algoritmos que deseas probar

# Resultados
results = []

for n in board_sizes:
    for algorithm in algorithms:
        success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored = run_algorithm(algorithm, n, num_executions)
        results.append([n, algorithm.__name__, success_percentage, avg_execution_time, std_execution_time, avg_states_explored, std_states_explored])

# Guardar los resultados en un archivo CSV
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['Board Size', 'Algorithm', 'Success Percentage', 'Avg Execution Time', 'Std Execution Time', 'Avg States Explored', 'Std States Explored']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow({'Board Size': result[0], 'Algorithm': result[1], 'Success Percentage': result[2], 'Avg Execution Time': result[3], 'Std Execution Time': result[4], 'Avg States Explored': result[5], 'Std States Explored': result[6]})
