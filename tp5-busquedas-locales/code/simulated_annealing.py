# 1. El algoritmo deberá ser capaz de encontrar solamente una solución para tableros de diferentes tamaños.
# 2. Una posible estructura para representar el tablero consiste en un arreglo de tamaño N, donde en cada posición hace
# referencia a una columna de tablero. Y cada valor hace referencia a una fila.
# 3. Se define una función objetivo H(e) la cual contabiliza la cantidad de pares de reinas amenazadas para un tablero
# e.
# 4. Se deberá definir una variable que establezca el número máximo de estados que podrán ser evaluados.
# 5. El programa deberá devolver el tablero solución (únicamente la estructura que representa el tablero). Junto a la
# cantidad de estados que tuvo que recorrer el algoritmo para llegar a la solución. En caso de alcanzar el máximo de
# estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H.
# 6. Replicar el punto 5 para los casos de las 4,8,10 reinas

# B) Implementar el algoritmo Simulated Annealing para resolver el problema del punto A.

# function SIMULATED-ANNEALING(problem, schedule) returns a solution state
# inputs: problem, a problem
#         schedule , a mapping from time to “temperature”
# current ← MAKE-NODE(problem.INITIAL-STATE)
# for t = 1 to ∞ do
#   T ← schedule(t)
#   if T = 0 then return current
#   next ← a randomly selected successor of current
#   ΔE ← next.VALUE – current.VALUE
#   if ΔE > 0 then current ← next
#   else current ← next only with probability e^(ΔE/T)


import math
import random
from utils import print_sol, plot_heuristic_fn


# The schedule input determines the value of the temperature T as a function of time.
def schedule(max_evaluations, t):
    return max_evaluations - t


def simulated_annealing(problem, max_evaluations=1000, verbose=False, plot_heuristic=False):
    current = problem.state
    current_value = problem.get_value(current)
    t = 0
    if plot_heuristic:
        h_values = []
    while t <= max_evaluations:
        T = schedule(max_evaluations, t)  # t = 1000 - evaluations -> T = schedule(t)
        if plot_heuristic:
            h_values.append(problem.heuristic_cost(current))
        if T == 0 or problem.goal_test(current_value):
            if verbose:
                print_sol(problem, current, current_value, t, max_evaluations)
            if plot_heuristic:
                plot_heuristic_fn(h_values, "simulated_annealing")
            return current, abs(current_value), t
        successor = problem.get_best_successor(current)  # next ← a randomly selected successor of current
        successor_value = problem.get_value(successor)
        delta_E = successor_value - current_value
        if delta_E > 0:
            current = successor
            current_value = successor_value
        else:  # current ← next only with probability e^(ΔE/T)
            probability = math.exp(delta_E / T)
            if probability > random.random():
                current = successor
                current_value = successor_value
        t += 1
    # nunca debería llegar acá
    if verbose:
        print_sol(problem, current, current_value, t, max_evaluations)
    if plot_heuristic:
        plot_heuristic_fn(h_values, "simulated_annealing")
    return current, abs(current_value), t

# from n_queens_problem import NQueensProblem
# p = NQueensProblem(10)
# simulated_annealing(p, verbose=True, plot_heuristic=True)
