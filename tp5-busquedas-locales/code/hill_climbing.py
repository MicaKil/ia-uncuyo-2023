# A) Implementar un algoritmo de Hill Climbing (versión canónica) para resolver el problema de las n-reinas.
#
# El algoritmo deberá ser capaz de encontrar solamente una solución para tableros de diferentes tamaños.
# Una posible estructura para representar el tablero consiste en un arreglo de tamaño N, donde en cada posición hace
# referencia a una columna de tablero. Y cada valor hace referencia a una fila.
#
# Se define una función objetivo H(e) la cual contabiliza la cantidad de pares de reinas amenazadas para un tablero e.
#
# Se deberá definir una variable que establezca el número máximo de estados que podrán ser evaluados.
#
# El programa deberá devolver el tablero solución (únicamente la estructura que representa el tablero). Junto a la
# cantidad de estados que tuvo que recorrer el algoritmo para llegar a la solución. En caso de alcanzar el máximo de
# estados evaluados, devolver la mejor solución encontrada y el valor correspondiente de la función H.
#
# Replicar el punto 5 para los casos de las 4,8,10 reinas

# function HILL-CLIMBING(problem) returns a state that is a local maximum
#   current ←MAKE-NODE(problem.INITIAL-STATE)
#   loop do
#       neighbor ←a highest-valued successor of current
#       if neighbor.VALUE ≤ current.VALUE then return current.STATE
#       current←neighbor

from n_queens_problem import NQueenProblem


def hill_climbing(problem):
    current = problem.state
    current_value = problem.get_value(current)
    evaluations = 1000
    while evaluations > 0:
        neighbor = problem.get_best_successor(current)
        neighbor_value = problem.get_value(neighbor)
        if neighbor_value <= current_value:
            print("Máximo local alcanzado.")
            print(f"Estado: {current}, \nValor: {abs(current_value)}, "
                  f"\nEstados Evaluados: {1000 - evaluations}")
            return current, abs(current_value), 1000 - evaluations
        current = neighbor
        current_value = neighbor_value
        evaluations -= 1
    print("Máximo local no alcanzado.")
    print(f"Estado: {current}, \nValor: {abs(current_value)}, \nEstados Evaluados: {1000 - evaluations}")
    return current, abs(current_value), 1000 - evaluations


p = NQueenProblem(8, None)
hill_climbing(p)

# print n queens board
def print_board(board):
    for row in board:
        print(row)

# B) Implementar el algoritmo Simulated Annealing para resolver el problema del punto A.
#
# C) Implementar un algoritmo genético para resolver el problema del punto A. Además de la implementación en código del
# mismo, se deberán incluir detalles respecto a
# 1. Definición de los individuos de la población
# 2. Estrategia de selección
# 3. Estrategia de reemplazo
# 4. Operadores.
