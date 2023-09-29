# let the hunger games begin
import random
from functools import partial


def elitism_cull(population, children, fitness):
    # se ordenan los individuos de mayor a menor según su valor/fitness
    new_population = sorted(population + children, key=lambda x: -fitness(x))
    return new_population[:len(population)]  # los mejores individuos son seleccionados


def random_cull(population, children, fitness):
    new_population = random.sample(population + children, len(population))
    # se ordenan los individuos de mayor a menor según su valor/fitness
    # para que el primero sea el mejor
    sort = sorted(new_population, key=lambda x: -fitness(x))
    return sort[:len(population)]


def cull(population, children, fitness, cull_type=elitism_cull):
    return cull_type(population, children, fitness)


# retorna una función parcializada con el tipo de culling
def set_cull_type(cull_type=elitism_cull):
    return partial(cull, cull_type=cull_type)
