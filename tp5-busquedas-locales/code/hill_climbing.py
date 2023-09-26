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

def hill_climbing(problem):
    current = problem.state
    current_value = problem.get_value(current)
    evaluations = 1000
    while evaluations > 0:
        neighbor = problem.get_best_successor(current)
        neighbor_value = problem.get_value(neighbor)
        if neighbor_value <= current_value:
            if problem.goal_test(current_value):
                print("Solución encontrada.")
            else:
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

# from n_queens_problem import NQueenProblem
# p = NQueensProblem(8)
# s, v, e = hill_climbing(p)
# p.print_board(s)
# print(p.ideal_value, v, p.heuristic_cost(s))
