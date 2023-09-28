import random
from functools import partial


def tournament_selection(fitness_fn, population: list, k=10):
    # se seleccionan k individuos de la población al azar
    selected = random.sample(population, k)
    # se ordenan los individuos de mayor a menor según su valor/fitness
    sorted_selection = sorted(selected, key=lambda x: -fitness_fn(x))
    return sorted_selection[:2]  # los 2 mejores individuos del torneo son seleccionados para reproducción


def roulette_selection(fitness_fn, population: list):
    # se calcula la probabilidad de selección de cada individuo
    fitness = [fitness_fn(state) for state in population]
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    # se seleccionan 2 individuos distintos al azar
    while True:
        selected = random.choices(population, weights=probabilities, k=2)
        if selected[0] != selected[1]:
            break
    return selected


def select(fitness_fn, population, selection_type=tournament_selection, k=10):
    if selection_type == tournament_selection:
        return tournament_selection(fitness_fn, population, k)
    elif selection_type == roulette_selection:
        return roulette_selection(fitness_fn, population)
    else:
        raise ValueError("Invalid selection type")


#  retorna una función parcializada con el tipo de selección y el valor de k
def set_selection_type(selection_type=tournament_selection, k=10):
    return partial(select, selection_type=selection_type, k=k)


# from n_queens_problem import NQueensProblem
# from genetic import *
#
# prob = NQueensProblem(8)
# pop = gen_population(prob, 50)
# sel = select(set_fitness_fn(prob), pop)
# print(sel)
#
# from culling import cull
# c = cull(pop, [], set_fitness_fn(prob))
# print(c)
