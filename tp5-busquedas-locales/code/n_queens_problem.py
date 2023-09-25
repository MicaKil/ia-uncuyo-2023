# A) Implementar un algoritmo de x para resolver el problema de las n-reinas.
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

from random import randint


class NQueenProblem:
    def __init__(self, n: int, state):
        self.size = n
        if state is None:
            self.state = [0] * n  # inicializa el tablero con todas las reinas en la fila 0
        else:
            self.state = state
        self.threats = self.heuristic_cost(self.state)

    def __str__(self):
        return str(f"state: {self.state}, threats: {self.threats}")

    def heuristic_cost(self, state):  # devuelve la cantidad de pares de reinas amenazadas
        h = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                # chequea si hay reinas en la misma fila o en la misma diagonal
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    h += 1
        return h

    #The successors of a state are all possible states
    # generated by moving a single queen to another square in the same column (so each state has
    # 8×7=56 successors)
    def gen_successor(self, state):
        #asumimos que el estado actual es el mejor
        best_successors = [state]  # contiene a los posibles sucesores
        lowest_threats = self.heuristic_cost(state)  # cantidad de pares de reinas amenazadas
        n = self.size
        for i in range(n):
            for j in range(n):
                if state[i] != j:
                    new_state = state.copy()
                    new_state[i] = j
                    new_threats = self.heuristic_cost(new_state)
                    if new_threats < lowest_threats:  # si el nuevo sucesor es mejor que el mejor sucesor
                        lowest_threats = new_threats
                        best_successors = [new_state]  # reinicializa la lista de mejores sucesores
                    elif new_threats == lowest_threats:
                        best_successors.append(new_state)

        return best_successors

    def get_best_successor(self, state):  # devuelve un sucesor al azar
        best_successors = self.gen_successor(state)
        return best_successors[randint(0, len(best_successors) - 1)]

    def get_value(self, state):
        return -self.heuristic_cost(state)  # el negativo pq hill climbing busca el máximo

    def goal_test(self, threats):
        return threats == 0

    def print_board(self, state):
        board = []
        for i in range(self.size):
            board.append(["-"] * self.size)
        for i in range(self.size):
            board[state[i]][i] = "Q"
        for row in board:
            print(" ".join(row))