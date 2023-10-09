# ## Ejercicio 6
# 1. Implementar una solución al problema de las n-reinas utilizando una formulación CSP.
# 2. Implementar una solución utilizando backtracking.
# 3. Implementar una solución utilizando encadenamiento hacia adelante.
# 4. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.
# 5. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8,
# 10, 12 y 15 reinas.
# 6. Realizar un gráfico de cajas para los puntos 4 y 5.

class Variable:
    def __init__(self, domain, index):
        self.value = None
        self.domain = domain
        self.index = index

    def __str__(self):
        return str(f"Variable: {self.index}, value: {self.value}, domain: {self.domain}")

    def __repr__(self):  # para que se imprima bien en las listas
        return str(f"Variable: {self.index}, value: {self.value}, domain: {self.domain}")


class NQueensCSP:
    def __init__(self, size: int):
        self.size = size
        self.domain = list(range(size))
        self.variables = [Variable(self.domain, i) for i in range(size)]
        self.state = [self.variables[i].value for i in range(size)]

    def __str__(self):
        return str(f"State: {self.state}, Variables: {self.variables}")

    # nconflicts devuelve la cantidad de conflictos que tiene una variable con un valor dado
    def nconflicts(self, var, value, assignment):
        conflicts = 0
        len_assignment = len(assignment)
        for i in range(len_assignment):
            if assignment[i].value == value:
                conflicts += 1
            if abs(assignment[i].value - value) == assignment[i].index - var.index:
                conflicts += 1
        return conflicts

    # is_consistent devuelve True si el valor de la variable no genera conflictos con los valores de las variables
    # asignadas anteriormente
    def is_consistent(self, var, value, assignment):
        if self.nconflicts(var, value, assignment) == 0:
            return True
        return False

    def is_complete(self, assignment):
        if len(assignment) == self.size:
            return True
        return False

    def constraints(self, xi, xj, x, y):
        if x == y:
            return False
        if abs(x - y) == xi.index - xj.index:
            return False
        return True
# p = NQueensCSP(4)
# print(p)
