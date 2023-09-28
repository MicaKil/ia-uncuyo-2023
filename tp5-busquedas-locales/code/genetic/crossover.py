from random import randint
from functools import partial


# se elige un punto de corte al azar y se intercambian los genes de los padres
def point_crossover(parent1, parent2):
    child1 = []
    child2 = []
    len_parent = len(parent1)
    n = randint(1, len_parent - 2)
    for i in range(n):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(n, len_parent):
        child1.append(parent2[i])
        child2.append(parent1[i])
    return child1, child2


# Order Crossover (OX)
# Procedure: OX
# 1. Select a substring from a parent at random.
# 2. Produce a proto-child by copying the substring into the corresponding position of it.
# 3. Delete the digits which are already in the substring from the 2nd parent. The resulted sequence of digits
# contains the digits that the proto-child needs.
# 4. Place the digits into the unfixed positions of the proto-child from left to right according to the order of the
# sequence to produce an offspring.


def order_crossover(parent1, parent2):
    # 1. Select a substring from a parent at random.
    len_parent = len(parent1)
    n1 = randint(0, len_parent - 2)
    n2 = n1 + randint(1, len_parent - n1 - 1) + 1
    # 2. Produce a proto-child by copying the substring into the corresponding position of it.
    child1 = [None] * len_parent
    child2 = [None] * len_parent

    child1[n1:n2] = parent1[n1:n2]
    child2[n1:n2] = parent2[n1:n2]
    # 3. Delete the digits which are already in the substring from the 2nd parent. The resulted sequence of digits
    # contains the digits that the proto-child needs.
    digits1 = [digit for digit in parent2 if digit not in child1]
    digits2 = [digit for digit in parent1 if digit not in child2]

    # 4. Place the digits into the unfixed positions of the proto-child from left to right according to the order of the
    # sequence to produce an offspring.
    i = 0
    k = 0
    len_digits1 = len(digits1)
    len_digits2 = len(digits2)
    for j in range(len_parent):
        if child1[j] is None:
            if i >= len_digits1:  # si ya no quedan más dígitos por agregar de digits1, se agregan los del padre 1
                child1[j] = parent1[j]
            else:
                child1[j] = digits1[i]
                i += 1
        if child2[j] is None:
            if k >= len_digits2:  # si ya no quedan más dígitos por agregar de digits2, se agregan los del padre 2
                child2[j] = parent2[j]
            else:
                child2[j] = digits2[k]
                k += 1

    return child1, child2


def crossover(paren1, parent2, crossover_type=order_crossover):
    return crossover_type(paren1, parent2)


# retorna una función parcializada con el tipo de crossover
def set_crossover_type(crossover_type=order_crossover):
    return partial(crossover, crossover_type=crossover_type)


# from n_queens_problem import NQueensProblem
# from genetic import gen_population
#
# prob = NQueensProblem(8)
# pop = gen_population(prob, 2)
# print(pop)
# c_fn = set_crossover_type(order_crossover)
# c = c_fn(pop[0], pop[1])
# print(c)
