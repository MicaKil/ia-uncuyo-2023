# ## Ejercicio 6
# 1. Implementar una solución al problema de las n-reinas utilizando una formulación CSP.
# 2. Implementar una solución utilizando backtracking.
# 3. Implementar una solución utilizando encadenamiento hacia adelante.
# 4. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.
# 5. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8,
# 10, 12 y 15 reinas.
# 6. Realizar un gráfico de cajas para los puntos 4 y 5.

from queue import Queue
from n_queens_problem import NQueensProblem


class Variable:
    def __init__(self, domain, index):
        self.value = None
        self.domain = domain
        self.index = index

    def __str__(self):
        return str(f"Variable: {self.index}, value: {self.value}, domain: {self.domain}")

    def __repr__(self):  # para que se imprima bien en las listas
        return str(f"Variable: {self.index}, value: {self.value}, domain: {self.domain}")


class NQueensCSP(NQueensProblem):
    def __init__(self, size: int):
        self.size = size
        self.domain = list(range(size))
        self.variables = [Variable(self.domain, i) for i in range(size)]

    def __str__(self):
        return str(f"Variables: {self.variables}")

    # nconflicts devuelve la cantidad de conflictos que tiene una variable con un valor dado
    def nconflicts(self, var, value, assignment):
        conflicts = 0
        len_assignment = len(assignment)
        # print(f"     x: (i {var.index}, v {value})")
        # print(f"     assignment: {assignment}, len_assignment: {len_assignment}")
        for i in range(len_assignment):
            cur_var = assignment[i]
            if self.check_row(value, cur_var.value):
                conflicts += 1
            if self.check_diagonal(var, cur_var, value, cur_var.value):
                conflicts += 1
        # state = [None] * self.size
        # state[var.index] = value
        # for i in assignment:
        #     state[i.index] = i.value
        # self.print_board(state)
        # print(f"     conflicts: {conflicts}")
        return conflicts

    # is_consistent devuelve True si el valor de la variable no genera conflictos con los valores de las variables
    # asignadas anteriormente
    def is_consistent(self, var, value, assignment):
        return self.nconflicts(var, value, assignment) == 0

    def is_complete(self, assignment):
        return len(assignment) == self.size

    def constraints(self, xi, xj, x, y):
        #print(f"     y: (i {xj.index}, v {y})")
        state = [None] * self.size
        state[xi.index] = x
        state[xj.index] = y
        #self.print_board(state)
        #print(f"x==y: {x == y}, diag: {abs(x - y) == xi.index - xj.index}, not: {not (x == y or abs(x - y) == xi.index - xj.index)}")
        if self.check_row(x, y) or self.check_diagonal(xi, xj, x, y):
            return False
        return True


    def check_row(self, x, y):
        return x == y


    def check_diagonal(self, xi, xj, x, y):
        return abs(x - y) == xi.index - xj.index


    def gen_arcs(self):
        arcs = Queue()
        for xi in self.variables:
            for xj in self.variables:
                if xi != xj:
                    arcs.put((xi, xj))
        return arcs

    def get_unassigned_neighbors(self, xi):
        neighbors = set()
        for xj in self.variables:
            if xj != xi and xj.value is None:
                neighbors.add(xj)
        return neighbors


#-----------------------------------------------------------------------------------------------------------------------

