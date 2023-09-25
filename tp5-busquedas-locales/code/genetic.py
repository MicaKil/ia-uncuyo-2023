# C) Implementar un algoritmo genético para resolver el problema del punto A. Además de la implementación en código del
# mismo, se deberán incluir detalles respecto a
# 1. Definición de los individuos de la población
# 2. Estrategia de selección
# 3. Estrategia de reemplazo
# 4. Operadores.

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
# function REPRODUCE(x , y) returns an individual
#   inputs: x , y, parent individuals
#   n←LENGTH(x ); c←random number from 1 to n
#   return APPEND(SUBSTRING(x, 1, c), SUBSTRING(y, c + 1, n))


import random


# GAs begin with a set of randomly generated states, called the k population
def gen_population(size: int, problem):
    population = []
    for i in range(size):
        population.append(problem.gen_random_state())
    return population


# each state is rated by the objective function, or (in GA terminology) the fitness function.
def fitness_fn(state, problem):
    return problem.get_value(state)


#two pairs are selected for reproduction
class Selection:
    def __init__(self, problem, population, type="tournament"):
        self.problem = problem
        self.population = population
        self.population_size = len(population)
        self.type = type

    def select(self):
        match self.type:
            case "tournament":
                return self.tournament_selection()
            case "ranking":
                return self.roulette_selection()
            case _:
                raise Exception("Invalid selection type")

    def tournament_selection(self, k=10):
        # se seleccionan k individuos de la población al azar
        selected = random.sample(self.population, k)
        # los 2 mejores individuos del torneo son seleccionados para reproducción
        return sorted(selected, key=lambda x: self.problem.get_value(x))[:2]

    def roulette_selection(self):
        # se calcula la probabilidad de selección de cada individuo
        fitness = [self.problem.get_value(state) for state in self.population]
        total_fitness = sum(fitness)
        probabilities = [f / total_fitness for f in fitness]
        # se seleccionan 2 individuos al azar
        selected = random.choices(self.population, weights=probabilities, k=2)
        return selected