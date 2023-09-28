from random import randint
from functools import partial


def randint_except(lower, upper, except_):
    while True:
        n = randint(lower, upper)
        if n != except_:
            return n


def random_swap(individual):
    len_individual = len(individual)
    i = randint(0, len_individual - 1)
    j = randint_except(0, len_individual - 1, i)
    individual[i], individual[j] = individual[j], individual[i]

    return individual


def random_mutation(individual):
    len_individual = len(individual)
    pos = randint(0, len_individual - 1)
    individual[pos] = randint(0, len_individual - 1)
    return individual


def mutate(individual, mutation_type=random_swap):
    return mutation_type(individual)


# retorna una función parcializada con el tipo de mutación
def set_mutation_type(mutation_type=random_swap):
    return partial(mutate, mutation_type=mutation_type)


# from n_queens_problem import NQueensProblem
# from genetic import gen_population
# from selection import select
# from crossover import crossover

# prob = NQueensProblem(8)
# pop = gen_population(prob, 1)
# print(pop)
# mutate_fn = set_mutation_type(random_swap)
# m = mutate_fn(pop[0])
# print(m)
