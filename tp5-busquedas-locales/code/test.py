from n_queens_problem import NQueensProblem
import genetic.genetic as gen
import genetic.selection as selection
import genetic.crossover as crossover
import genetic.mutation as mutation
import genetic.culling as culling

prob = NQueensProblem(8)
pop = gen.gen_population(prob, 50)
select_fn = selection.set_selection_type(selection.tournament_selection, 10)
crossover_fn = crossover.set_crossover_type(crossover.order_crossover)
mutate_fn = mutation.set_mutation_type(mutation.random_swap)
cull_fn = culling.set_cull_type(culling.elitism_cull)
fitness_fn = gen.set_fitness_fn(prob)

g = gen.genetic(pop, fitness_fn, prob, select_fn, crossover_fn, mutate_fn, cull_fn)
print(g)
prob.print_board(g)
print(f"fitness: {fitness_fn(g)}, heuristic: {prob.heuristic_cost(g)}")
