def print_sol(problem, current, current_value, evaluations, max_evaluations):
    heuristic_cost = problem.heuristic_cost(current)
    if problem.goal_test(current_value):
        print("Solución encontrada.")
    else:
        print("Máximo local alcanzado.")
    if evaluations >= max_evaluations:
        print("Máximo de evaluaciones alcanzado.")
        print(f"Estado: {current}, \nValor: {abs(current_value)}, \nHeurística: {heuristic_cost}")
    else:
        print(f"Estado: {current}, \nValor: {abs(current_value)}, \nHeurística: {heuristic_cost},"
              f"\nEstados Evaluados: {evaluations}")
