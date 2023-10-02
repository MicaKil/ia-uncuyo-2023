from n_queens_problem import NQueensProblem
import genetic.genetic as genetic
import genetic.selection as selection
import genetic.crossover as crossover
import genetic.mutation as mutation
import genetic.culling as culling

n = 10
problem = NQueensProblem(n)
population_size = 10 * n
population = genetic.gen_population(problem, population_size)
select_fn = selection.set_selection_type(selection.tournament_selection, population_size // 4)
crossover_fn = crossover.set_crossover_type(crossover.order_crossover)
mutate_fn = mutation.set_mutation_type(mutation.random_swap)
cull_fn = culling.set_cull_type(culling.elitism_cull)
fitness_fn = genetic.set_fitness_fn(problem)

genetic.genetic(population, fitness_fn, problem, select_fn, crossover_fn, mutate_fn, cull_fn, verbose=True,
                plot_heuristic=True)
