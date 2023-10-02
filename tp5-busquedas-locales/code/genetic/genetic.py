# C) Implementar un algoritmo genético para resolver el problema del punto A. Además de la implementación en código del
# mismo, se deberán incluir detalles respecto a
# 1. Definición de los individuos de la población
# 2. Estrategia de selección
# 3. Estrategia de reemplazo
# 4. Operadores.

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

import random
from functools import partial
from utils import print_sol, plot_heuristic_fn


# GAs begin with a set of randomly generated states, called the k population
def gen_population(problem, size: int):
    population = []
    i = 0
    while i < size:
        new_state = problem.gen_random_state()
        if new_state not in population:
            population.append(new_state)
            i += 1
    return population


def get_fitness(problem, state):
    return problem.get_value(state)


def set_fitness_fn(problem):
    return partial(get_fitness, problem)


# function GENETIC-ALGORITHM(population, FITNESS-FN) returns an individual
#   inputs: population, a set of individuals
#   FITNESS-FN, a function that measures the fitness of an individual
#   repeat
#       new population ←empty set
#       for i = 1 to SIZE(population) do
#           x ←RANDOM-SELECTION(population, FITNESS-FN)
#           y ←RANDOM-SELECTION(population, FITNESS-FN)
#           child ←REPRODUCE(x , y)
#           if (small random probability) then child ←MUTATE(child )
#           add child to new population
#       population ←new population
#   until some individual is fit enough, or enough time has elapsed
#   return the best individual in population, according to FITNESS-FN


def genetic(population, fitness_fn, problem, select_fn, crossover_fn, mutate_fn, cull_fn, max_generations=1000,
            mutate_rate=0.1, verbose=False, plot_heuristic=False):
    generations = 0
    current_best = population[0]  # asume que el mejor es el primero
    current_best_value = fitness_fn(current_best)
    if plot_heuristic:
        h_values = []
    while generations < max_generations:
        if plot_heuristic:
            h_values.append(problem.heuristic_cost(current_best))
        new_population = []
        len_population = len(population)
        for i in range(len_population//2):
            parent1, parent2 = select_fn(fitness_fn, population)  # selecciona 2 individuos
            child1, child2 = crossover_fn(parent1, parent2)
            if random.random() < mutate_rate:
                mutate_fn(child1)
            if random.random() < mutate_rate:
                mutate_fn(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = cull_fn(population, new_population, fitness_fn)
        generations += 1
        current_best = population[0]
        current_best_value = abs(fitness_fn(current_best))
        if problem.goal_test(fitness_fn(current_best)):
            if verbose:
                print_sol(problem, current_best, current_best_value, generations, max_generations)
            if plot_heuristic:
                plot_heuristic_fn(h_values, "genetic")
            return current_best, current_best_value, generations
    if verbose:
        print_sol(problem, current_best, current_best_value, generations, max_generations)
    if plot_heuristic:
        plot_heuristic_fn(h_values, "genetic")
    # return the best individual in population, according to FITNESS-FN
    return current_best, current_best_value, generations
