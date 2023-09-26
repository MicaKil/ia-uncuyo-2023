import random


def tournament_selection(problem, population: set, k=10):
    print(k)
    # se seleccionan k individuos de la población al azar
    population = list(population)
    selected = random.sample(population, k)
    # se ordenan los individuos de menor a mayor según su valor/fitness
    sorted_ = sorted(selected, key=lambda x: problem.get_value(x))
    return sorted_[:2]  # los 2 mejores individuos del torneo son seleccionados para reproducción


def roulette_selection(problem, population: set):
    population = list(population)
    # se calcula la probabilidad de selección de cada individuo
    fitness = [problem.get_value(state) for state in population]
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    # se seleccionan 2 individuos al azar
    selected = random.choices(population, weights=probabilities, k=2)
    return selected


def select(problem, population, selection_type=tournament_selection, k=10):
    if selection_type == tournament_selection:
        return tournament_selection(problem, population, k)
    elif selection_type == roulette_selection:
        return roulette_selection(problem, population)
    else:
        raise ValueError("Invalid selection type")


# from n_queens_problem import NQueensProblem
# prob = NQueensProblem(8)
# pop = gen_population(100, prob)
# sel = select(prob, pop, k=20)
# print(sel)
