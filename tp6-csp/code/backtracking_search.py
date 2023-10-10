from variable_and_value_ordering import select_unassigned_variable, order_domain_values
from inference import inference
from copy import deepcopy


# function BACKTRACKING-SEARCH(csp) returns a solution, or failure
#   return BACKTRACK({ }, csp)

global states_explored


def backtracking_search(csp):
    global states_explored
    states_explored = 0
    solution = backtrack([], csp)
    return solution, states_explored


# function BACKTRACK(assignment, csp) returns a solution, or failure
#   if assignment is complete then return assignment
#   var ← SELECT-UNASSIGNED-VARIABLE(csp)
#   for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do
#       if value is consistent with assignment then
#           add {var = value} to assignment
#           inferences ← INFERENCE(csp, var , value)
#           if inferences != failure then
#               add inferences to assignment
#               result ← BACKTRACK(assignment, csp)
#               if result != failure then
#                   return result
#       remove {var = value} and inferences from assignment
#   return failure

def backtrack(assignment: list, csp):
    global states_explored
    states_explored += 1
    if len(assignment) == len(csp.variables):
        return sorted(assignment, key=lambda variable: variable.index)
    # print(assignment)
    var = select_unassigned_variable(assignment, csp)
    var_old = deepcopy(var)
    # print("\n", var)
    sorted_domain = order_domain_values(var, assignment, csp)
    # print("sorted_domain: ", sorted_domain)
    for value in sorted_domain:
        csp_old = deepcopy(csp)
        if csp.is_consistent(var, value, assignment):
            var.value = value
            assignment.append(var)
            # print("assignment: ", assignment)
            if inference(csp, var):
                # print("inference: ", csp)
                result = backtrack(assignment, csp)
                if result is not None:
                    return result
        if var in assignment:
            assignment.remove(var)
        undo_var(var, var_old)
        undo_csp(csp, csp_old)
    return None


def undo_var(var, var_old):
    var.value = var_old.value
    var.domain = var_old.domain
    var.index = var_old.index
    return var


def undo_csp(csp, csp_old):
    for var, var_old in zip(csp.variables, csp_old.variables):
        undo_var(var, var_old)
    return csp


# ----------------------------------------------------------------------------------------------------------------------
from n_queens_CSP import NQueensCSP

p = NQueensCSP(8)
s, r = backtracking_search(p)
print(s)
print(r)
states_ = [var.value for var in s]
p.print_board(states_)
print(p.heuristic_cost(states_))
