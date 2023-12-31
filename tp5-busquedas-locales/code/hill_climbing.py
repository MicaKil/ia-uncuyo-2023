# A) Implementar un algoritmo de Hill Climbing (versión canónica) para resolver el problema de las n-reinas.
#
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

# function HILL-CLIMBING(problem) returns a state that is a local maximum
#   current ←MAKE-NODE(problem.INITIAL-STATE)
#   loop do
#       neighbor ←a highest-valued successor of current
#       if neighbor.VALUE ≤ current.VALUE then return current.STATE
#       current←neighbor

from utils import print_sol, plot_heuristic_fn


def hill_climbing(problem, max_evaluations=1000, verbose=False, plot_heuristic=False):
    current = problem.state
    current_value = problem.get_value(current)
    evaluations = 0
    if plot_heuristic:
        h_values = [problem.heuristic_cost(current)]
    while evaluations < max_evaluations:
        neighbor = problem.get_best_successor(current)
        neighbor_value = problem.get_value(neighbor)
        if plot_heuristic:
            h_values.append(problem.heuristic_cost(neighbor))
        if neighbor_value <= current_value:
            if verbose:
                print_sol(problem, current, current_value, evaluations, max_evaluations)
            if plot_heuristic:
                plot_heuristic_fn(h_values, "hill_climbing")
            return current, abs(current_value), evaluations
        current = neighbor
        current_value = neighbor_value
        evaluations += 1
    if verbose:
        print_sol(problem, current, current_value, evaluations, max_evaluations)
    if plot_heuristic:
        plot_heuristic_fn(h_values, "hill_climbing")
    return current, abs(current_value), evaluations


# from n_queens_problem import NQueensProblem
# p = NQueensProblem(10)
# hill_climbing(p, verbose=True, plot_heuristic=True)
